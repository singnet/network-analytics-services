# Tested on python3.6

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import random
import plotly as py
import plotly.graph_objs as go
import time
import math
import logging



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









__end__ = '__end__'



if __name__ == '__main__':


    # tuple_1()
    # dict_1()
    bi_graph()

    pass