#!/usr/bin/env python

from pyVim import connect

# vCenter login credential

vCenter_ip = ""
vCenter_user = ""
vCenter_pass = ""

cluster = connect.ConnectNoSSL(vCenter_ip, 443, vCenter_user, vCenter_pass)
