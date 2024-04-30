#!/bin/sh

while ! PGPASSWORD=$DB_PASSWD psql -U $DB_USER -d postgres -h inventory-db -c "SELECT datname FROM pg_database WHERE datname='$DB_NAME';" | grep -q $DB_NAME; do
    echo "the database not ready yet"
    sleep 2
done

exec python3 ./app/app.py