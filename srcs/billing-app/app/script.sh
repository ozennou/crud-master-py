#!/bin/sh

while ! PGPASSWORD=$BILLING_DB_PASSWORD psql -U $BILLING_DB_USER -d postgres -h $BILLING_DB_HOST -c "SELECT datname FROM pg_database WHERE datname='$BILLING_DB_NAME';" | grep -q $BILLING_DB_NAME; do
    echo "the database not ready yet"
    sleep 2
done

while ! nc -zv $RABBIT_HOST 5672; do
    echo "Waiting RabbitMQ..."
    sleep 2
done
sleep 5
while ! nc -zv $RABBIT_HOST 5672; do  # i do that cause i start and stop to configure rabbitmq.
    echo "Waiting RabbitMQ..."
    sleep 2
done

exec python3 ./app/app.py