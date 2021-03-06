#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cluster_manager import ClusterManager
from kafka import KafkaNodeManager
from zookeeper import ZookeeperNodeManager
from setup import (AmazonLinux1Manager, AmazonLinux2Manager, CentOS7Manager, CentOS8Manager)
from worker import WorkerNodeManager
from master import MasterNodeManager

# ClusterManager('setup', CentOS8Manager).deploy()
# ClusterManager('setup', CentOS7Manager).deploy()
# ClusterManager('setup', AmazonLinux1Manager).deploy()
# ClusterManager('setup', AmazonLinux2Manager).deploy()

kafka_manager = ClusterManager('kafka', KafkaNodeManager)
kafka_manager.destroy()
kafka_manager.clean_data()  # remove

zookeeper_manager = ClusterManager('zookeeper', ZookeeperNodeManager)
zookeeper_manager.destroy()
zookeeper_manager.clean_data()  # remove
zookeeper_manager.deploy()
zookeeper_manager.configure()
zookeeper_manager.start()

kafka_manager.deploy()
kafka_manager.configure()
kafka_manager.start()

# worker_manager = ClusterManager('worker', WorkerNodeManager)
# worker_manager.destroy()
# worker_manager.deploy()

# master_manager = ClusterManager('master', MasterNodeManager)
# master_manager.destroy()
# master_manager.deploy()
