# Tested on python3.6

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite



class BipartiteGraphs:


    def __init__(self):

        self.truth_value = False
        self.return_message = ''


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
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array', (i)]
            if len(input_1['edges'][i]) != 2:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain two edges', (i)]
            if input_1['edges'][i][0] is '' or input_1['edges'][i][0] is None or input_1['edges'][i][1] is '' or input_1['edges'][i][1] is None:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain at least one element', (i)]


        # With respect to the validity of edges provided, given an edge [bipartite_0_node_x,bipartite_1_node_y],
        # if either of the elements doesn’t belong to the respective bipartition_0 or bipartition_1, then an error occurs.

        # First we need to automatically determine whether index 0 or 1 correspond to bipartion_0 or bipartition_1

        # Next: Start coding at 4, then move on to handling error 2










        output = {}

        output['bipartite_0'] = input_0['bipartite_0']
        output['bipartite_1'] = input_0['bipartite_1']
        output['edges'] = input_1['edges']




        return [self.truth_value,self.return_message,output]


    def projected_graph(self,input_0,input_1,input_2):


        output = {}






        return output




__end__ = '__end__'


if __name__ == '__main__':

    pass