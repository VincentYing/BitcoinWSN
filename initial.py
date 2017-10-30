################################################################################
# CS 224W (Fall 2017) - Project
# Weighted Sign Networks
# Author: vhying@stanford.edu
# Last Updated: Oct 29, 2017
################################################################################

import snap
import random
import numpy as np
import matplotlib.pyplot as plt

# Data Load
print "Loading Data,"

print "Loading epinions graph..."
epinionsGr = snap.TUNGraph.New()
epinionsGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/soc-Epinions1.txt", 0, 1)

print "Loading slashdot graph..."
slashdotGr = snap.TUNGraph.New()
slashdotGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/soc-Slashdot0902.txt", 0, 1)

print "Loading wikipedia graph..."
wikiGr = snap.TUNGraph.New()
wikiGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/wiki-Vote.txt", 0, 1)

print "Loading bitcoin alpha graph..."
btcAlphaGr = snap.TUNGraph.New()
btcAlphaGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/soc-sign-bitcoinalpha.csv", 0, 1)

print "Loading bitcoin otc graph..."
btcOTCGr = snap.TUNGraph.New()
btcOTCGr = snap.LoadEdgeList(snap.PNGraph, "Datasets/soc-sign-bitcoinotc.csv", 0, 1)



