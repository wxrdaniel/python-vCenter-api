#!/usr/bin/env python

from pyVim import connect

# vCenter login credential

vCenter_ip = ""
vCenter_user = ""
vCenter_pass = ""

# vCenter Cluster
cluster = connect.ConnectNoSSL(vCenter_ip, 443, vCenter_user, vCenter_pass)
searcher = cluster.content.searchIndex

# VM IP(s)
#vm_list = []
vm = ""

# Snapshot Info
snap_name = "Test Snap"
snap_description = "Snapshot created by python"
snap_memory = False
snap_quiesce = True


target_host = searcher.FindByIp(ip=str(ip), vmSearch=True)
snapshot = target_host.CreateSnapshot(snap_name, snap_description, snap_memory, snap_quiesce)

# if target_host.snapshot.rootSnapshotList[0]['name'] == snap_name:
#     return True
