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


    def find_Periphery(self, graph, usebounds=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph)
        result = nx.algorithms.distance_measures.periphery(G, usebounds=usebounds)

        return True, 'success', result

    def find_degree_centrality(self, graph, in_out=''):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        if in_out not in ['','in','out']:
            return False,'Wrong in_out parameter specified',{}

        if in_out == 'in':
            G = self.construct_graph(graph, directed=True)
            result = nx.algorithms.centrality.in_degree_centrality(G)
        elif in_out == 'out':
            G = self.construct_graph(graph, directed=True)
            result = nx.algorithms.centrality.out_degree_centrality(G)
        else:
            G = self.construct_graph(graph)
            result = nx.algorithms.centrality.degree_centrality(G)

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
        if not ret[0]:
            return ret


        weight = None if weight == False else 'weights'
        seed = None if seed == 0 else seed
        k = None if k == 0 else k


        if type != 'node' and type != 'edge':
            return False,'type parameter can only be node or edge',{}
        if 'weights' not in graph and weight:
            return False, 'weight parameter specified but weights are not given in input graph', {}

        if k is not None:
            if k > len(graph['nodes']):
                return False, 'parameter k is larger than the number of nodes in the graph', {}

        if 'weights' in graph:
            if not all(i > 0 for i in graph['weights']) and weight is not None:
                return False, 'one or more weights in the graph are less than zero'

        G = self.construct_graph(graph, directed)

        if type == 'edge':
            result = nx.algorithms.centrality.edge_betweenness_centrality(G, k=k, normalized=normalized, weight=weight,
                                                                          seed=seed)
            output = {'betweenness_centrality': result,'type':'edge'}
        else:
            result = nx.algorithms.centrality.betweenness_centrality(G, k=k, normalized=normalized, weight=weight,
                                                                     endpoints=endpoints, seed=seed)
            output = {'betweenness_centrality': result, 'type': 'node'}

        return True, 'success', output

    def find_pagerank(self, graph, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None,
                      weight=False, dangling=None, directed=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)

        alpha = 0.85 if alpha == 0.0 else alpha
        personalization = None if personalization == None else personalization
        max_iter = 100 if max_iter == 0 else max_iter
        tol = 1e-06 if tol == 0.0 else tol
        dangling = None if dangling == None else dangling
        weight = None if weight == False else 'weights'
        nstart = None if nstart == None else nstart

        if 'weights' not in graph and weight:
            return False, 'weight parameter specified but weights are not given in input graph', {}


        ret = self.cv.is_valid_pagerank(graph,personalization,dangling,nstart)
        if not ret[0]:
            return ret

        result = nx.algorithms.link_analysis.pagerank_alg.pagerank(G, alpha=alpha, personalization=personalization,
                                                                   max_iter=max_iter,
                                                                   tol=tol, nstart=nstart, weight=weight,
                                                                   dangling=dangling)
        output = {"pagerank": result}
        return True, 'success', output

    def find_eigenvector_centrality(self, graph, max_iter=100, tol=1e-06, nstart=None, weight=False, directed=False, in_out=True):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)

        # Done for out-edges eigenvector centrality
        if not in_out and directed:
            G.reverse()

        max_iter = 100 if max_iter == 0 else max_iter
        tol = 1e-06 if tol == 0.0 else tol
        weight = None if weight == False else 'weights'
        nstart = None if nstart == None else nstart

        if 'weights' not in graph and weight:
            return False, 'weight parameter specified but weights are not given in input graph', {}

        ret = self.cv.is_valid_eigenvector_centrality(graph, nstart)

        if not ret[0]:
            return ret


        result = nx.algorithms.centrality.eigenvector_centrality(G, max_iter=max_iter, tol=tol, nstart=nstart,
                                                                 weight=weight)
        output = {"eigenvector_centrality": result}
        return True, 'success', output

    def find_hits(self, graph, max_iter=100, tol=1e-08, nstart=None, normalized=True, directed=False):
        ret = self.cv.is_valid_graph(graph)
        if not ret[0]:
            return ret

        G = self.construct_graph(graph, directed)


        max_iter = 100 if max_iter == 0 else max_iter
        tol = 1e-08 if tol == 0.0 else tol
        nstart = None if nstart == None else nstart

        ret = self.cv.is_valid_hits(graph, nstart)

        if not ret[0]:
            return ret

        result = nx.algorithms.link_analysis.hits_alg.hits(G, max_iter=max_iter, tol=tol, nstart=nstart, normalized=normalized)
        output = {"hubs": result[0],"authorities":result[1]}
        return True, 'success', output
