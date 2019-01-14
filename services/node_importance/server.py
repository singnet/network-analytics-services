import grpc
from concurrent import futures
import time

import node_importance_pb2
import node_importance_pb2_grpc

from node_importance import NodeImportance
# import graphs

import networkx as nx


class NodeImportanceServicer(node_importance_pb2_grpc.NodeImportanceServicer):
	def CentralNodes(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.CentralNodeOutput()
		responce.status,responce.messgae,responce.output = ni.find_central_nodes(graph_in)
		return responce

	def Eccentricity(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.EccentricityOutput()
		responce.status,responce.messgae,responce.output = ni.find_eccentricity(graph_in)
		return responce

	def ClosenessCentrality(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}

			nodes_list = []
			for nodes_ in request.nodes:
				if nodes_ not in ['[',',',']']:
					nodes_list.append(nodes_)
			# print(nodes_list)
		except Exception as e:
                    return ["False", str(e),{}]
        


		responce = node_importance_pb2.ClosenessCentralityOutput()
		responce.status,responce.messgae,responce.output = ni.find_closeness_centrality(graph_in,nodes_list)
		return responce


	def DegreeCentrality(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.DegreeCentralityOutput()
		responce.status,responce.messgae,responce.output = ni.find_degree_centrality(graph_in)
		return responce
	def BetweennessCentrality(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.BetweennessCentralityOutput()
		responce.status,responce.messgae,responce.output = ni.find_betweenness_centrality(graph_in)
		return responce

	def PageRank(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.PageRankOutput()
		responce.status,responce.messgae,responce.output = ni.find_pagerank(graph_in)
		return responce

	def EigenvectorCentrality(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.EigenvectorCentralityOutput()
		responce.status,responce.messgae,responce.output = ni.find_eigenvector_centrality(graph_in)
		return responce

	def HubMatrix(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.HubMatrixOutput()
		responce.status,responce.messgae,responce.output = ni.find_hub_matrix(graph_in)
		return responce

	def AuthorityMatrix(self,request,context):
		ni = NodeImportance()
		graph = request.graph

		try:
			edges_list = []
			for edges_proto in graph.edges:
				edges_list.append(list(edges_proto.edge))
			graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
		except Exception as e:
                    return ["False", str(e),{}]


		responce = node_importance_pb2.AuthorityMatrixOutput()
		responce.status,responce.messgae,responce.output = ni.find_authority_matrix(graph_in)
		return responce


class Server():
	def __init__(self):
		self.port = '[::]:50051'
		self.server = None
	def start_server(self):
		self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
		node_importance_pb2_grpc.add_NodeImportanceServicer_to_server(NodeImportanceServicer(),self.server)
		print('Starting server. Listening on port 50051.')
		self.server.add_insecure_port(self.port)
		self.server.start()

	
		
	def stop_server(self):
		self.server.stop(0)


