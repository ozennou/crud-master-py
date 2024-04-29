FROM alpine:3.18

RUN apk update

RUN apk add --no-cache postgresql postgresql-contrib

RUN mkdir /run/postgresql

RUN chown postgres:postgres /run/postgresql

COPY ./tools/script.sh /tmp/script.sh

RUN chmod +x /tmp/script.sh

ENTRYPOINT [ "/tmp/script.sh" ]
