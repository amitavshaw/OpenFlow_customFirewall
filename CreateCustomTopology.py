#!/usr/bin/python
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller, OVSKernelSwitch, RemoteController
class CreateTopo( Topo ):
	def __init__( self ):
	# Initialize the topology
		Topo.__init__(self)
	# Add hosts h1, h2, h3, h4, h5, h6
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
	# Add switches s1, s2, s3, s4
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
	# Add links with bandwidths as per problem description
		self.addLink(s1, s2)
		self.addLink(h1, s1) 
		self.addLink(h2, s1)
		self.addLink(h3, s1)
		self.addLink(h4, s2)
		self.addLink(h5, s2)
		self.addLink(h6, s2)
def activateTopo():
	topology = CreateTopo()
	# mininet.net.Mininet type object initialization
	net = Mininet(topology,link=TCLink,controller=RemoteController) 
	# Starting the controller and switches.
	net.start() 
	print "Dumping host connections"
	dumpNodeConnections(net.hosts)
	# Initializing command line interface
	CLI(net)
	net.stop()
if __name__ == '__main__':
	# Setting log level to 'info' as the default level is 'warning'
	setLogLevel('info')
	activateTopo()
