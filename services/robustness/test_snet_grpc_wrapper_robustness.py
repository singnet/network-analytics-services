# Tested on python3.6

import unittest

import grpc


from service_spec_robustness import network_analytics_robustness_pb2
from service_spec_robustness import network_analytics_robustness_pb2_grpc

import snet_grpc_wrapper_robustness



class TestSnetWrapperRobustness(unittest.TestCase):


    def setUp(self):

        self.server = snet_grpc_wrapper_robustness.serve_test()
        self.server.start()


    def tearDown(self):
        self.server.stop(0)
        print('Server stopped')

    # Check MinNodesToRemove
    def test_min_node_graph(self):
        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetowrkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1','2','3','4','5','6'],
            "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['4','6']]
            }
        source_node = '1'
        target_node = '6'

        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req)

        graph_1 = network_analytics_robustness_pb2.MinNodeGraphRequest(graph=graph_in,source_node=source_node,target_node=target_node)

        response = stub.MinNodeGraph(graph_1)
        print(response.status)
        print(response.message)
        print(response.nodes_output)
        print(response.edges_output)

    # Check MostImportantNodes
    def test_most_import_graph(self):
        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetowrkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1','2','3','4','5','6','7','8'],
            "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
            "weights": [3,4,5,6,7,8,9,10]
        }
        source_nodes = ['5','7']
        target_nodes = ['6']


        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        if('weights' in graph):
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req, weights=graph['weights'])
        else:
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req)


        graph_1 = network_analytics_robustness_pb2.MostImportantGraphRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=1)

        response = stub.MostImportantGraph(graph_1)
        print(response.status)
        print(response.message)
        print(response.node_betweenness_centrality)
        print(response.edge_betweenness_centrality)




__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()
