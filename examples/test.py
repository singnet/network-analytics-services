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



def bi_graph():
    B = nx.Graph()
    # B.add_edges_from([('a', 1), ('b', 1), (1, 2), ('b', 2)])
    B.add_edges_from([])
    print(B.nodes())
    print(B.edges())
    print(bipartite.is_bipartite(B))







__end__ = '__end__'



if __name__ == '__main__':


    bi_graph()

    pass