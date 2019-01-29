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

    def get_graph(self, graph):

        edges_req = []
        try:
            for e in graph["edges"]:
                edges_req.append(node_importance_pb2.Edge(edge=e))
        except Exception as e:
            return [False, str(e), {}]

        try:
            weights_req = graph['weights']
        except Exception as e:
            weights_req = None

        graph_in = node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req, weights=weights_req)
        return graph_in

    def find_central(self, stub, graph, usebounds=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.CentralNodeRequest(graph=graph_in, usebounds=usebounds)
            response = stub.CentralNodes(Request_data)
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
            Request_data = node_importance_pb2.DegreeCentralityRequest(graph=graph_in, in_out=in_out,
                                                                       directed=directed)
            response = stub.DegreeCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_closeness_centrality(self, stub, graph, nodes, directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.ClosenessCentralityRequest(graph=graph_in, nodes=nodes,
                                                                          directed=directed)
            response = stub.ClosenessCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_betweenness_centrality(self, stub, graph, k=None, normalized=True, weight=None, endpoints=False,
                                    seed=None, directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.BetweennessCentralityRequest(graph=graph_in, k=k, normalized=normalized,
                                                                            weight=weight, endpoints=endpoints,
                                                                            seed=seed,
                                                                            directed=directed)
            response = stub.BetweennessCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_pagerank(self, stub, graph, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None,
                      weight='weight', dangling=None, directed=False):
        nstart_key_list = []
        nstart_value_list = []
        nstart_new = None
        personalization_key_list = []
        personalization_value_list = []
        personalization_new = None
        dangling_key_list = []
        dangling_value_list = []
        dangling_new = None
        try:
            if personalization is not None:
                for k, v in personalization.items():
                    personalization_key_list.append(k)
                    personalization_value_list.append(v)
                personalization_new = node_importance_pb2.Personalization(key=personalization_key_list,
                                                                          value=personalization_value_list)
            if dangling is not None:
                for k, v in dangling.items():
                    dangling_key_list.append(k)
                    dangling_value_list.append(v)
                dangling_new = node_importance_pb2.Dangling(key=dangling_key_list, value=dangling_value_list)

            if nstart is not None:
                for k, v in nstart.items():
                    nstart_key_list.append(k)
                    nstart_value_list.append(v)
                nstart_new = node_importance_pb2.Nstart(key=nstart_key_list, value=nstart_value_list)
        except Exception as e:
            return [False, str(e), {}]

        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.PageRankRequest(graph=graph_in, alpha=alpha,
                                                               personalization=personalization_new,
                                                               max_iter=max_iter, tol=tol, nstart=nstart_new,
                                                               weight=weight,
                                                               dangling=dangling_new, directed=directed)
            response = stub.PageRank(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_eigenvector_centrality(self, stub, graph, max_iter=100, tol=1e-06, nstart=None,
                                    weight=None, directed=False):

        nstart_key_list = []
        nstart_value_list = []
        nstart_new = None
        try:
            if nstart is not None:
                for k, v in nstart.items():
                    nstart_key_list.append(k)
                    nstart_value_list.append(v)
                nstart_new = node_importance_pb2.Nstart(key=nstart_key_list, value=nstart_value_list)
        except Exception as e:
            return [False, str(e), {}]

        try:

            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.EigenvectorCentralityRequest(graph=graph_in, max_iter=max_iter, tol=tol,
                                                                            nstart=nstart_new, weight=weight,
                                                                            directed=directed)
            response = stub.EigenvectorCentrality(Request_data)
            return response
        except Exception as e:
            return [False, str(e), {}]

    def find_hits(self, stub, graph, nodelist=None, mode='hub_matrix', directed=False):
        try:
            graph_in = self.get_graph(graph=graph)
            Request_data = node_importance_pb2.HitsRequest(graph=graph_in, nodelist=nodelist, mode=mode,
                                                           directed=False)
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
