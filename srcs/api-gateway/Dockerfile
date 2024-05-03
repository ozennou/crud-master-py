FROM alpine:3.18

RUN apk update

RUN apk add python3 py-pip postgresql

COPY ./app ./app

RUN pip install --no-cache-dir -r ./app/Requirements.txt

ENTRYPOINT [ "python3", "./app/app.py" ]