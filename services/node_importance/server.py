import grpc
from concurrent import futures
import time

from service_spec import node_importance_pb2
from service_spec import node_importance_pb2_grpc

from node_importance import NodeImportance
# import graphs

import networkx as nx


class NodeImportanceServicer(node_importance_pb2_grpc.NodeImportanceServicer):
    def CentralNodes(self, request, context):
        ni = NodeImportance()
        graph = request.graph
        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_reponce = ni.find_central_nodes(graph_in)
        output_nodes_list = node_importance_pb2.OutputNodesList(output_nodes=temp_reponce[2]['central_nodes'])

        responce = node_importance_pb2.CentralNodeResponse(status=temp_reponce[0], message=temp_reponce[1],
                                                           output=output_nodes_list)
        return responce

    def Periphery(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_reponce = ni.find_Periphery(graph_in)

        print(temp_reponce)
        output_nodes_list = node_importance_pb2.OutputNodesList(output_nodes=temp_reponce[2]['periphery'])

        responce = node_importance_pb2.PeripheryResponse(status=temp_reponce[0], message=temp_reponce[1],
                                                         output=output_nodes_list)
        print("here",responce)
        return responce

    def ClosenessCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}

            nodes_list = []
            for nodes_ in request.nodes:
                if nodes_ not in ['[', ',', ']']:
                    nodes_list.append(nodes_)
        # print(nodes_list)
        except Exception as e:
            return [False, str(e), {}]

        responce = node_importance_pb2.ClosenessCentralityResponse()
        responce.status, responce.message, responce.Response = ni.find_closeness_centrality(graph_in, nodes_list)
        return responce

    def DegreeCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        responce = node_importance_pb2.DegreeCentralityResponse()
        responce.status, responce.message, responce.Response = ni.find_degree_centrality(graph_in)
        return responce

    def BetweennessCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        responce = node_importance_pb2.BetweennessCentralityResponse()
        responce.status, responce.message, responce.Response = ni.find_betweenness_centrality(graph_in)
        return responce

    def PageRank(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        responce = node_importance_pb2.PageRankResponse()
        responce.status, responce.message, responce.Response = ni.find_pagerank(graph_in)
        return responce

    def EigenvectorCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        responce = node_importance_pb2.EigenvectorCentralityResponse()
        responce.status, responce.message, responce.Response = ni.find_eigenvector_centrality(graph_in)
        return responce

    def HubMatrix(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        responce = node_importance_pb2.HubMatrixResponse()
        responce.status, responce.message, responce.Response = ni.find_hub_matrix(graph_in)
        return responce

    def AuthorityMatrix(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list}
        except Exception as e:
            return [False, str(e), {}]

        responce = node_importance_pb2.AuthorityMatrixResponse()
        responce.status, responce.message, responce.Response = ni.find_authority_matrix(graph_in)
        return responce


class Server():
    def __init__(self):
        self.port = '[::]:50051'
        self.server = None

    def start_server(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        node_importance_pb2_grpc.add_NodeImportanceServicer_to_server(NodeImportanceServicer(), self.server)
        print('Starting server. Listening on port 50051.')
        self.server.add_insecure_port(self.port)
        self.server.start()

    def stop_server(self):
        self.server.stop(0)
