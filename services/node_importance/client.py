import os
import grpc
from service_spec_node_importance import node_importance_pb2
from service_spec_node_importance import node_importance_pb2_grpc

from snet_grpc_wrapper_node_importance import *


class ClientTest():
    def __init__(self, port='localhost:5002'):
        self.port = port

    def open_grpc_channel(self):
        channel = grpc.insecure_channel(self.port)
        stub = node_importance_pb2_grpc.NodeImportanceStub(channel)
        return stub

    def get_graph(self, graph):

        try_weight = False
        try_edge = False

        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
            try_edge = True
        except Exception as e:
            pass

        try:
            weights_req = graph['weights']
            try_weight = True
        except Exception as e:
            pass

        try:

            if not try_weight and not try_edge:
                graph_in = node_importance_pb2.Graph(nodes=graph["nodes"])
            elif not try_weight and try_edge:
                graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req)
            elif try_weight and not try_edge:
                graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], weights=weights_req)
            else:
                graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=weights_req)

        except:

            if not try_weight and not try_edge:
                graph_in = node_importance_pb2.Graph()
            elif not try_weight and try_edge:
                graph_in = node_importance_pb2.Graph(edges=edges_req)
            elif try_weight and not try_edge:
                graph_in = node_importance_pb2.Graph(weights=weights_req)
            else:
                graph_in = node_importance_pb2.Graph(edges=edges_req, weights=weights_req)

        return graph_in

    def find_closeness_centrality(self, stub, graph, distance=False, wf_improved=True, reverse=False, directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.ClosenessCentralityRequest(graph=graph_in, distance=distance, wf_improved=wf_improved, reverse=reverse, directed=directed)
            response = stub.ClosenessCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_Periphery(self, stub, graph, usebounds=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.PeripheryRequest(graph=graph_in, usebounds=usebounds)
            response = stub.Periphery(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_degree_centrality(self, stub, graph, in_out=None, directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.DegreeCentralityRequest(graph=graph_in, in_out=in_out)
            response = stub.DegreeCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]


    def find_betweenness_centrality(self, stub, graph, k=None, normalized=True, weight=None, endpoints=False,
                                    seed=None, type='node', directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.BetweennessCentralityRequest(graph=graph_in, k=k, normalized=normalized,
                                                                            weight=weight, endpoints=endpoints,
                                                                            seed=seed, type=type,
                                                                            directed=directed)
            response = stub.BetweennessCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_pagerank(self, stub, graph, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None,
                      weight=False, dangling=None, directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.PageRankRequest(graph=graph_in, alpha=alpha,
                                                               personalization=personalization,
                                                               max_iter=max_iter, tol=tol, nstart=nstart,
                                                               weight=weight,
                                                               dangling=dangling, directed=directed)
            response = stub.PageRank(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_eigenvector_centrality(self, stub, graph, max_iter=100, tol=1e-06, nstart=None,
                                    weight=None, directed=False, in_out=True):

        try:

            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.EigenvectorCentralityRequest(graph=graph_in, max_iter=max_iter, tol=tol,
                                                                            nstart=nstart, weight=weight,
                                                                            directed=directed,in_out=in_out)
            response = stub.EigenvectorCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_hits(self, stub, graph, max_iter=100, tol=1e-08, nstart=None, normalized=True, directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.HitsRequest(graph=graph_in,max_iter=max_iter, tol=tol, nstart=nstart, normalized=normalized, directed=directed)

            response = stub.Hits(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def close_channel(self, channel):
        pass

# if __name__ == "__main__":
#     graph = {
#         "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
#         "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
#         "weights": [3, 4, 5, 6, 7, 8, 9, 10]
#     }
#     server = Server()
#     server.start_server()
#     client = ClientTest()
#     stub = client.open_grpc_channel()
#     client.find_degree_centrality(stub, graph)
#     client.find_closeness_centrality(stub, graph,nodes=['8','8'])
#     client.find_central(stub, graph)
#     client.find_betweenness_centrality(stub, graph)
#     client.find_pagerank(stub, graph)
#     client.find_eigenvector_centrality(stub, graph)
#     client.find_hits(stub, graph)
#     server.stop_server()
