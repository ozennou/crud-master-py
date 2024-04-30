#!/bin/bash

/etc/init.d/rabbitmq-server start

rabbitmqctl add_user ${RABBITMQ_USER} ${RABBITMQ_PASSWD}
rabbitmqctl set_user_tags ${RABBITMQ_USER} administrator
rabbitmqctl set_permissions -p / ${RABBITMQ_USER} ".*" ".*" ".*"

rabbitmqadmin -u $RABBITMQ_USER -p $RABBITMQ_PASSWD declare exchange name=$RABBIT_EXCHANGE type=direct
rabbitmqadmin -u $RABBITMQ_USER -p $RABBITMQ_PASSWD declare queue name=$RABBIT_QUEUE
rabbitmqadmin -u $RABBITMQ_USER -p $RABBITMQ_PASSWD declare binding source=$RABBIT_EXCHANGE destination=$RABBIT_QUEUE routing_key=order

/etc/init.d/rabbitmq-server stop

exec rabbitmq-server