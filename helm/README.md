# Zabbix Kubernetes Discovery Helm Chart

This directory contains a chart for Kubernetes monitoring for Zabbix.
See [the README.md there](./zabbix-kubernetes-discovery/README.md) for
instructions on how to use it.

## Publishing

We use Github pages to publish the Helm chart as a versioned package. The
tarballs and index.yaml file are updated automatically (Github Actions).

More details in [Axians Helm repository here](https://helm.acsp.io).

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

## Uninstall

```bash
$ helm delete zabbix-kubernetes-discovery \
    --namespace zabbix-monitoring
```

## Parameters

| Name                           | Description  | Type    | Value |
|--------------------------------|--------------|---------|-------
| `namespace.name`               |              | string  | `zabbix-monitoring`                                         |
| `rbac.create`                  |              | boolean | `true`                                                      |
| `rbac.name`                    |              | string  | `zabbix-kubernetes-discovery`                               |
| `rbac.rolebinding`             |              | string  | `zabbix-kubernetes-discovery`                               |
| `serviceAccount.create`        |              | boolean | `true`                                                      |
| `serviceAccount.name`          |              | string  | `zabbix-kubernetes-discovery`                               |
| `deployment.name`              |              | string  | `zabbix-kubernetes-discovery`                               |
| `deployment.image.name`        |              | string  | `ghcr.io/axians-acsp/zabbix-kubernetes-discovery:v1.1.0`    |
| `deployment.image.pullPolicy`  |              | string  | `IfNotPresent`                                              |
| `deployment.replicas`          |              | integer | `1`                                                         |
| `deployment.strategy`          |              | string  | `Recreate`                                                  |
| `environment.ZABBIX_ENDPOINT`  |              | string  | `""`                                                        |
| `environment.KUBERNETES_NAME`  |              | string  | `""`                                                        |
| `crontab.name`                 |              | string  | `zabbix-kubernetes-discovery`                               |
| `crontab.schedule.discovery`   |              | string  | `0 * * * *`                                                 |
| `crontab.schedule.item`        |              | string  | `*/3 * * * *`                                               |
| `resources.requests.cpu`       |              | string  | `50m`                                                       |
| `resources.requests.memory`    |              | string  | `128Mi`                                                     |
| `resources.limits.cpu`         |              | string  | `1000m`                                                     |
| `resources.limits.memory`      |              | string  | `1Gi`                                                       |
| `nodeSelector`                 |              | dict    | `{}`                                                        |
| `tolerations`                  |              | list    | `[]`                                                        |
| `affinity`                     |              | dict    | `{}`                                                        |
