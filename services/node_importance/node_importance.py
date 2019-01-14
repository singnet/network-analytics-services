# Tested on python3.6
import pandas as pd
import numpy as np

import networkx as nx

from networkx.algorithms.connectivity import minimum_st_node_cut
from networkx.algorithms.connectivity import minimum_st_edge_cut

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


import check_graph_validity

class NodeImportance:

    def __init__(self):
        self.cv = check_graph_validity.Graphs()

    def construct_graph(self,graph,directed):
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
        return G


    def find_central_nodes(self,graph,e=None,usebounds=False,directed=False):

        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False

        
        if type(usebounds) != bool:
            Print("usebounds must be boolean")
            return False

        G = self.construct_graph(graph,directed)

        result = nx.algorithms.distance_measures.center(G)

        output={}
        output["central_nodes"] = result

        return True,'success',str(output)

    def find_eccentricity(self,graph, v=None, sp=None,directed=False):

        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False

        
        G = self.construct_graph(graph,directed)

        result = nx.algorithms.distance_measures.eccentricity(G, v,sp)

        output={}
        output["eccentricity"] = result

        return True,'success',str(output)

    def find_degree_centrality(self,graph,directed=False):
        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False
        G = self.construct_graph(graph,directed)

        result = nx.algorithms.centrality.degree_centrality(G)

        output={}
        output["degree_centrality"] = result

        return True,'success',str(output)


    def find_closeness_centrality(self,graph, nodes, normalized=True,directed=False):

        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False
        G = self.construct_graph(graph,directed)

        result = nx.algorithms.bipartite.centrality.closeness_centrality(G, nodes, normalized=True)
        

        output={}
        output["closeness_centrality"] = result

        return True,'success',str(output)
        


    def find_betweenness_centrality(self,graph,k=None, normalized=True, weight=None, endpoints=False, seed=None,directed=False):
        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False

        G = self.construct_graph(graph,directed)

        result = nx.algorithms.centrality.betweenness_centrality(G,k=None, normalized=True, weight=None, endpoints=False, seed=None)

        output={}
        output["betweenness_centrality"] = result

        return True,'success',str(output)

    def find_pagerank(self,graph, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None,directed=False):
        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False
        G = self.construct_graph(graph,directed)

        result = nx.algorithms.link_analysis.pagerank_alg.pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)

        output={}
        output["pagerank"] = result

        return True,'success',str(output)

    def find_eigenvector_centrality(self,graph, max_iter=100, tol=1e-06, nstart=None, weight=None,directed=False):
        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False
        G = self.construct_graph(graph,directed)

        result = nx.algorithms.centrality.eigenvector_centrality(G, max_iter, tol, nstart, weight)

        output={}
        output["eigenvector_centrality"] = result

        return True,'success',str(output)

    def find_hub_matrix(self,graph, nodelist=None,directed=False):
        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False
        G = self.construct_graph(graph,directed)

        result = nx.algorithms.link_analysis.hits_alg.hub_matrix(G,  nodelist)

        # output={}
        # output["hub_matrix"] = result

        return True,'success',str(result)

    def find_authority_matrix(self,graph, nodelist=None,directed=False):
        ret = self.cv.is_valid_graph(graph)

        if not ret:
            print("Input is not a Valid graph")
            return False
        G = self.construct_graph(graph,directed)

        result = nx.algorithms.link_analysis.hits_alg.authority_matrix(G,  nodelist)

        output={}
        output["authority_matrix"] = result

        return True,'success',str(result)








