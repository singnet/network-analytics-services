# Tested on python3.6

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite
from networkx.algorithms import distance_measures
from networkx.algorithms import centrality
from networkx.algorithms import link_analysis
import matplotlib.pyplot as plt
import random
import plotly as py
import plotly.graph_objs as go
import time
import math
import logging
import operator


def list_1():

    a = [[]]
    print(a.__len__())

def dict_2():

    a=5

    if 'r' not in a:
        print('not in')


def tuple_1():
    r = (4,'w',3)
    print(r[0])
    print(r[1])
    print(r[2])

def dict_1():

    r={'a':2,'b':3,5:8}

    if 5 in r:
        print('yes')

    s = 5

    try:
        if 4 in s:
            print('hi')
    except Exception as e:
        logging.exception("messagae")

def bi_graph():
    B = nx.Graph()
    # B.add_edges_from([('a', 1), ('b', 1), (1, 2), ('b', 2)])
    B.add_edges_from([('a', 1), ('b', 1), ('a', 2), ('c', 2)])
    B.add_edges_from([])
    print(list(B.nodes()))
    print(list(B.edges()))
    print(bipartite.is_bipartite(B))

    e = list(B.edges())

    f = []

    for i in e:
        f.append(list(i))
    print(f)

    # P = bipartite.collaboration_weighted_projected_graph(B,['a','b','c'])
    P = bipartite.projected_graph(B,['a','b','c'])
    print(list(P.nodes()))
    print(list(P.edges(data=True)))

    f = []

    for i in list(P.edges(data=True)):
        # print('i')
        # print(i)
        f.append(list(i)[:2])
        if 'weight' in list(i)[2]:
            print(i[2]['weight'])
        else:
            print('no weight')

    print(f)


def graph_1():
    G = nx.Graph()
    G.add_nodes_from([2, 3, 5, 6, 7])
    G.add_edges_from([[2, 3], [5, 3],[6,7],[7,2],[5,7]])
    print(list(G.nodes()))
    print(list(G.edges()))
    print(distance_measures.center(G))
    print(distance_measures.periphery(G))
    # print(distance_measures.center(G,e={12: 2, 13: 3, 15: 2, 16: 3}))
    # print(distance_measures.center(G,e={333: 3}))
    print(distance_measures.eccentricity(G))


def graph_2():
    G = nx.nx.DiGraph()
    # G.add_nodes_from([2, 3, 5, 6, 7])
    G.add_edges_from([[2, 3], [5, 3], [6, 7], [7, 2], [5, 7]])
    # G.add_path([2,3,6,7])
    # G.add_path([2,4,5])
    # print(list(G.nodes()))
    print(list(G.edges()))
    print(list(G.out_degree()))
    print(list(G.in_degree()))
    print(centrality.in_degree_centrality(G))
    print(link_analysis.pagerank(G,personalization={2:-4}))
    print(link_analysis.pagerank(G,dangling={5:0,7:1}))


def bet_subset():

    graph = {
        "nodes": [1, 2, 3, 4, 5, 6, 7, 8,9,10],
        "edges": [[1, 2], [1, 4], [2, 3], [2, 5], [3, 4], [3, 6], [2, 7], [3, 8],[7,9],[5,9],[9,10],[10,6]],
        "weights": [3, 4, 5, 6, 7, 8, 9, 10]

    }



    G = nx.Graph()
    G = nx.DiGraph()
    G.add_nodes_from(graph['nodes'])
    G.add_edges_from(graph['edges'])
    source_nodes = [5, 7]
    target_nodes = [6]

    result = nx.betweenness_centrality_subset(G, source_nodes, target_nodes, False)

    print(result)
    # print(list(max(result.items(), key=lambda k: k[1])))
    # print(result.items())
    # print(max(result.items(), key=operator.itemgetter(1)))

    highest = max(result.values())
    print(highest)
    print([k for k, v in result.items() if v == highest])

    result = nx.edge_betweenness_centrality_subset(G, source_nodes, target_nodes, False)
    print(result)

    highest = max(result.values())
    print(highest)
    print([k for k, v in result.items() if v == highest])









__end__ = '__end__'



if __name__ == '__main__':

    bet_subset()
    # graph_2()
    # graph_1()
    # list_1()
    # dict_2()
    # tuple_1()
    # dict_1()
    # bi_graph()

    pass