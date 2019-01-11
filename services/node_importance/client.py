import os
import grpc
import node_importance_pb2
import node_importance_pb2_grpc


class ClientTest():
	def __init__(self,port='localhost:50051',image_output='client_out'):
		self.port = port
		


	def open_grpc_channel(self):
		channel = grpc.insecure_channel(self.port)
		stub = node_importance_pb2_grpc.NodeImportanceStub(channel)
		return stub
		

	def find_central(self,stub,graph=None):
		edges_req = []
		for e in graph["edges"]:
			edges_req.append(node_importance_pb2.Edge(edge=e))

		graph_in = node_importance_pb2.Graph(nodes=graph["nodes"],edges=edges_req,weights=graph['weights'])
		input_graph = node_importance_pb2.CentralNodeInput(graph = graph_in)
		responce = stub.CentralNodes(input_graph)
		print(responce.status,responce.messgae,responce.output)
		return responce

		
	def close_channel(self,channel):
		pass

if __name__ == "__main__":
	graph = {
        "nodes": ['1','2','3','4','5','6','7','8'],
        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
        "weights": [3,4,5,6,7,8,9,10]
    }
	client = ClientTest()
	stub = client.open_grpc_channel()
	client.find_central(stub,graph)