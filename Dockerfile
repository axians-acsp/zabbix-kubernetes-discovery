FROM ubuntu:20.04

LABEL description="Zabbix Kubernetes Discovery" \
      maintainer="Axians Cloud Services Provider" \
      repository="https://github.com/axians-acsp/zabbix-kubernetes-discovery"

ENV ZABBIX_ENDPOINT=""
ENV KUBERNETES_NAME=""
ENV SUPERCRONIC_VER="0.1.12"
ENV SUPERCRONIC_SHA="048b95b48b708983effb2e5c935a1ef8483d9e3e"

RUN apt update && \
    apt install -y telnet curl wget less vim traceroute iputils-ping python3 python3-pip && \
    rm -rf /var/lib/apt/lists && \
    pip3 install requests kubernetes py-zabbix && \
    mkdir -p /app /root/.kube && \
    touch /app/crontab

RUN curl -fsSLO "https://github.com/aptible/supercronic/releases/download/v${SUPERCRONIC_VER}/supercronic-linux-amd64" && \
    echo "${SUPERCRONIC_SHA}  supercronic-linux-amd64" | sha1sum -c - && \
    chmod +x supercronic-linux-amd64 && \
    mv supercronic-linux-amd64 /usr/local/bin/supercronic

COPY ./src/ /app/

RUN chmod +x /app/*.py

CMD ["/usr/local/bin/supercronic", "-split-logs", "-json", "/app/crontab"]
