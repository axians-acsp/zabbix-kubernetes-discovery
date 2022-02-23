from kubernetes import client
import json

def getNode(name=None):
    """
    description: get all or specific node
    return: list
    """
    kubernetes = client.CoreV1Api()

    nodes = []

    for node in kubernetes.list_node().items:
        node_healthz = kubernetes.connect_get_node_proxy_with_path(name=node.metadata.name, path="healthz")
        node_status = kubernetes.read_node_status(name=node.metadata.name)

        json = {
            "name": node.metadata.name,
            "uid": node.metadata.uid,
            "status": node_healthz,
            "capacity": node_status.status.capacity,
            "allocatable": node_status.status.allocatable
        }

        if name == json['name']:
            return [json]
        if any(n['name'] == json['name'] for n in nodes):
            continue

        nodes.append(json)

    return nodes


def getDaemonset(name=None):
    """
    description: get all or specific daemonset
    return: list
    """
    kubernetes = client.AppsV1Api()

    daemonsets = []

    for daemonset in kubernetes.list_daemon_set_for_all_namespaces().items:

        json = {
            "name": daemonset.metadata.name,
            "namespace": daemonset.metadata.namespace,
            "replicas": {
                "desired": daemonset.status.desired_number_scheduled,
                "current": daemonset.status.current_number_scheduled,
                "available": daemonset.status.number_available,
                "ready": daemonset.status.number_ready
            }
        }

        for i in ["desired", "current", "available", "ready"]:
            if json['replicas'][i] is None:
                json['replicas'][i] = 0

        if name == json['name']:
            return [json]
        if any(d['name'] == json['name'] for d in daemonsets):
            continue

        daemonsets.append(json)

    return daemonsets


def getVolume(name=None):
    """
    description: get all or specific persistent volume claim
    return: list
    """
    kubernetes = client.CoreV1Api()

    volumes = []

    for node in kubernetes.list_node().items:
        node_info = kubernetes.connect_get_node_proxy_with_path(name=node.metadata.name, path="stats/summary").replace("'", "\"")
        node_json = json.loads(node_info)

        for pod in node_json['pods']:

            if not "volume" in pod:
                continue

            for volume in pod['volume']:

                if not "pvcRef" in volume:
                    continue
                else:
                    volume['namespace'] = volume['pvcRef']['namespace']

                for i in ["time", "pvcRef"]:
                    del volume[i]

                if name == volume['name']:
                    return [volume]

                if any(v['name'] == volume['name'] for v in volumes):
                    continue
                
                if "-token-" in volume['name']:
                    continue

                volumes.append(volume)

    return volumes


def getDeployment(name=None):
    """
    description: get all or specific deployment
    return: list
    """
    kubernetes = client.AppsV1Api()

    deployments = []

    for deployment in kubernetes.list_deployment_for_all_namespaces().items:

        json = {
            "name": deployment.metadata.name,
            "namespace": deployment.metadata.namespace,
            "replicas": {
                "desired": deployment.status.replicas,
                "ready": deployment.status.ready_replicas,
                "available": deployment.status.available_replicas
            }
        }

        for i in ["desired", "ready", "available"]:
            if json['replicas'][i] is None:
                json['replicas'][i] = 0

        if name == json['name']:
            return [json]
        if any(d['name'] == json['name'] for d in deployments):
            continue

        deployments.append(json)

    return deployments
