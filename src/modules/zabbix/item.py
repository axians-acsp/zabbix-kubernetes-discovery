from pyzabbix import ZabbixMetric

def zabbixItemNode(clustername, nodes=[]):
    """
    description: create a item for node
    return: class ZabbixMetric
    """
    sender = []

    for node in nodes:
        sender.append(ZabbixMetric(clustername, "kubernetes.node.healthz[{}]".format(node['name']), node['status']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.capacity.cpu[{}]".format(node['name']), node['capacity']['cpu']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.capacity.memory[{}]".format(node['name']), node['capacity']['memory']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.capacity.pods[{}]".format(node['name']), node['capacity']['pods']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.allocatable.cpu[{}]".format(node['name']), node['allocatable']['cpu']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.allocatable.memory[{}]".format(node['name']), node['allocatable']['memory']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.allocatable.pods[{}]".format(node['name']), node['allocatable']['pods']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.current.pods[{}]".format(node['name']), node['current']['pods']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.current.podsUsed[{}]".format(node['name']), node['current']['pods_used']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.node.current.podsFree[{}]".format(node['name']), node['current']['pods_free']),)

    return sender


def zabbixItemDaemonset(clustername, daemonsets=[]):
    """
    description: create a item for daemonset
    return: class ZabbixMetric
    """
    sender = []

    for daemonset in daemonsets:
        sender.append(ZabbixMetric(clustername, "kubernetes.daemonset.desiredReplicas[{}]".format(daemonset['name']), daemonset['replicas']['desired']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.daemonset.currentReplicas[{}]".format(daemonset['name']), daemonset['replicas']['current']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.daemonset.availableReplicas[{}]".format(daemonset['name']), daemonset['replicas']['available']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.daemonset.readyReplicas[{}]".format(daemonset['name']), daemonset['replicas']['ready']),)

    return sender


def zabbixItemVolume(clustername, volumes=[]):
    """
    description: create a item for persistent volume claim
    return: class ZabbixMetric
    """
    sender = []

    for volume in volumes: 
        sender.append(ZabbixMetric(clustername, "kubernetes.volumeclaim.availableBytes[{}]".format(volume['name']), volume['availableBytes']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.volumeclaim.capacityBytes[{}]".format(volume['name']), volume['capacityBytes']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.volumeclaim.usedBytes[{}]".format(volume['name']), volume['usedBytes']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.volumeclaim.inodesFree[{}]".format(volume['name']), volume['inodesFree']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.volumeclaim.inodes[{}]".format(volume['name']), volume['inodes']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.volumeclaim.inodesUsed[{}]".format(volume['name']), volume['inodesUsed']),)

    return sender


def zabbixItemDeployment(clustername, deployments=[]):
    """
    description: create a item for deployment
    return: class ZabbixResponse
    """
    sender = []

    for deployment in deployments:
        sender.append(ZabbixMetric(clustername, "kubernetes.deployment.availableReplicas[{}]".format(deployment['name']), deployment['replicas']['available']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.deployment.readyReplicas[{}]".format(deployment['name']), deployment['replicas']['ready']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.deployment.desiredReplicas[{}]".format(deployment['name']), deployment['replicas']['desired']),)

    return sender


def zabbixItemStatefulset(clustername, statefulsets=[]):
    """
    description: create a item for statefulset
    return: class ZabbixResponse
    """
    sender = []

    for statefulset in statefulsets:
        sender.append(ZabbixMetric(clustername, "kubernetes.statefulset.availableReplicas[{}]".format(statefulset['name']), statefulset['replicas']['available']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.statefulset.readyReplicas[{}]".format(statefulset['name']), statefulset['replicas']['ready']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.statefulset.desiredReplicas[{}]".format(statefulset['name']), statefulset['replicas']['desired']),)

    return sender


def zabbixItemCronjob(clustername, cronjobs=[]):
    """
    description: create a item for cronjob
    return: class ZabbixResponse
    """
    sender = []

    for cronjob in cronjobs:
        sender.append(ZabbixMetric(clustername, "kubernetes.cronjob.exitcode[{}]".format(cronjob['name']), cronjob['status']['status']['exitcode']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.cronjob.restart[{}]".format(cronjob['name']), cronjob['status']['status']['restart']),)
        sender.append(ZabbixMetric(clustername, "kubernetes.cronjob.reason[{}]".format(cronjob['name']), cronjob['status']['status']['reason']),)

    return sender
