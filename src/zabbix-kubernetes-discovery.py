#!/usr/bin/env python3

import argparse, sys, os
from random import randint
from time import sleep
from kubernetes import config
from pyzabbix import ZabbixSender
from modules.kubernetes.get import *
from modules.zabbix.item import *
from modules.zabbix.discovery import *

parser = argparse.ArgumentParser()
parser.add_argument("--zabbix-endpoint", dest="zabbix_endpoint", action="store", required=True, help="Set Zabbix endpoint (server)")
parser.add_argument("--kubernetes-name", dest="kubernetes_name", action="store", required=True, help="Set Kubernetes cluster name in Zabbix")
parser.add_argument("--monitoring-mode", dest="monitoring_mode", action="store", required=True, help="Mode of monitoring", choices=["volume","deployment","daemonset","node","statefulset"])
parser.add_argument("--monitoring-type", dest="monitoring_type", action="store", required=True, help="Type of monitoring", choices=["discovery", "item", "json"])
parser.add_argument("--object-name", dest="object_name", action="store", required=False, help="Name of object in Kubernetes", default=None)
parser.add_argument("--no-wait", dest="no_wait", action="store_true", required=False, help="Disable startup wait time", default=False)
args = parser.parse_args()

if os.path.exists("/var/run/secrets/kubernetes.io/serviceaccount/token"):
    config.load_incluster_config()
else:
    try:
        config.load_kube_config()
    except:
        print("Unable to find kubernetes cluster configuration")
        sys.exit(1)

zabbix = ZabbixSender(args.zabbix_endpoint)

if __name__ == "__main__":

    # Random sleep between 0 and 15 seconds
    if args.no_wait == False:
        timewait = randint(0,15)
        print("Starting in {} second(s)...".format(timewait))
        sleep(timewait)

    # Node
    if args.monitoring_mode == "node":
        if args.monitoring_type == "json":
            print("JSON output (node): {}".format(
                getNode(args.object_name)))
        if args.monitoring_type == "discovery":
            print("Zabbix discovery (node): {}".format(
                zabbix.send(zabbixDiscoveryNode(args.kubernetes_name, getNode(args.object_name)))))
        if args.monitoring_type == "item":
            print("Zabbix item (node): {}".format(
                zabbix.send(zabbixItemNode(args.kubernetes_name, getNode(args.object_name)))))

    # Daemonset
    if args.monitoring_mode == "daemonset":
        if args.monitoring_type == "json":
            print("JSON output (daemonset): {}".format(
                getDaemonset(args.object_name)))
        if args.monitoring_type == "discovery":
            print("Zabbix discovery (daemonset): {}".format(
                zabbix.send(zabbixDiscoveryDaemonset(args.kubernetes_name, getDaemonset(args.object_name)))))
        if args.monitoring_type == "item":
            print("Zabbix item (daemonset): {}".format(
                zabbix.send(zabbixItemDaemonset(args.kubernetes_name, getDaemonset(args.object_name)))))

    # Volumes
    if args.monitoring_mode == "volume":
        if args.monitoring_type == "json":
            print("JSON output (volume): {}".format(
                getVolume(args.object_name)))
        if args.monitoring_type == "discovery":
            print("Zabbix discovery (volume): {}".format(
                zabbix.send(zabbixDiscoveryVolume(args.kubernetes_name, getVolume(args.object_name)))))
        if args.monitoring_type == "item":
            print("Zabbix item (volume): {}".format(
                zabbix.send(zabbixItemVolume(args.kubernetes_name, getVolume(args.object_name)))))
    
    # Deployment
    if args.monitoring_mode == "deployment":
        if args.monitoring_type == "json":
            print("JSON output (deployment): {}".format(
                getDeployment(args.object_name)))
        if args.monitoring_type == "discovery":
            print("Zabbix discovery (deployment): {}".format(
                zabbix.send(zabbixDiscoveryDeployment(args.kubernetes_name, getDeployment(args.object_name)))))
        if args.monitoring_type == "item":
            print("Zabbix item (deployment): {}".format(
                zabbix.send(zabbixItemDeployment(args.kubernetes_name, getDeployment(args.object_name)))))

    # Statefulset
    if args.monitoring_mode == "statefulset":
        if args.monitoring_type == "json":
            print("JSON output (statefulset): {}".format(
                getStatefulset(args.object_name)))
        if args.monitoring_type == "discovery":
            print("Zabbix discovery (statefulset): {}".format(
                zabbix.send(zabbixDiscoveryStatefulset(args.kubernetes_name, getStatefulset(args.object_name)))))
        if args.monitoring_type == "item":
            print("Zabbix item (statefulset): {}".format(
                zabbix.send(zabbixItemStatefulset(args.kubernetes_name, getStatefulset(args.object_name)))))
