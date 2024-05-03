#!/bin/sh

if [ -f /var/lib/postgresql/data/PG_VERSION ];then
    exec postgres -D /var/lib/postgresql/data
fi

chmod 0700 /var/lib/postgresql

initdb -D /var/lib/postgresql/data

echo 'host all all 0.0.0.0/0 md5' >> /var/lib/postgresql/data/pg_hba.conf

echo listen_addresses=\'*\' >> /var/lib/postgresql/data/postgresql.conf

pg_ctl start -D /var/lib/postgresql/data

psql -d postgres -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';"

psql -d postgres -c "CREATE DATABASE ${DB_NAME} OWNER ${DB_USER};"
psql -d postgres -c "CREATE DATABASE test_db OWNER ${DB_USER};"

psql -d postgres -c "ALTER USER postgres WITH PASSWORD '${P_PASSWD}';"

pg_ctl stop -D /var/lib/postgresql/data

exec postgres -D /var/lib/postgresql/data