################################################################################
# CS 224W (Fall 2017) - Project
# Weighted Sign Networks
# Author: akshayk@stanford.edu, vhying@stanford.edu
# Last Updated: Dec 06, 2017
################################################################################

import snap
import random
import numpy as np
import matplotlib.pyplot as plt
import powerlaw


def loadDirectedSigns(filename):
    """
    :param - filename: undirected graph with associated edge sign

    return type: dictionary (key = node pair (a,b), value = sign)
    return: Return sign associated with node pairs. Both pairs, (a,b) and (b,a)
    are stored as keys. Self-edges are NOT included.
    """
    signs = {}
    with open(filename, 'r') as ipfile:
      for line in ipfile:
        if line[0] != '#':
            if filename[-3:] == "csv":
              line_arr = line.split(',')
            else:
              line_arr = line.split()
            if line_arr[0] == line_arr[1]:
              continue
            node1 = int(line_arr[0])
            node2 = int(line_arr[1])
            sign = int(line_arr[2])
            signs[(node1, node2)] = sign

    return signs


def selfEdgeDel(G):
    # Remove self-edges
    for edge in G.Edges():
      srcNId = edge.GetSrcNId()
      dstNId = edge.GetDstNId()
      if srcNId == dstNId: 
        G.DelEdge(srcNId, dstNId)

    return G


# Data Load
print "Loading Weighted Graphs:"
print "Loading bitcoin alpha graph..."
btcAlphaGr = snap.TNGraph.New()
btcAlphaGr = snap.LoadEdgeList(snap.PNGraph, "Datasets/soc-sign-bitcoinalpha.csv", 0, 1, ',')
btcAlphaGr = selfEdgeDel(btcAlphaGr)
btcAlphaSigns = loadDirectedSigns("Datasets/soc-sign-bitcoinalpha.csv")

print "Loading bitcoin otc graph..."
btcOTCGr = snap.TNGraph.New()
btcOTCGr = snap.LoadEdgeList(snap.PNGraph, "Datasets/soc-sign-bitcoinotc.csv", 0, 1, ',')
btcOTCGr = selfEdgeDel(btcOTCGr)
btcOTCSigns = loadDirectedSigns("Datasets/soc-sign-bitcoinotc.csv")
print
