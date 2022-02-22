![](.github/assets/zabbix-kubernetes-discovery.png)

<p align="center">
  <a style="text-decoration:none" href="https://github.com/axians-acsp/zabbix-kubernetes-discovery/blob/main/LICENSE.md">
    <img alt="License" src="https://img.shields.io/github/license/axians-acsp/zabbix-kubernetes-discovery?logo=github&color=0&label=License&style=flat-square">
  </a>
  <a style="text-decoration:none" href="https://github.com/axians-acsp/zabbix-kubernetes-discovery/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/axians-acsp/zabbix-kubernetes-discovery?logo=github&color=0&label=Issues&style=flat-square">
  </a>
  <a style="text-decoration:none" href="https://github.com/axians-acsp/zabbix-kubernetes-discovery/actions/workflows/docker.yml">
    <img alt="Pipeline Docker" src="https://img.shields.io/github/workflow/status/axians-acsp/zabbix-kubernetes-discovery/Build%20and%20publish%20Docker?logo=github&color=0&label=Pipeline%20Docker&style=flat-square">
  </a>
  <a style="text-decoration:none" href="https://github.com/axians-acsp/zabbix-kubernetes-discovery/actions/workflows/helm.yml">
    <img alt="Pipeline Helm" src="https://img.shields.io/github/workflow/status/axians-acsp/zabbix-kubernetes-discovery/Helm%20Release?logo=github&color=0&label=Pipeline%20Helm&style=flat-square">
  </a>
</p>

# Zabbix Kubernetes Discovery

## Introduction

Kubernetes monitoring for Zabbix with discovery objects:

* Nodes
* DaemonSets
* Deployments
* PersistentVolumeClaims

Works with 2 variables only:

* `ZABBIX_ENDPOINT`: Zabbix server/proxy where the datas will be sent
* `KUBERNETES_NAME`: Name of your Kubernetes cluster on Zabbix (host)

## Install

Before installation, you need to create `zabbix-monitoring` namespace in your cluster:

```bash
$ kubectl create namespace zabbix-monitoring
```

### Helm from local

```bash
$ helm upgrade --install zabbix-kubernetes-discovery \
    ./helm/zabbix-kubernetes-discovery/ \
    --values ./helm/zabbix-kubernetes-discovery/values.yaml \
    --namespace zabbix-monitoring \
    --set namespace.name="zabbix-monitoring" \
    --set environment.ZABBIX_ENDPOINT="zabbix-proxy.example.com" \
    --set environment.KUBERNETES_NAME="kubernetes-cluster-example"
```

### Helm from repo

```bash
$ helm repo add acsp https://helm.acsp.io
$ helm upgrade --install zabbix-kubernetes-discovery \
    acsp/zabbix-kubernetes-discovery \
    --namespace zabbix-monitoring
    --set namespace.name="zabbix-monitoring" \
    --set environment.ZABBIX_ENDPOINT="zabbix-proxy.example.com" \
    --set environment.KUBERNETES_NAME="kubernetes-cluster-name"
```

## Development

### Manual build

You can build Docker image manually like this:

```bash
$ docker build -t zabbix-kubernetes-discovery .
```

## Contributing

All contributions are welcome! Please fork the main branch, create a new branch and then create a pull request.
