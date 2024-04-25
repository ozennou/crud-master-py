#!/bin/sh

DB_USER=amine
DB_PASSWORD=passwd
DB_NAME=movies_db



su -c "mkdir /var/lib/postgresql/data"  -s /bin/sh postgres

su -c "chmod 0700 /var/lib/postgresql" -s /bin/sh postgres

su -c "initdb -D /var/lib/postgresql/data" -s /bin/sh postgres

su -c "echo 'host all all 0.0.0.0/0 md5' >> /var/lib/postgresql/data/pg_hba.conf" -s /bin/sh postgres

su -c "echo listen_addresses=\'*\' >> /var/lib/postgresql/data/postgresql.conf" -s /bin/sh postgres

su -c "pg_ctl start -D /var/lib/postgresql/data" -s /bin/sh postgres

su -c "psql -d postgres -c \"CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';\"" -s /bin/sh postgres

su -c "psql -d postgres -c \"CREATE DATABASE ${DB_NAME} OWNER ${DB_USER};\"" -s /bin/sh postgres

su -c "pg_ctl stop -D /var/lib/postgresql/data" -s /bin/sh postgres

su -c "exec postgres -D /var/lib/postgresql/data" -s /bin/sh postgres