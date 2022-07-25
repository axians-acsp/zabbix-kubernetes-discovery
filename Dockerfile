FROM ubuntu:22.04

LABEL description="Zabbix Kubernetes Discovery" \
      maintainer="Axians Cloud Services Provider" \
      repository="https://github.com/axians-acsp/zabbix-kubernetes-discovery"

WORKDIR /app

ENV ZABBIX_ENDPOINT=""
ENV KUBERNETES_NAME=""

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl iputils-ping python3 python3-pip && \
    rm -rf /var/lib/apt/lists && \
    pip3 install --no-cache-dir requests kubernetes py-zabbix && \
    mkdir -p /app /root/.kube && \
    touch /app/crontab

ARG SUPERCRONIC_VER="0.2.1"
ARG SUPERCRONIC_SHA="d7f4c0886eb85249ad05ed592902fa6865bb9d70"

RUN curl -fsSLO "https://github.com/aptible/supercronic/releases/download/v${SUPERCRONIC_VER}/supercronic-linux-amd64" && \
    echo "${SUPERCRONIC_SHA}  supercronic-linux-amd64" | sha1sum -c - && \
    chmod +x supercronic-linux-amd64 && \
    mv supercronic-linux-amd64 /usr/local/bin/supercronic

COPY ./src/ /app/

RUN chmod +x /app/*.py

CMD ["/usr/local/bin/supercronic", "-split-logs", "-json", "/app/crontab"]
