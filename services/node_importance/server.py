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

		print(responce)
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


