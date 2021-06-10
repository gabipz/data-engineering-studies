"""
#### Proposta
* Criar operador que envia mensagem para outro (XCom)
#### Dependências DAG
Nenhuma
#### Inputs
Nenhum
#### Outputs
Nenhum
"""

import os
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

from plugins.tools.dag_utils import get_dag_config_object


DAG_NAME = 'third_dag'
config = get_dag_config_object(dag_name=DAG_NAME)

default_args = {
    'owner': 'ADP',
    'depends_on_past': False,
    'catchup': False,
    #'email': [Variable.get(email) for email in config.email_to_variables],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=60),
    'start_date': datetime(year=2020, month=12, day=22),
    #'on_failure_callback': task_fail_slack_alert('SLACK_AIRFLOW_ERROR'),
}

dag = DAG(
    dag_id=DAG_NAME,
    description="DAG intended to determine which fruit is and to print",
    catchup=False,
    default_args=default_args,
    schedule_interval='@once',
    max_active_runs=1
)


dag.doc_md = __doc__


def send_fruit_list(fruits, **kwargs):
    kwargs['ti'].xcom_push(key='fruit_list', value=fruits)

def catch_fruit_list(**kwargs):
    fruit_list = kwargs['ti'].xcom_pull(task_ids='push_id', key='fruit_list')
    print(f'The fruits are {fruit_list}.')



slack_start = DummyOperator(task_id='slack_start', dag=dag)

slack_finished = DummyOperator(task_id='slack_finished', dag=dag)

push = PythonOperator(
    task_id='push_id',
    python_callable=send_fruit_list,
    op_kwargs={
        'fruits': config.fruits
    }, 
    provide_context=True,
    dag=dag
)

pull = PythonOperator(
    task_id=f'print_fruit',
    python_callable=catch_fruit_list,
    provide_context=True,
    dag=dag
)



slack_start >> push >> pull >> slack_finished
