# Tested on python3.6

import networkx as nx
from networkx.algorithms import bipartite


class BipartiteGraphs:


    def __init__(self):

        # self.truth_value = False
        # self.return_message = ''

        self.networkx_graph = None

        pass


    def bipartite_graph(self,input_0,input_1):

        # 1 / 0

        # Make sure that the right fields exist and are array data types
        if 'bipartite_0' not in input_0:
            return[False,'Parameter bipartite_0 does not exist in given input',{}]
        if not isinstance(input_0['bipartite_0'],list):
            return [False, 'Parameter bipartite_0 does not have an array value', {}]
        if 'bipartite_1' not in input_0:
            return[False,'Parameter bipartite_1 does not exist in given input',{}]
        if not isinstance(input_0['bipartite_1'],list):
            return [False, 'Parameter bipartite_1 does not have an array value', {}]
        if 'edges' not in input_1:
            return[False,'Parameter edges does not exist in given input',{}]
        if not isinstance(input_1['edges'],list):
            return [False, 'Parameter edges does not have an array value', {}]

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
            if not isinstance(input_1['edges'][i],list):
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array'.format(i),{}]
            if len(input_1['edges'][i]) != 2:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain two edges'.format(i),{}]
            if input_1['edges'][i][0] is '' or input_1['edges'][i][0] is None or input_1['edges'][i][1] is '' or input_1['edges'][i][1] is None:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain at least one element'.format(i),{}]


        # With respect to the validity of edges provided, given an edge [bipartite_0_node_x,bipartite_1_node_y],
        # if either of the elements doesn’t belong to the respective bipartition_0 or bipartition_1, then an error occurs.

        # First we need to automatically determine whether index 0 or 1 correspond to bipartion_0 or bipartition_1
        edge_0 = None
        edge_1 = None

        if input_1['edges'][0][0] in input_0['bipartite_0']:
            edge_0 = 0
            edge_1 = 1
        elif input_1['edges'][0][0] in input_0['bipartite_1']:
            edge_0 = 1
            edge_1 = 0
        else:
            return[False, 'Edge element at zero-indexed position 0 is not contained in either of the bipartitions',{}]

        edge_0_text = 'bipartite_'+str(edge_0)
        edge_1_text = 'bipartite_'+str(edge_1)


        # Make sure an edge element is found in at least one of the given bipartition inputs
        for i in range(len(input_1['edges'])):
            if input_1['edges'][i][0] not in input_0[edge_0_text] and input_1['edges'][i][0] not in input_0[edge_1_text]:
                return [False, 'Edge element at zero-indexed position {} is not contained in either of the bipartitions'.format(i),{}]
            if input_1['edges'][i][1] not in input_0[edge_0_text] and input_1['edges'][i][1] not in input_0[edge_1_text]:
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

        self.networkx_graph = G


        output = {}

        output['bipartite_0'] = input_0['bipartite_0']
        output['bipartite_1'] = input_0['bipartite_1']
        output['edges'] = input_1['edges']




        return [True,'success',output]


    def projected_graph(self,input_0,input_1,input_2):

        # Make sure the right fields exist
        if 'bipartite_0' not in input_0:
            return[False,'Parameter bipartite_0 does not exist in given input',{}]

        if 'bipartite_1' not in input_0:
            return[False,'Parameter bipartite_1 does not exist in given input',{}]

        if 'edges' not in input_0:
            return[False,'Parameter edges does not exist in given input',{}]

        if 'nodes' not in input_1:
            return[False,'Parameter nodes does not exist in given input',{}]

        # Checking given graph is valid bipartite graph

        ret_val = self.bipartite_graph({'bipartite_0':input_0['bipartite_0'],'bipartite_1':input_0['bipartite_1']},{'edges':input_0['edges']})

        if not ret_val[0]:
            return ret_val

        # Checking validity of the nodes parameter

        if not isinstance(input_1['nodes'], list):
            return[False,'Parameter nodes does not contain an array',{}]

        if len(input_1['nodes']) <= 0:
            return [False, 'Parameter nodes does not contain at least one element', {}]

        # Checking nodes to project onto all belong to a single biparition and of course
        # they are actually found in one of the bipartitions

        edge = None

        if input_1['nodes'][0] in input_0['bipartite_0']:
            edge = 0
        elif input_1['nodes'][0] in input_0['bipartite_1']:
            edge = 1
        else:
            return [False, 'Node element at zero-indexed position 0 is not contained in either of the bipartitions', {}]

        edge_text = 'bipartite_' + str(edge)

        # Make sure that all elements are found in the discovered bipartition
        for i in range(len(input_1['nodes'])):
            if input_1['nodes'][i] not in input_0[edge_text]:
                return [False, 'Node element at zero-indexed position {} is not contained in {}'.format(i,edge_text), {}]

        P = None

        if input_2 == 'none':
            P = bipartite.projected_graph(self.networkx_graph, input_1['nodes'])
        elif input_2 == 'multigraph':
            P = bipartite.projected_graph(self.networkx_graph, input_1['nodes'],multigraph=True)
        elif input_2 == 'degree':
            P = bipartite.weighted_projected_graph(self.networkx_graph, input_1['nodes'])
        elif input_2 == 'degree_ratio':
            P = bipartite.weighted_projected_graph(self.networkx_graph, input_1['nodes'], ratio=True)
        elif input_2 == 'Newman':
            P = bipartite.collaboration_weighted_projected_graph(self.networkx_graph, input_1['nodes'])
        elif input_2 == 'Jaccard':
            P = bipartite.overlap_weighted_projected_graph(self.networkx_graph, input_1['nodes'])
        elif input_2 == 'Jaccard_modified':
            P = bipartite.overlap_weighted_projected_graph(self.networkx_graph, input_1['nodes'], jaccard=False)
        else:
            return [False, 'Unkown weighting logic specified', {}]

        output = {}

        output['nodes'] = list(P.nodes())
        output['edges'] = []
        output['weights'] = []

        weight_q_mark = True

        for i in list(P.edges(data=True)):
            output['edges'].append(list(i)[:2])

            if weight_q_mark:
                if 'weight' in list(i)[2]:
                    output['weights'].append(list(i)[2]['weight'])
                else:
                    weight_q_mark = False




        return [True,'success',output]


__end__ = '__end__'


if __name__ == '__main__':

    pass