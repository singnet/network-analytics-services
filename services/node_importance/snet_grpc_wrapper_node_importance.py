import grpc
from concurrent import futures
import time

from service_spec_node_importance import node_importance_pb2
from service_spec_node_importance import node_importance_pb2_grpc

from node_importance import NodeImportance


class NodeImportanceServicer(node_importance_pb2_grpc.NodeImportanceServicer):
    def CentralNodes(self, request, context):
        ni = NodeImportance()
        graph = request.graph
        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_response = ni.find_central_nodes(graph=graph_in, u=request.u, distance=request.distance,
                                              wf_improved=request.wf_improved, reverse=request.reverse)
        centalnodes_output_key = []
        centralnodes_output_value = []
        if temp_response[0]:
            if isinstance(temp_response[2]["central_nodes"], dict):
                for k, v in temp_response[2]["central_nodes"].items():
                    centalnodes_output_key.append(k)
                    centralnodes_output_value.append(v)
            else:
                centalnodes_output_key.append(request.u)
                centralnodes_output_value.append(temp_response[2]["central_nodes"])

        output = node_importance_pb2.DictOutput(edge=centalnodes_output_key,
                                                output=centralnodes_output_value)
        responce = node_importance_pb2.CentralNodeResponse(status=temp_response[0], message=temp_response[1],
                                                           output=output)
        return responce

    def Periphery(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]
        temp_reponse = ni.find_Periphery(graph=graph_in, usebounds=request.usebounds)
        output_nodes_list = node_importance_pb2.OutputNodesList(output_nodes=temp_reponse[2]['periphery'])
        responce = node_importance_pb2.PeripheryResponse(status=temp_reponse[0], message=temp_reponse[1],
                                                         output=output_nodes_list)
        return responce

    def ClosenessCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))

            nodes_list = []
            for nodes_ in request.nodes:
                if nodes_ not in ['[', ',', ']']:
                    nodes_list.append(nodes_)
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_response = ni.find_closeness_centrality(graph=graph_in, nodes=nodes_list)
        closeness_output_edges = []
        closeness_output_value = []
        if temp_response[0]:
            for k, v in temp_response[2]["closeness_centrality"].items():
                closeness_output_edges.append(k)
                closeness_output_value.append(v)

        output = node_importance_pb2.DictOutput(edge=closeness_output_edges,
                                                output=closeness_output_value)
        response = node_importance_pb2.ClosenessCentralityResponse(status=temp_response[0], message=temp_response[1],
                                                                   output=output)
        return response

    def DegreeCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_response = ni.find_degree_centrality(graph_in, request.in_out)
        centrality_output_edges = []
        centrality_output_value = []
        if temp_response[0]:
            for k, v in temp_response[2][str(request.in_out) + "degree_centrality"].items():
                centrality_output_edges.append(k)
                centrality_output_value.append(v)

        output = node_importance_pb2.DictOutput(edge=centrality_output_edges,
                                                output=centrality_output_value)
        response = node_importance_pb2.DegreeCentralityResponse(status=temp_response[0], message=temp_response[1],
                                                                output=output)
        return response

    def BetweennessCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]
        temp_response = ni.find_betweenness_centrality(graph_in, k=request.k, normalized=request.normalized,
                                                       weight=request.weight, endpoints=request.endpoints,
                                                       type=request.type, seed=request.seed)

        betweenness_output_edges = []
        betweenness_output_value = []
        if temp_response[0]:
            if request.type == 'edge':
                for k, v in temp_response[2]["betweenness_centrality"].items():
                    betweenness_output_edges.append(node_importance_pb2.Edge(edge=[k[0], k[1]]))
                    betweenness_output_value.append(v)
            else:
                for k, v in temp_response[2]["betweenness_centrality"].items():
                    betweenness_output_edges.append(node_importance_pb2.Edge(edge=k))
                    betweenness_output_value.append(v)
                
        output = node_importance_pb2.BetweennessOutput(edge=betweenness_output_edges,
                                                       output=betweenness_output_value)
        response = node_importance_pb2.BetweennessCentralityResponse(status=temp_response[0], message=temp_response[1],
                                                                     output=output)
        return response

    def PageRank(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_response = ni.find_pagerank(graph_in, request.alpha, request.personalization, request.max_iter,
                                         request.tol, request.nstart, request.weight, request.dangling)
        pagerank_output_edges = []
        pagerank_output_value = []
        if temp_response[0]:
            for k, v in temp_response[2]["pagerank"].items():
                pagerank_output_edges.append(k)
                pagerank_output_value.append(v)

        output = node_importance_pb2.DictOutput(edge=pagerank_output_edges,
                                                output=pagerank_output_value)
        response = node_importance_pb2.PageRankResponse(status=temp_response[0], message=temp_response[1],
                                                        output=output)
        return response

    def EigenvectorCentrality(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_response = ni.find_eigenvector_centrality(graph_in, request.max_iter, request.tol, request.nstart,
                                                       request.weight)
        eigenvector_output_edges = []
        eigenvector_output_value = []
        if temp_response[0]:
            for k, v in temp_response[2]["eigenvector_centrality"].items():
                eigenvector_output_edges.append(k)
                eigenvector_output_value.append(v)

        output = node_importance_pb2.DictOutput(edge=eigenvector_output_edges,
                                                output=eigenvector_output_value)

        response = node_importance_pb2.EigenvectorCentralityResponse(status=temp_response[0], message=temp_response[1],
                                                                     output=output)

        return response

    def Hits(self, request, context):
        ni = NodeImportance()
        graph = request.graph

        try:
            edges_list = []
            weights_list = []
            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            if len(graph.weights) > 0:
                for weights_proto in graph.weights:
                    weights_list.append(int(weights_proto))
            graph_in = {"nodes": list(graph.nodes), "edges": edges_list, "weights": weights_list}
        except Exception as e:
            return [False, str(e), {}]

        temp_response = ni.find_hits(graph_in, request.nodelist, request.mode)
        hits_list = []
        if temp_response[0]:
            for i in temp_response[2][request.mode]:
                hits_list.append(node_importance_pb2.HitsOutput(hits_out=list(i)))

        response = node_importance_pb2.HitsResponse(status=temp_response[0], message=temp_response[1],
                                                    output=hits_list)

        return response


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
