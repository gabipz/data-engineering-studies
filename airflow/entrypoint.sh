#!/bin/bash

command=$1

airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@example.org -p admin
airflow db init
airflow $command




