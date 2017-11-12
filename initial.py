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


def loadSigns(filename):
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
                line_arr = line.split()
                if line_arr[0] == line_arr[1]:
    				continue
                node1 = int(line_arr[0])
                node2 = int(line_arr[1])
                sign = int(line_arr[2])
                signs[(node1, node2)] = sign
                signs[(node2, node1)] = sign
    return signs


def computeTriadCounts(G, signs):
    """
    :param - G: graph
    :param - signs: Dictionary of signs (key = node pair (a,b), value = sign)

    return type: List, each position representing count of t0, t1, t2, and t3, respectively.
    return: Return the counts for t0, t1, t2, and t3 triad types. Count each triad
    only once and do not count self edges.
    """

    triad_count = [0, 0, 0, 0] # each position represents count of t0, t1, t2, t3, respectively
    
    # Remove self-edges
    for edge in G.Edges():
      srcNId = edge.GetSrcNId()
      dstNId = edge.GetDstNId()
      if srcNId == dstNId: 
        G.DelEdge(srcNId, dstNId)

    counted = set()

    for NI in G.Nodes():
        Id = NI.GetId()
        print Id
        deg = NI.GetDeg()
        for nth in range(deg):
            nId = NI.GetNbrNId(nth)
            ndeg = G.GetNI(nId).GetDeg()
            for nnth in range(ndeg):
                nnId = G.GetNI(nId).GetNbrNId(nnth)
                if Id == nnId: 
                  continue

                if G.IsEdge(Id, nnId):
                  tup = tuple(sorted([Id, nId, nnId]))

                  # Check the Set
                  if (tup in counted):
                    continue

                  # Insert Triad into set
                  counted.add(tup)
    
                  # Count Triads
                  numPos = 0
                  if (signs[(Id, nId)] == 1):
                    numPos = numPos + 1
                  if (signs[(nId, nnId)] == 1):
                    numPos = numPos + 1
                  if (signs[(Id, nnId)] == 1):
                    numPos = numPos + 1

                  triad_count[numPos] = triad_count[numPos] + 1  

    return triad_count


def displayStats(G, signs):
    '''
    :param - G: graph
    :param - signs: Dictionary of signs (key = node pair (a,b), value = sign)

    Computes and prints the fraction of positive edges and negative edges,
        and the probability of each type of triad.
    '''
    fracPos = 0
    fracNeg = 0
    probs = [0,0,0,0]

    for k,v in signs.iteritems():
      if v > 0:
        fracPos = fracPos + 1
      elif v < 0:
        fracNeg = fracNeg + 1

    fracPos = fracPos / 2
    fracNeg = fracNeg / 2
    total = fracPos + fracNeg
    fracPos = fracPos / float(total)
    fracNeg = fracNeg / float(total)

    print 'Fraction of Positive Edges: %0.4f' % (fracPos)
    print 'Fraction of Negative Edges: %0.4f' % (fracNeg)

    for i in range(4):
        print "Probability of Triad t%d: %0.4f" % (i, probs[i])


# Data Load
print "Loading Unweighted Graphs:"
print "Loading epinions graph..."
epinionsGr = snap.TUNGraph.New()
epinionsGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/soc-sign-epinions.txt", 0, 1)

print "Loading slashdot graph..."
slashdotGr = snap.TUNGraph.New()
slashdotGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/soc-sign-Slashdot090221.txt", 0, 1)

"""
print "Loading wikipedia graph..."
wikiGr = snap.TUNGraph.New()
wikiGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/wiki-Vote.txt", 0, 1)
"""
print


print "Loading Weighted Graphs:"
print "Loading bitcoin alpha graph..."
btcAlphaGr = snap.TUNGraph.New()
btcAlphaGr = snap.LoadEdgeList(snap.PUNGraph, "Datasets/soc-sign-bitcoinalpha.csv", 0, 1)

print "Loading bitcoin otc graph..."
btcOTCGr = snap.TUNGraph.New()
btcOTCGr = snap.LoadEdgeList(snap.PNGraph, "Datasets/soc-sign-bitcoinotc.csv", 0, 1)
print


print "Balance"
print "Status"
print


print "Compute Triad Counts:"

print "Epinions graph..."
signs = loadSigns("Datasets/soc-sign-epinions.txt")
triad_count = computeTriadCounts(epinionsGr, signs)

for i in range(4):
    print "Count of Triad t%d: %d" % (i, triad_count[i])

total_triads = float(sum(triad_count)) if sum(triad_count) != 0 else 1
for i in range(4):
    print "Fraction of Triad t%d: %0.4f" % (i, triad_count[i]/total_triads)

displayStats(epinionsGr, signs)
