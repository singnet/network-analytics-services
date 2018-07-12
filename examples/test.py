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
    B.add_edges_from([])
    print(B.nodes())
    print(B.edges())
    print(bipartite.is_bipartite(B))







__end__ = '__end__'



if __name__ == '__main__':


    dict_1()
    # bi_graph()

    pass