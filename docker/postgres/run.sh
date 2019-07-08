#!/usr/bin/env bash

docker run -p 5432:5432 \
    -e DJANGO_DB_NAME=mailerdb \
    -e DJANGO_DB_USER=postgres \
    -e DJANGO_DB_PASSWORD=allN1ghtL0ng22 \
    -e POSTGRES_PASSWORD=allN1ghtL0ng22 \
    -d \
    --name mailerdb-postgres \
    paulrogers/mailerdb_postgres