#!/bin/sh

#docker run --net=host -e POSTGRES_USER=airflow -e POSTGRES_PASSWORD=airflow -e POSTGRES_DB=airflow -e PGDATA=/var/lib/postgresql/data/pgdata -v pgdata:/var/lib/postgresql/data/pgdata -p 5432:5432 postgres

docker run --name postgresql --network airflow \
-e POSTGRES_USER=airflow -e POSTGRES_PASSWORD=airflow -e POSTGRES_DB=airflow -e PGDATA=/var/lib/postgresql/data/pgdata -v pgdata:/var/lib/postgresql/data/pgdata -p 5432:5432 postgres
