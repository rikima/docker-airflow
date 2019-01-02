#!/bin/sh

docker run --name webserver \
    --network airflow \
    -e LOAD_EX=n \
    -e EXECUTOR=Local \
    -e POSTGRES_USER=airflow \
    -e POSTGRES_PASSWORD=airflow \
    -e POSTGRES_DB=airflow \
    -v `pwd`/dags:/usr/local/airflow/dags \
    -v `pwd`/plugins:/usr/local/airflow/plugins \
    -p 8080:8080 \
my-airflow webserver