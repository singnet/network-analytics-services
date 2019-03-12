# Tested on python3.6
import pandas as pd
import numpy as np

import networkx as nx

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import check_graph_validity


class NodeImportance:

    def __init__(self):
        self.cv = check_graph_validity.Graphs()

    def construct_graph(self, graph, directed=False):
        try:
            # construct networkx graph from given graph
            if directed:
                G = nx.DiGraph()
            else:
                G = nx.Graph()
            G.add_nodes_from(graph['nodes'])
            G.add_edges_from(graph['edges'])
        except Exception as e:
            return [False, str(e), {}]

        try:
            if 'weights' in graph:
                for i in range(len(graph['edges'])):
                    G[graph['edges'][i][0]][graph['edges'][i][1]]['weight'] = graph['weights'][i]
        except Exception as e:
            pass

        return G


    def find_central_nodes(self, graph, usebounds=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph)
        result = nx.algorithms.distance_measures.center(G, usebounds=usebounds)

        return True, 'success', result

    # def find_central_nodes(self, graph, u=None, distance=None, wf_improved=True, reverse=False):
    #     ret = self.cv.is_valid_graph(graph)
    #     if not ret[0]:
    #         return ret
    #
    #     u = None if u == '' else u
    #     distance = None if distance == '' else distance
    #
    #     G = self.construct_graph(graph)
    #     result = nx.algorithms.centrality.closeness_centrality(G, u=u, distance=distance, wf_improved=wf_improved,
    #                                                            reverse=reverse)
    #     output = {"central_nodes": result}
    #     return True, 'success', output

    def find_Periphery(self, graph, usebounds=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph)
        result = nx.algorithms.distance_measures.periphery(G, usebounds=usebounds)

        return True, 'success', result

    def find_degree_centrality(self, graph, in_out=None, directed=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        if in_out == 'in':
            G = self.construct_graph(graph, directed=True)
            result = nx.algorithms.centrality.in_degree_centrality(G)
        elif in_out == 'out':
            G = self.construct_graph(graph, directed=True)
            result = nx.algorithms.centrality.out_degree_centrality(G)
        else:
            G = self.construct_graph(graph, directed)
            result = nx.algorithms.centrality.degree_centrality(G)
        if in_out is not None:
            output = {str(in_out) + "degree_centrality": result}
        else:
            output = {"degree_centrality": result}
        return True, 'success', output

    def find_closeness_centrality(self, graph, distance=False, wf_improved=True, reverse=False, directed=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)

        if 'weights' not in graph and distance:
            return False, 'distance parameter specified but weights are not given in input graph', {}

        if not distance:
            result = nx.algorithms.centrality.closeness_centrality(G, distance='weights', wf_improved=wf_improved, reverse=reverse)
        else:
            result = nx.algorithms.centrality.closeness_centrality(G, wf_improved=wf_improved, reverse=reverse)

        output = {"closeness_centrality": result}
        return True, 'success', output

    def find_betweenness_centrality(self, graph, k=None, normalized=True, weight=False, endpoints=False, seed=None,
                                    type='node', directed=False):
        ret = self.cv.is_valid_graph(graph)
        weight = None if weight == False else 'weights'
        type = 'node' if type == '' else type
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)
        k = None if k == 0 else k

        if type == 'edge':
            result = nx.algorithms.centrality.edge_betweenness_centrality(G, k=k, normalized=normalized, weight=weight,
                                                                          seed=seed)
        else:
            result = nx.algorithms.centrality.betweenness_centrality(G, k=k, normalized=normalized, weight=weight,
                                                                     endpoints=endpoints, seed=seed)
        output = {'betweenness_centrality': result}
        return True, 'success', output

    def find_pagerank(self, graph, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None,
                      weight=False, dangling=None, directed=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)

        alpha = 0.85 if alpha == 0.0 else alpha
        personalization = None if personalization == '' else personalization
        max_iter = 100 if max_iter == 0 else max_iter
        tol = 1e-06 if tol == 0.0 else tol
        dangling = None if dangling == '' else dangling
        weight = None if weight == False else 'weights'
        nstart_dict = None
        personalization_dict = None
        dangling_list = None

        try:
            if len(personalization.key) > 0:
                keys = personalization.key
                values = personalization.value
                for i in range(len(keys)):
                    personalization_dict[keys[i]] = values[i]
        except Exception as e:
            personalization_dict = None

        try:
            if len(nstart.key) > 0:
                keys = nstart.key
                values = nstart.value
                for i in range(len(keys)):
                    nstart_dict[keys[i]] = values[i]
        except Exception as e:
            nstart_dict = None

        try:
            if len(dangling.key) > 0:
                keys = dangling.key
                values = dangling.value
                for i in range(len(keys)):
                    dangling_list[keys[i]] = values[i]
        except Exception as e:
            dangling_list = None

        result = nx.algorithms.link_analysis.pagerank_alg.pagerank(G, alpha=alpha, personalization=personalization_dict,
                                                                   max_iter=max_iter,
                                                                   tol=tol, nstart=nstart_dict, weight=weight,
                                                                   dangling=dangling_list)
        output = {"pagerank": result}
        return True, 'success', output

    def find_eigenvector_centrality(self, graph, max_iter=100, tol=1e-06, nstart=None, weight=False, directed=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)

        weight = None if weight == False else "weights"
        nstart_dict = {}
        try:
            if len(nstart.keys) > 0:
                keys = nstart.key
                values = nstart.value
                for i in range(len(keys)):
                    nstart_dict[keys[i]] = values[i]
        except Exception as e:
            nstart_dict = None

        result = nx.algorithms.centrality.eigenvector_centrality(G, max_iter=max_iter, tol=tol, nstart=nstart_dict,
                                                                 weight=weight)
        output = {"eigenvector_centrality": result}
        return True, 'success', output

    def find_hits(self, graph, nodelist=None, mode='hub_matrix', directed=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)

        nodelist = None if nodelist == '' else nodelist
        if mode == 'authority_matrix':
            result = nx.algorithms.link_analysis.hits_alg.authority_matrix(G, nodelist)
            output = {"authority_matrix": result.tolist()}

        else:
            result = nx.algorithms.link_analysis.hits_alg.hub_matrix(G, nodelist)
            output = {"hub_matrix": result.tolist()}
        return True, 'success', output
