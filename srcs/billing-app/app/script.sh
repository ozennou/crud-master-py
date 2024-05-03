#!/bin/sh

while ! PGPASSWORD=$DB_PASSWD psql -U $DB_USER -d postgres -h $DB_HOST -c "SELECT datname FROM pg_database WHERE datname='$DB_NAME';" | grep -q $DB_NAME; do
    echo "the database not ready yet"
    sleep 2
done

while ! nc -zv rabbitmq 5672; do
    echo "Waiting RabbitMQ..."
    sleep 2
done
sleep 5
while ! nc -zv rabbitmq 5672; do  # i do that cause i start and stop to configure rabbitmq.
    echo "Waiting RabbitMQ..."
    sleep 2
done

exec python3 ./app/app.py