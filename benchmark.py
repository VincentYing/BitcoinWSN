################################################################################
# CS 224W (Fall 2017) - Project
# Weighted Sign Networks
# Author: akshayk@stanford.edu, vhying@stanford.edu
# Last Updated: Dec 06, 2017
################################################################################


import networkx as nx
import tidaltrust as tt


# Data Load
print "Loading Weighted Graphs:"
print "Loading bitcoin alpha graph..."
fh = open("Datasets/soc-sign-bitcoinalpha.csv", "r")
btcAlphaGr = nx.read_weighted_edgelist(fh, delimiter=',', nodetype=int)
fh.close()


# Tidaltrust of single edge.
print tt.compute_trust(btcAlphaGr, 1, 888)["trust"]
