# Apache Airflow

O Airflow permite definir fluxos de trabalho que envolve consulta de dados de inúmeras fontes, tratamento e mineração de dados, de forma que possa ser feito de forma agendada ou não, ou seja, uma pipeline de dados.

Os fluxos de trabalho são criados por meio de scripts Python.

## Criando o docker-compose.yml

Em todo arquivo ```docker-compose.yml```, há uma espécie de receita para construção das diferentes aplicações. Primeiro, coloca-se a versão do Docker Compose que estamos utilizando e depois são adicionados os serviços - variando de aplicação para aplicação e que será pego de imagens já prontas ou construído através de um ```Dockerfile```.
```
version: '3'
services:
    service_name1:
        build:
            dockerfile: ..path..
```
É possível ver em maiores detalhes no próprio [docker-compose.yml](docker-compose.yml) que foi feito para iniciar o Flowditas, que está estruturado com os seguintes serviços:
- Redis (tem imagem pronta)
- Postgres (tem imagem pronta)
- Web Server (Dockerfile)

Além do [docker-compose.yml](docker-compose.yml), também foram criados os arquivos [Dockerfile](Dockerfile) (para construir a imagem do Airflow), o [requirements.txt](requirements.txt) (com os requerimentos da aplicação) e o [entrypoint.sh](entrypoint.sh) (que é um arquivo executável).

## Rodando a aplicação
Para "buildar" a aplicação:
```
docker-compose build

```
Para subir a aplicação:
```
docker-compose up -d
```

## Conceitos

Pipeline de dados é um conjunto de ações que realizará o processamento de dados específicos. Exemplo: Extrair dados da previsão do tempo dos próximos 7 dias da cidade de São Paulo e armazenar os dados.

- DAG: fluxo de trabalho (conjunto de tasks)
- Task: unidade mais básica da DAG
- Operator: blocos de construção de um DAG, eles contêm a lógica de como os dados são processados em um data pipeline e cada task é definida justamente pela instanciação de um operador.

### Arquitetura do airflow

Webserver: apresenta uma interface de usuário que nos permite inspecionar, acionar e acompanhar o comportamento dos DAGs e suas tarefas;
Pasta de arquivos DAG: armazena os arquivos DAGs criados. Ela é lida pelo agendador e executor;

Scheduler (agendador): lida com o acionamento dos fluxos de trabalho (DAGs) agendados e o envio de tarefas para o executor;

Banco de dados: usado pelo agendador, executor e webserver para armazenar os metadados e status do DAG e suas tarefas;

Executor: lida com as tarefas em execução. O Airflow possui vários executores, mas apenas um é utilizado por vez.

### Operators

Os operadores são classes Python que encapsulam a lógica para fazer uma unidade de trabalho, ou seja, uma tarefa. Eles definem as ações que serão concluídas para cada unidade de trabalho e abstraem muito código que teríamos que escrever. Quando instanciamos um operador e passamos os parâmetros necessários, a instância desse operador passa a ser uma tarefa.

Existem muitos tipos diferentes de operadores disponíveis no Airflow e o trabalho que cada um faz varia muito. Alguns dos operadores mais usados são:

- PythonOperator: executa uma função Python;
- BashOperator: executa um script bash;
- KubernetesPodOperator: executa uma imagem definida como imagem do Docker em um pod do Kubernetes;
- SnowflakeOperator: executa uma consulta em um banco de dados Snowflake;
- EmailOperator: envia um e-mail.

O Airflow tem um conjunto muito extenso de operadores disponíveis. No entanto, se não existir um operador para seu caso de uso, você também pode criar os seus próprios operadores.

#### PythonOperator

Este operador executa funções ou códigos python. Exemplo

```python
def extrai_dados(data_interval_end)
    pass

tarefa_1 = PythonOperator(
    task_id = 'extrai_dados',
    python_callable = extrai_dados, #chama a função
    op_kwargs = {'data_interval_end' : '{{data_interval_end.strftime("%Y-%m-%d")}}'} #pega os argumentos utilizados na função
    )

```

## Referências

- [Automatizando seu fluxo de trabalho com Airflow](https://medium.com/@gilsondev/automatizando-seu-fluxo-de-trabalho-com-airflow-4dbc1c932dcb)

- [Primeiros passos com o Apache Airflow: ETL fácil, robusto e de baixo custo](https://medium.com/data-hackers/primeiros-passos-com-o-apache-airflow-etl-f%C3%A1cil-robusto-e-de-baixo-custo-f80db989edae)

- [Documentation - Concepts (XCom)](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html?highlight=xcom#xcoms)

- [Airflow XComs examplo](https://big-data-demystified.ninja/2020/04/15/airflow-xcoms-example-airflow-demystified/)
