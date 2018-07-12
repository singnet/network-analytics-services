# Tested on python3.6

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite



class BipartiteGraphs:


    def __init__(self):

        # self.truth_value = False
        # self.return_message = ''

        pass


    def bipartite_graph(self,input_0,input_1):


        # Making sure both input bipartitions contain at least one node

        if len(input_0['bipartite_0']) <= 0:

            return[False,'Parameter bipartite_0 does not contain at least one element',{}]

        if len(input_0['bipartite_1']) <= 0:

            return [False, 'Parameter bipartite_1 does not contain at least one element', {}]

        # Making sure parameter edges contains at least one element/node

        if len(input_1['edges']) <= 0:
            return [False, 'Parameter edges does not contain at least one element', {}]

        # Making sure parameter edges contains all elements as lists/arrays

        for i in range(len(input_1['edges'])):
            if isinstance(input_1['edges'][i],list):
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array', (i),{}]
            if len(input_1['edges'][i]) != 2:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain two edges', (i),{}]
            if input_1['edges'][i][0] is '' or input_1['edges'][i][0] is None or input_1['edges'][i][1] is '' or input_1['edges'][i][1] is None:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain at least one element', (i),{}]


        # With respect to the validity of edges provided, given an edge [bipartite_0_node_x,bipartite_1_node_y],
        # if either of the elements doesn’t belong to the respective bipartition_0 or bipartition_1, then an error occurs.

        # First we need to automatically determine whether index 0 or 1 correspond to bipartion_0 or bipartition_1
        edge_0 = None
        edge_1 = None
        if input_1['edges'][0] in input_0['bipartite_0']:
            edge_0 = 0
            edge_1 = 1
        elif input_1['edges'][0] in input_0['bipartite_1']:
            edge_0 = 1
            edge_1 = 0
        else:
            return[False, 'Edge element at zero-indexed position 0 is not contained in either of the bipartitions',{}]

        edge_0_text = 'bipartite_'+str(edge_0)
        edge_1_text = 'bipartite_'+str(edge_1)


        # Make sure an edge element is found in at least one of the given bipartition inputs
        for i in range(len(input_1['edges'])):
            if input_1['edges'][i][0] not in input_0[edge_0_text] or input_1['edges'][i][0] not in input_0[edge_1_text]:
                return [False, 'Edge element at zero-indexed position {} is not contained in either of the bipartitions'.format(i),{}]
            if input_1['edges'][i][1] not in input_0[edge_0_text] or input_1['edges'][i][1] not in input_0[edge_1_text]:
                return [False, 'Edge element at zero-indexed position {} is not contained in either of the bipartitions'.format(i),{}]

        # Make sure all edge labels are found in the respecitve bipartitions

        for i in range(len(input_1['edges'])):
            if input_1['edges'][i][0] not in input_0[edge_0_text]:
                return [False,'Edge element at zero-indexed position {} belongs to the wrong bipartition'.format(i), {}]
            if input_1['edges'][i][1] not in input_0[edge_1_text]:
                return [False,'Edge element at zero-indexed position {} belongs to the wrong bipartition'.format(i), {}]

        # Using networkx's utility to check if input graph is bipartite
        G = nx.Graph()
        G.add_nodes_from(input_0[edge_0_text],bipartite=edge_0)
        G.add_nodes_from(input_0[edge_1_text],bipartite=edge_1)
        G.add_edges_from(input_1['edges'])

        truth_val = bipartite.is_bipartite(G)
        if not truth_val:
            return[False,'Input graph is not a bipartite graph',{}]



        output = {}

        output['bipartite_0'] = input_0['bipartite_0']
        output['bipartite_1'] = input_0['bipartite_1']
        output['edges'] = input_1['edges']




        return [True,'success',output]


    def projected_graph(self,input_0,input_1,input_2):

        # Anyway you might need to update the error doc wrt the new error handlers

        # And you need to do code review too.

        output = {}






        return output



__end__ = '__end__'


if __name__ == '__main__':

    pass