# OpenFlow Custom Firewall

Implementation of firewall on SDN using pox controller, a custom topology and custom firewall rules:
First the following network is connected using the “customTopology.py” script I developed. 
There are two switches and six hosts. The first three hosts such as h1, h2, h3 are connected to s1. The other three hosts such as h4, h5, h6 are connected to s3. The goal is to create firewall between h1 and h4; h2 and h6; h3 and h6.

## Firstly, the custom firewall is run using the pox controller:
**./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning misc.customFirewall**

This starts the pox controller and the learning algorithm listening on port 6633.

## Secondly, the topology is created. 
Order of running these scripts is important. Topology is supposed to be created only after starting the pox controller:

**sudo python customTopology.py**

The moment the topology is created, the pox controller starts learning as can be seen in the figure below. The firewalls between h1 and h4; h2 and h6; h3 and h6 are expected to be created.

## Results
The results of the “pingall” shows, as expected, that the to-and-fro traffic between h1 and h4; h3 and h6; h2 and h6 are absent.

## Improvements
Will be reading the firewall rules from a .csv file instead of hard coding the src, dest as it is now.

 
