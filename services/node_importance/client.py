import os
import grpc
from service_spec import node_importance_pb2
from service_spec import node_importance_pb2_grpc


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
            responce = stub.CentralNodes(Request_graph)
            return responce
        except Exception as e:
            return [False, str(e), {}]

    def find_eccentricity(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.EccentricityRequest(graph=graph_in, directed=False)
            responce = stub.Eccentricity(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
        except Exception as e:
            return [False, str(e), {}]

    def find_degree_centrality(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.DegreeCentralityRequest(graph=graph_in, directed=False)
            responce = stub.DegreeCentrality(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
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
            Request_graph = node_importance_pb2.ClosenessCentralityRequest(graph=graph_in, nodes="[1,2]",
                                                                             directed=False)
            responce = stub.ClosenessCentrality(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
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
            responce = stub.BetweennessCentrality(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
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
            responce = stub.PageRank(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
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
            responce = stub.EigenvectorCentrality(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
        except Exception as e:
            return [False, str(e), {}]

    def find_hub_matrix(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.HubMatrixRequest(graph=graph_in, directed=False)
            responce = stub.HubMatrix(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
        except Exception as e:
            return [False, str(e), {}]

    def find_authority_matrix(self, stub, graph):
        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=graph['weights'])
            Request_graph = node_importance_pb2.AuthorityMatrixRequest(graph=graph_in, directed=False)
            responce = stub.AuthorityMatrix(Request_graph)
            # print(responce.status,responce.message,responce.output)
            return responce
        except Exception as e:
            return [False, str(e), {}]

    def close_channel(self, channel):
        pass

# if __name__ == "__main__":
# 	graph = {
#         "nodes": ['1','2','3','4','5','6','7','8'],
#         "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
#         "weights": [3,4,5,6,7,8,9,10]
#     }
# 	client = ClientTest()
# 	stub = client.open_grpc_channel()
# 	client.find_closeness_centrality(stub,graph)
# 	client.find_central(stub,graph)
# 	client.find_eccentricity(stub,graph)
# 	client.find_degree_centrality(stub,graph)
# 	client.find_betweenness_centrality(stub,graph)
# 	client.find_pagerank(stub,graph)
# 	client.find_eigenvector_centrality(stub,graph)
# 	client.find_hub_matrix(stub,graph)
# 	client.find_authority_matrix(stub,graph)
