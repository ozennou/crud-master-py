FROM debian:12

RUN apt-get update && \
    apt-get install -y rabbitmq-server && \
    rabbitmq-plugins enable rabbitmq_management

COPY ./tools/script.sh /tmp/script.sh

RUN chmod +x /tmp/script.sh

ENTRYPOINT [ "/tmp/script.sh" ]
