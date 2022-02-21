![](.github/assets/zabbix-kubernetes-discovery.png)

<p align="center">
  <a style="text-decoration:none" href="https://github.com/axians-acsp/zabbix-kubernetes-discovery/blob/main/LICENSE.md">
    <img alt="License" src="https://img.shields.io/github/license/axians-acsp/zabbix-kubernetes-discovery?logo=github&color=0&label=License&style=flat-square">
  </a>
  <a style="text-decoration:none" href="https://github.com/axians-acsp/zabbix-kubernetes-discovery/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/axians-acsp/zabbix-kubernetes-discovery?logo=github&color=0&label=Issues&style=flat-square">
  </a>
  <a style="text-decoration:none" href="https://github.com/axians-acsp/zabbix-kubernetes-discovery/actions/workflows/docker.yml">
    <img alt="Pipeline" src="https://img.shields.io/github/workflow/status/axians-acsp/zabbix-kubernetes-discovery/Build%20and%20publish%20Docker?logo=github&color=0&label=Pipeline&style=flat-square">
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

### Helm from local

```bash
$ kubectl create namespace zabbix-monitoring
$ helm upgrade --install zabbix-kubernetes-discovery ./helm/ \
    -f ./helm/values.yaml \
    -n zabbix-monitoring \
    --set namespace.name="zabbix-monitoring" \
    --set environment.ZABBIX_ENDPOINT="zabbix-proxy.example.com" \
    --set environment.KUBERNETES_NAME="kubernetes-cluster-example"
```

### Helm from repo

## Development

### Manual build

You can build Docker image manually like this:

```bash
$ docker build -t zabbix-kubernetes-discovery .
```

## Contributing

All contributions are welcome! Please fork the main branch, create a new branch and then create a pull request.
