# Tested on python3.6
import pandas as pd
import numpy as np

import networkx as nx

from networkx.algorithms.connectivity import minimum_st_node_cut
from networkx.algorithms.connectivity import minimum_st_edge_cut

import check_graph_validity

class Graphs:

    def __init__(self):


        pass

    def min_nodes_to_remove(self,graph,source_node,target_node):

        cv = check_graph_validity.Graphs()
        ret = cv.is_valid_min_nodes_graph(graph,source_node,target_node)
        if(not ret[0]):
            ret.append({})
            print (ret)
            return ret
        
        try:
            # construct networkx graph from given graph
            G = nx.Graph()
            G.add_nodes_from(graph['nodes'])
            G.add_edges_from(graph['edges'])

        except Exception as e:
            return [False, str(e),{}]
        

        output = {}

        # get the minimum set of nodes/edges to disconnect source_node and targert_node 
        nodes = list(minimum_st_node_cut(G , source_node, target_node))
        edges = list(minimum_st_edge_cut(G , source_node, target_node))
        edges = [list(e) for e in edges]
        
        output["nodes"] = nodes
        output["edges"] = edges


        return [True, 'success', output]

    def most_important_nodes_edges(self, graph, source_nodes, target_nodes, T=0, normalized=False, directed=False):

        cv=check_graph_validity.Graphs()
        ret = cv.is_valid_most_important_graph(graph, source_nodes, target_nodes,T)
        if(not ret[0]):
            ret.append({})
            print (ret)
            return ret
      
        try:
            # construct networkx graph from given graph
            if (directed):
                G=nx.DiGraph()
            else:    
                G = nx.Graph()
            G.add_nodes_from(graph['nodes'])
            G.add_edges_from(graph['edges'])

            if 'weights' in graph:
            	for i in range(len(graph['edges'])):
            	    G[graph['edges'][i][0]][graph['edges'][i][1]]['weight'] = graph['weights'][i]
        except Exception as e:
                	return ["False", str(e),{}]

        output={}
        clearDict={}
       
        if (T == 0):
            
            result=nx.betweenness_centrality_subset(G, source_nodes, target_nodes, normalized, weight='weights')
            #remove nodes that are either in source_node or in target_node
            for key,val in result.items():
                if (not(key in source_nodes or key in target_nodes)):
                 clearDict[key]=val   
            print(clearDict)

            
        elif (T == 1):
            result =nx.edge_betweenness_centrality_subset(G, source_nodes, target_nodes, normalized, weight='weights')
            for key,val in result.items():
                 #remove nodes that are either in source_node or in target_node
                if(not(key[0] in source_nodes or key[0] in target_nodes or key[1] in source_nodes or key[1] in target_nodes)):
                    clearDict[key]=val
            print(clearDict)


        output["betweenness_centrality"] = list(max(clearDict.items(), key=lambda k: k[1]))    #result

        print (output)


        return [True, 'success', output]

__end__ = '__end__'


if __name__ == '__main__':

    pass