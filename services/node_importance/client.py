import os
import grpc
from service_spec import node_importance_pb2
from service_spec import node_importance_pb2_grpc

from server import *


class ClientTest():
    def __init__(self, port='localhost:50051', image_output='client_out'):
        self.port = port

    def open_grpc_channel(self):
        channel = grpc.insecure_channel(self.port)
        stub = node_importance_pb2_grpc.NodeImportanceStub(channel)
        return stub

    def find_central(self, stub, graph):
        edges_req = []

        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.CentralNodeRequest(graph=graph_in, directed=False)
            response = stub.CentralNodes(Request_graph)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_Periphery(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:

            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.PeripheryRequest(graph=graph_in, directed=False)
            response = stub.Periphery(Request_graph)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_degree_centrality(self, stub, graph, in_out=None):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.DegreeCentralityRequest(graph=graph_in, in_out=in_out, directed=False)
            response = stub.DegreeCentrality(Request_graph)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_closeness_centrality(self, stub, graph, nodes):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.ClosenessCentralityRequest(graph=graph_in, nodes=nodes,
                                                                           directed=False)
            response = stub.ClosenessCentrality(Request_graph)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_betweenness_centrality(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.BetweennessCentralityRequest(graph=graph_in, directed=False)
            response = stub.BetweennessCentrality(Request_graph)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_pagerank(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.PageRankRequest(graph=graph_in, directed=False)
            response = stub.PageRank(Request_graph)
            # print(response.status,response.message,response.output)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_eigenvector_centrality(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.EigenvectorCentralityRequest(graph=graph_in, directed=False)
            response = stub.EigenvectorCentrality(Request_graph)
            # print(response.status,response.message,response.output)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_hits(self, stub, graph,nodelist=None,mode='hub_matrix'):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            # node_list = node_importance_pb2.
            Request_graph = node_importance_pb2.HitsRequest(graph=graph_in,nodelist=nodelist,mode=mode,directed=False)
            response = stub.Hits(Request_graph)
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
#     server.stop_server()
# 	  client.find_closeness_centrality(stub,graph)
# 	  client.find_central(stub,graph)
# 	  client.find_eccentricity(stub,graph)
# 	  client.find_degree_centrality(stub,graph)
# 	  client.find_betweenness_centrality(stub,graph)
# 	  client.find_pagerank(stub,graph)
# 	client.find_eigenvector_centrality(stub,graph)
# 	client.find_hub_matrix(stub,graph)
# 	client.find_authority_matrix(stub,graph)
