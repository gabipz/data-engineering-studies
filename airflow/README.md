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

Além do [docker-compose.yml](docker-compose.yml), também foram criados os arquivos [Dockerfile](Dockerfile) (para construir a imagem do Airflow), o (requirements.txt)[requirements.txt] (com os requerimentos da aplicação) e o [entrypoint.sh](entrypoint.sh) (que é um arquivo executável).

## Rodando a aplicação
Para "buildar" a aplicação:
```
docker-compose build

```
Para subir a aplicação:
```
docker-compose up -d
```



## Referências

- [Automatizando seu fluxo de trabalho com Airflow](https://medium.com/@gilsondev/automatizando-seu-fluxo-de-trabalho-com-airflow-4dbc1c932dcb)

- [Primeiros passos com o Apache Airflow: ETL fácil, robusto e de baixo custo](https://medium.com/data-hackers/primeiros-passos-com-o-apache-airflow-etl-f%C3%A1cil-robusto-e-de-baixo-custo-f80db989edae)

- [Documentation - Concepts (XCom)](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html?highlight=xcom#xcoms)

- [Airflow XComs examplo](https://big-data-demystified.ninja/2020/04/15/airflow-xcoms-example-airflow-demystified/)
