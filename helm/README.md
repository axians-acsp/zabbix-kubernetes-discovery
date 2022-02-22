# Zabbix Kubernetes Discovery Helm Chart

This directory contains a chart for Kubernetes monitoring for Zabbix.
See [the README.md there](./zabbix-kubernetes-discovery/README.md) for
instructions on how to use it.

## Publishing

We use Github pages to publish the chart as a versioned package. The
tarballs and index.yaml file are updated with a script in that branch.

## Prerequisites

* Kubernetes v1.19+
* Helm 3.2.0+

## Install

```bash
$ helm repo add acsp https://helm.acsp.io
$ helm upgrade --install zabbix-kubernetes-discovery \
    acsp/zabbix-kubernetes-discovery \
    --namespace zabbix-monitoring
    --set namespace.name="zabbix-monitoring" \
    --set environment.ZABBIX_ENDPOINT="zabbix-proxy.example.com" \
    --set environment.KUBERNETES_NAME="kubernetes-cluster-name"
```

## Parameters

| Name                           | Description | Value |
|--------------------------------|-------------|-------|
| `namespace.name`               | | `zabbix-monitoring` |
| `rbac.create`                  | | `true` |
| `rbac.name`                    | | `zabbix-kubernetes-discovery` |
| `rbac.rolebinding`             | | `zabbix-kubernetes-discovery` |
| `serviceAccount.create`        | | `true` |
| `serviceAccount.name`          | | `zabbix-kubernetes-discovery` |
| `deployment.name`              | | `zabbix-kubernetes-discovery` |
| `deployment.image.name`        | | `ghcr.io/axians-acsp/zabbix-kubernetes-discovery:latest` |
| `deployment.image.pullPolicy`  | | `Always` |
| `deployment.replicas`          | | `1` |
| `deployment.strategy`          | | `Recreate` |
| `environment.ZABBIX_ENDPOINT`  | | `""` |
| `environment.KUBERNETES_NAME`  | | `""` |
| `crontab.name`                 | | `zabbix-kubernetes-discovery` |
| `crontab.schedule.discovery`   | | `0 * * * *` |
| `crontab.schedule.item`        | | `*/3 * * * *` |
| `resources.requests.cpu`       | | `10m` |
| `resources.requests.memory`    | | `32Mi` |
| `resources.limits.cpu`         | | `500m` |
| `resources.limits.memory`      | | `256Mi` |
| `nodeSelector`                 | | `{}` |
| `tolerations`                  | | `[]` |
| `affinity`                     | | `{}` |
