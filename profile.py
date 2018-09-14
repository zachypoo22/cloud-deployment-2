import geni.portal as portal
import geni.rspec.pg as pg

request = portal.context.makeRequestRSpec()


node1 = request.XenVM("node-1")
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
iface1 = node1.addInterface("if1")
iface1.addAddress(pg.IPv4Address("192.168.1.1",  "255.255.255.0"))
node1.routable_control_ip = True


node2 = request.XenVM("node-2")
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
iface2 = node2.addInterface("if1")
iface2.addAddress(pg.IPv4Address("192.168.1.2",  "255.255.255.0"))


node3 = request.XenVM("node-3")
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
iface3 = node3.addInterface("if1")
iface3.addAddress(pg.IPv4Address("192.168.1.3",  "255.255.255.0"))


node4 = request.XenVM("node-4")
node4.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
iface4 = node4.addInterface("if1")
iface4.addAddress(pg.IPv4Address("192.168.1.4",  "255.255.255.0"))

portal.context.printRequestRSpec()
