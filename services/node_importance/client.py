import os
import grpc
from service_spec_node_importance import network_analytics_node_importance_pb2
from service_spec_node_importance import network_analytics_node_importance_pb2_grpc

from snet_grpc_wrapper_node_importance import *


class ClientTest():
    def __init__(self, port='localhost:5001'):
        self.port = port

    def open_grpc_channel(self):
        channel = grpc.insecure_channel(self.port)
        stub = network_analytics_node_importance_pb2_grpc.NetworkAnalyticsNodeImportanceStub(channel)
        return stub

    def get_graph(self, graph):

        try_weight = False
        try_edge = False

        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(network_analytics_node_importance_pb2.Edge(edge=e))
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
                graph_in = network_analytics_node_importance_pb2.Graph(nodes=graph["nodes"])
            elif not try_weight and try_edge:
                graph_in = network_analytics_node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req)
            elif try_weight and not try_edge:
                graph_in = network_analytics_node_importance_pb2.Graph(nodes=graph["nodes"], weights=weights_req)
            else:
                graph_in = network_analytics_node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=weights_req)

        except:

            if not try_weight and not try_edge:
                graph_in = network_analytics_node_importance_pb2.Graph()
            elif not try_weight and try_edge:
                graph_in = network_analytics_node_importance_pb2.Graph(edges=edges_req)
            elif try_weight and not try_edge:
                graph_in = network_analytics_node_importance_pb2.Graph(weights=weights_req)
            else:
                graph_in = network_analytics_node_importance_pb2.Graph(edges=edges_req, weights=weights_req)

        return graph_in

    def find_closeness_centrality(self, stub, Request_data):
        try:
            response = stub.ClosenessCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]


    def find_Periphery(self, stub, Request_data):
        try:
            response = stub.Periphery(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_degree_centrality(self, stub, Request_data):
        try:
            response = stub.DegreeCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]


    def find_betweenness_centrality(self, stub, Request_data):
        try:

            response = stub.BetweennessCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_pagerank(self, stub, Request_data):
        try:
            response = stub.PageRank(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_eigenvector_centrality(self, stub, Request_data):

        try:
            response = stub.EigenvectorCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_hits(self, stub, Request_data):
        try:
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
