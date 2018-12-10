# Tested on python3.6
import pandas as pd
import numpy as np

import networkx as nx

from networkx.algorithms.connectivity import minimum_st_node_cut
from networkx.algorithms.connectivity import minimum_st_edge_cut

class Graphs:

    def __init__(self):


        pass

    def min_nodes_to_remove(self,graph,source_node,target_node):

        # make sure the edges are in a proper format
        if(not(isinstance(graph['edges'],list))):
            return [False, 'the supplied edge is not type array',{}]

        # make sure there is atleast more than one node is given
        if(len(graph['nodes']) < 1):
            return [False, 'graph should atleast contain two nodes',{}]

        # make sure there is atleast one edge is given
        if(len(graph['edges']) < 1):
            return [False, 'graph should atleast contain one edge',{}]
       
        for i in range(len(graph['edges'])):
            if(not(isinstance(graph['edges'][i],list))):
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array'.format(i),{}]
            if(len(graph['edges'][i]) != 2):
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain two nodes'.format(i),{}]
            if graph['edges'][i][0] is '' or graph['edges'][i][0] is None or graph['edges'][i][1] is '' or graph['edges'][i][1] is None:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does contain an empty node'.format(i),{}]

            # make sure all nodes specified in the edges exist in nodes list
            if(not(graph['edges'][i][0] in graph['nodes'])):
                graph['nodes'].append(graph['edges'][i][0])
            if(not(graph['edges'][i][1] in graph['nodes'])):
                graph['nodes'].append(graph['edges'][i][1])

        try:
            # construct networkx graph from given graph
            G = nx.Graph()
            G.add_nodes_from(graph['nodes'])
            G.add_edges_from(graph['edges'])

        except Exception as e:
            return [False, str(e),{}]

        # make sure source_node and target_node exists in the graph
        if(not(source_node in G )):
            return [False, 'node {} doesn’t exist in the graph'.format(source_node),{}]
        if(not(target_node in G )):
            return [False, 'node {} doesn’t exist in the graph'.format(target_node),{}]

        # make sure their is a path between the source_node and target_node
        if(not(nx.has_path(G ,source_node, target_node))): 
            return [False, 'no path exists between node {} and node {}'.format(source_node,target_node),{}]

        output = {}

        # get the minimum set of nodes/edges to disconnect source_node and targert_node 
        nodes = list(minimum_st_node_cut(G , source_node, target_node))
        edges = list(minimum_st_edge_cut(G , source_node, target_node))
        edges = [list(e) for e in edges]
        
        output["nodes"] = nodes
        output["edges"] = edges


        return [True, 'success', output]

    def most_important_nodes_edges(self, graph, source_nodes, target_nodes, T=0, normalized=True, weighted_edges=False):
        # make sure the edges are in a proper format
        if(not(isinstance(graph['edges'],list))):
            return [False, 'the supplied edge is not type array',{}]

        if 'weights' in graph:
            if(not(isinstance(graph['weights'],list))):
                return [False, 'the supplied weight is not type array',{}]
            if(len(graph['edges']) != len(graph['weights'])):
                return [False, 'the length of supplied edges and weights does not match',{}]


        # make sure there is atleast more than one node is given
        if(len(graph['nodes']) < 1):
            return [False, 'graph should atleast contain two nodes',{}]

        # make sure there is atleast one edge is given
        if(len(graph['edges']) < 1):
            return [False, 'graph should atleast contain one edge',{}]
       
        for i in range(len(graph['edges'])):
            if(not(isinstance(graph['edges'][i],list))):
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array'.format(i),{}]
            if(len(graph['edges'][i]) != 2):
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain two nodes'.format(i),{}]
            if graph['edges'][i][0] is '' or graph['edges'][i][0] is None or graph['edges'][i][1] is '' or graph['edges'][i][1] is None:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does contain an empty node'.format(i),{}]

            # make sure all nodes specified in the edges exist in nodes list
            if(not(graph['edges'][i][0] in graph['nodes'])):
                graph['nodes'].append(graph['edges'][i][0])
            if(not(graph['edges'][i][1] in graph['nodes'])):
                graph['nodes'].append(graph['edges'][i][1])

        # make sure source_nodes and target_nodes are a 1D array
        if(not(isinstance(source_nodes,list))):
            return [False, 'Element of the input source_nodes is not an array',{}]
        if(not(isinstance(target_nodes,list))):
            return [False, 'Element of the input target_nodes is not an array',{}]

       
       # make sure source_node and target_node exists in the graph
        if (not(all(elem in graph['nodes']  for elem in source_nodes))):	
            diff = list(set(source_nodes).difference(graph['nodes']))
            return [False, 'node {} doesn’t exist in the graph'.format(diff[0]),{}]

        if(not(all(elem in graph['nodes']  for elem in target_nodes))):
        	diff = list(set(target_nodes).difference(graph['nodes']))
        	return [False, 'node {} doesn’t exist in the graph'.format(diff[0]),{}]



        # make sure their is a path between the source_node and target_node
        found=False
        for node in source_nodes:
        	for t_node in target_nodes:
        		if (not((abs(node - t_node)==1))):
        		   for sublist in graph['edges']: # or in the node list
	        		    print (abs(node - t_node))
	        		    if (node in sublist and t_node in sublist):
	        		    	found=True
	        		    if (not found):
	        		    	return [False, 'no path exists from node {} to node {}'.format(node,t_node),{}]			





        if(T != 0 and T != 1 ):
            return [False, 'type can only be 0 or 1',{}]

        try:
            # construct networkx graph from given graph
            G = nx.Graph()
            G.add_nodes_from(graph['nodes'])
            G.add_edges_from(graph['edges'])

            if 'weights' in graph:
            	for i in range(len(graph['edges'])):
            	    G[graph['edges'][i][0]][graph['edges'][i][1]]['weight'] = graph['weights'][i]
        except Exception as e:
                	return ["False", str(e),{}]

        for node in source_nodes:
            # make sure nodes in source_nodes the graph
            if(not(node in G )):
                return [False, 'node {} doesn’t exist in the graph'.format(node),{}]

        for node in target_nodes:
            # make sure nodes in target_nodes the graph
            if(not(node in G )):
                return [False, 'node {} doesn’t exist in the graph'.format(node),{}]

        # make sure there is a path between source_nodes and target_nodes
        for s_node in source_nodes:
            for t_node in target_nodes:
                if not(nx.has_path(G,s_node,t_node)):
                    return [False, 'no path exists from node {} to node {}'.format(s_node,t_node),{}]

        output={}
        # result = Util.between_parallel(H,processes)
        if (T == 0):
        	result=nx.betweenness_centrality_subset(G, source_nodes, target_nodes, normalized, weight='weights')
        	print(result)
        elif (T == 1):
            result =nx.edge_betweenness_centrality_subset(G, source_nodes, target_nodes, normalized, weight='weights')
            print(result)

        output["betweenness_centrality"] = result


        return [True, 'success', output]

__end__ = '__end__'


if __name__ == '__main__':

    pass