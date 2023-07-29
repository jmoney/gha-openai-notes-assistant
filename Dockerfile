FROM alpine:3.16

ADD main.py /app/main.py
COPY bin /app/bin

RUN apk update
RUN apk add --no-cache python3 github-cli

ENTRYPOINT [ "/app/bin/entrypoint.sh" ]