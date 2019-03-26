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
    def test_min_nodes_to_remove(self):


        #

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4','5', '6'],
            "edges": [['1', '21'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['4', '6']]
        }
        source_node = '1'
        target_node = '6'

        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req)

        graph_1 = network_analytics_robustness_pb2.MinNodesToRemoveRequest(graph=graph_in,source_node=source_node,target_node=target_node)



        try:
            response = stub.MinNodesToRemove(graph_1)
        except Exception as e:
            response = str(e)

        self.assertIn('edge value at [0][1] is not a node',response)
        # print(response.status)
        # print(response.message)
        # print(response.nodes_output)
        # print(response.edges_output)
        # expected = network_analytics_robustness_pb2.MinNodesToRemoveResponse(status=False, message='edge value at [0][1] is not a node')
        # self.assertEqual(response, expected)



        #

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4','5', '6'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['4', '6']]
        }
        source_node = '1'
        target_node = '6'

        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req)

        graph_1 = network_analytics_robustness_pb2.MinNodesToRemoveRequest(graph=graph_in,source_node=source_node,target_node=target_node)

        response = stub.MinNodesToRemove(graph_1)
        print(response.status)
        print(response.message)
        print(response.nodes_output)
        print(response.edges_output)
        edges_resp = []
        for edge_ret in [['4', '6'], ['3', '6']]:
            edges_resp.append(network_analytics_robustness_pb2.Edge(edge=edge_ret))
        expected = network_analytics_robustness_pb2.MinNodesToRemoveResponse(status=True, message='success',nodes_output=['4','3'],edges_output=edges_resp)
        self.assertEqual(response.status,expected.status)
        self.assertEqual(response.message,expected.message)
        self.assertCountEqual(response.nodes_output,expected.nodes_output)
        self.assertCountEqual(response.edges_output,expected.edges_output)

    # Check MostImportantNodes
    def test_most_important_nodes_edges_subset(self):


        #

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']]

        }

        source_nodes = ['5', '17', '10']
        target_nodes = ['6']

        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        if ('weights' in graph):
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"], edges=edges_req,
                                                              weights=graph['weights'])
        else:
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"], edges=edges_req)

        graph_1 = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetRequest(graph=graph_in, source_nodes=source_nodes,target_nodes=target_nodes)


        try:
            response = stub.MostImportantNodesEdgesSubset(graph_1)
        except Exception as e:
            response = str(e)

        self.assertIn('source_nodes [1] does not exist in graph', response)


        # response = stub.MostImportantNodesEdgesSubset(graph_1)
        # print(response.status)
        # print(response.message)
        # print(response.node_betweenness_centrality)
        # print(response.edge_betweenness_centrality)
        # expected = None
        # expected = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=False, message='source_nodes [1] does not exist in graph')
        # self.assertEqual(response, expected)


        #

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']]

        }

        source_nodes = ['5', '7']
        target_nodes = ['6']

        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        if ('weights' in graph):
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"], edges=edges_req,
                                                              weights=graph['weights'])
        else:
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"], edges=edges_req)

        graph_1 = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetRequest(graph=graph_in, source_nodes=source_nodes,target_nodes=target_nodes)

        response = stub.MostImportantNodesEdgesSubset(graph_1)
        print(response.status)
        print(response.message)
        print(response.node_betweenness_centrality)
        print(response.edge_betweenness_centrality)
        expected = None
        graph_resp = network_analytics_robustness_pb2.node_betweenness(node=['2','3'], node_centrality_value=1.0)
        expected = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=True, message='success',node_betweenness_centrality=graph_resp)
        self.assertEqual(response, expected)
        # self.assertEqual(response.status, expected.status)
        # self.assertEqual(response.message, expected.message)
        # self.assertCountEqual(response.node_betweenness_centrality.node, expected.node_betweenness_centrality.node)
        # self.assertEqual(response.node_betweenness_centrality.node_centrality_value, expected.node_betweenness_centrality.node_centrality_value)

        #

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, 5, 6, 7, 8, 9, 10]
        }
        source_nodes = ['5', '7']
        target_nodes = ['6']


        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        if('weights' in graph):
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req, weights=graph['weights'])
        else:
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req)


        graph_1 = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=1)

        response = stub.MostImportantNodesEdgesSubset(graph_1)
        print(response.status)
        print(response.message)
        print(response.node_betweenness_centrality)
        print(response.edge_betweenness_centrality)
        expected = None
        edges_resp = []
        for edge_ret in [('2', '3'), ('3', '6')]:
            edges_resp.append(network_analytics_robustness_pb2.Edge(edge=list(edge_ret)))
        graph_resp = network_analytics_robustness_pb2.edge_betweenness(edge=edges_resp, edge_centrality_value=1.0)
        expected = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=True, message='success',edge_betweenness_centrality=graph_resp)
        self.assertEqual(response,expected)


        #

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8'], ['7', '9'], ['5', '9'], ['9', '10'], ['10', '6']]

        }

        source_nodes = ['5', '7']
        target_nodes = ['6']


        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        if('weights' in graph):
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req, weights=graph['weights'])
        else:
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req)


        graph_1 = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=1,directed=True)

        response = stub.MostImportantNodesEdgesSubset(graph_1)
        print(response.status)
        print(response.message)
        print(response.node_betweenness_centrality)
        print(response.edge_betweenness_centrality)
        expected = None
        edges_resp = []
        for edge_ret in [('9', '10'), ('10', '6')]:
            edges_resp.append(network_analytics_robustness_pb2.Edge(edge=list(edge_ret)))
        graph_resp = network_analytics_robustness_pb2.edge_betweenness(edge=edges_resp, edge_centrality_value=2.0)
        expected = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=True, message='success',edge_betweenness_centrality=graph_resp)
        self.assertEqual(response,expected)


        #

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8'], ['7', '9'], ['5', '9'], ['9', '10'], ['10', '6']],
            "weights": [1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        }

        source_nodes = ['5', '7']
        target_nodes = ['6']


        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

        if('weights' in graph):
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req, weights=graph['weights'])
        else:
            graph_in = network_analytics_robustness_pb2.Graph(nodes=graph["nodes"],edges=edges_req)


        graph_1 = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=1,directed=True,weight=True)

        response = stub.MostImportantNodesEdgesSubset(graph_1)
        print(response.status)
        print(response.message)
        print(response.node_betweenness_centrality)
        print(response.edge_betweenness_centrality)
        expected = None
        edges_resp = []
        for edge_ret in [('9', '10'), ('10', '6')]:
            edges_resp.append(network_analytics_robustness_pb2.Edge(edge=list(edge_ret)))
        graph_resp = network_analytics_robustness_pb2.edge_betweenness(edge=edges_resp, edge_centrality_value=2.0)
        expected = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=True, message='success',edge_betweenness_centrality=graph_resp)
        self.assertEqual(response,expected)


__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()
