"""
#### Proposta
Criar DAG que:
    * Print Hello World e é possível ver o print nos logs da DAG (Usar PythonOperator)
    * Criar 2 operadores Dummy (DummyOperator) nomeados como 'slack_start' e 'slack_finished'
    * Fazer o desenho da DAG iniciando com slack_start, PythonOperator e slackend

    * Tem que seguir os padrões do Flowditas
        * Tem que ter documentação
        * Tem que ter config
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

DAG_NAME = 'first_dag'
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

# Definição da objeto da DAG
dag = DAG(
    dag_id=DAG_NAME,
    description="DAG intended to print 'Hello world'.",
    catchup=False,
    default_args=default_args,
    schedule_interval='@once',
    max_active_runs=1
)

dag.doc_md = __doc__


def hello_world(config):
    #logging.info('Hello World')
    print('Hello World')



slack_start = DummyOperator(task_id='slack_start', dag=dag)

hello_world_op = PythonOperator(
    task_id='hello_world_id',
    python_callable=hello_world,
    op_kwargs={
        'config': config
    },
    dag=dag
)

slack_finished = DummyOperator(task_id='slack_finished', dag=dag)


slack_start >> hello_world_op >> slack_finished

