#!/bin/bash

RABBITMQ_USER=amine
RABBITMQ_PASSWD=passwd


/etc/init.d/rabbitmq-server start

rabbitmqctl add_user ${RABBITMQ_USER} ${RABBITMQ_PASSWD}
rabbitmqctl set_user_tags ${RABBITMQ_USER} administrator
rabbitmqctl set_permissions -p / ${RABBITMQ_USER} ".*" ".*" ".*"

/etc/init.d/rabbitmq-server stop

exec rabbitmq-server