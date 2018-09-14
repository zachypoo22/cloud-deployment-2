"""Part 2 of Lab 1

Instructions:
Wait for the profile instance to start
"""

import geni.portal as portal
import geni.rspec.pg as pg

request = portal.context.makeRequestRSpec()


node1 = request.XenVM("node-1")
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node1.routable_control_ip = "true"

iface1 = node1.addInterface("if1")
iface1.component_id = "eth1"
iface1.addAddress(pg.IPv4Address("192.168.1.1", "255.255.255.0"))


node2 = request.XenVM("node-2")
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
iface2 = node2.addInterface("if2")
iface2.component_id = "eth2"
iface2.addAddress(pg.IPv4Address("192.168.1.2",  "255.255.255.0"))

node3 = request.XenVM("node-3")
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
iface3 = node3.addInterface("if3")
iface3.component_id = "eth3"
iface3.addAddress(pg.IPv4Address("192.168.1.3",  "255.255.255.0"))


node4 = request.XenVM("node-4")
node4.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
iface4 = node4.addInterface("if4")
iface4.component_id = "eth4"
iface4.addAddress(pg.IPv4Address("192.168.1.4",  "255.255.255.0"))

# add network links
link = request.LAN("lan")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.addInterface(iface4)


portal.context.printRequestRSpec()
