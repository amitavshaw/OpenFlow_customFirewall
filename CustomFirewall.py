#!/usr/bin/python
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr, IPAddr
from pox.lib.util import dpidToStr
import pox.lib.packet as pkt

firewallRules = [['10.0.0.1','10.0.0.4'],['10.0.0.2','10.0.0.6'],['10.0.0.3','10.0.0.6']]
log = core.getLogger()
class CustFirewall (EventMixin):
	def __init__ (self):
		self.listenTo(core.openflow)
	''' modifyRule modifies the flow by providing a match on 
	the basis of IP addresses. In the msg, action is omitted which is why this rule will drop packets. This is according to the openflow documentation'''
	def modifyRule (self, src, dst, duration = 0):
		msg = of.ofp_flow_mod()
		match = of.ofp_match(dl_type = 0x800,
				     nw_proto = pkt.ipv4.ICMP_PROTOCOL)
		match.nw_src = IPAddr(src)
		match.nw_dst = IPAddr(dst)
		msg.match = match
		self.connection.send(msg)

	def _handle_ConnectionUp (self, event):
		self.connection = event.connection
		for rule in firewallRules:
			self.modifyRule(rule[0],rule[1],0)
		log.info("Firewall rules installed on %s", dpidToStr(event.dpid))
def launch ():
    core.registerNew(CustFirewall)
