FROM alpine:3.16

ADD main.py /app/main.py
COPY bin /app/bin
RUN chmod +x /app/bin/entrypoint.sh

RUN apk update
RUN apk add --no-cache python3

ENTRYPOINT [ "/app/bin/entrypoint.sh" ]