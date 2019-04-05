import unittest
from node_importance import NodeImportance

import networkx as nx
import numpy as np
from client import ClientTest
from snet_grpc_wrapper_node_importance import *

from service_spec_node_importance import network_analytics_node_importance_pb2
from service_spec_node_importance import network_analytics_node_importance_pb2_grpc


class TestNodeImportance(unittest.TestCase):

    def setUp(self):
        self.server = Server()
        self.server.start_server()
        self.client = ClientTest()
        self.stub = self.client.open_grpc_channel()
        self.graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, 5, 6, 7, 8, 9, 10]
        }
        self.graph_no_weights = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']]
        }
        self.graph_01 = {
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, 5, 6, 7, 8, 9, 10]
        }
        self.graph_02 = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "weights": [3, 4, 5, 6, 7, 8, 9, 10]
        }
        self.graph_03 = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']]
        }
        self.graph_04 = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, 5, 6, 7]
        }
        self.graph_05 = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '25'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, 5, 6, 7, 8, 9, 10]
        }

    def test_find_central_nodes(self):

        center_req = network_analytics_node_importance_pb2.CentralNodeRequest(graph=self.client.get_graph(self.graph))
        resp = self.stub.CentralNodes(center_req)

        self.assertEqual(resp.status, True)
        self.assertEqual(resp.message, 'success')
        self.assertCountEqual(list(resp.output), ['2', '3'])

        center_req = network_analytics_node_importance_pb2.CentralNodeRequest(graph=self.client.get_graph(self.graph_05), usebounds=True)

        try:
            response = self.stub.CentralNodes(center_req)
        except Exception as e:
            response = str(e)

        self.assertIn('edge value at [3][1] is not a node', response)



    def test_find_Periphery(self):
        expected_result = ['1', '4', '5', '6', '7', '8']

        # Default Test
        request = network_analytics_node_importance_pb2.PeripheryRequest(graph=self.client.get_graph(self.graph))
        result = self.client.find_Periphery(self.stub, request)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(list(result.output), expected_result)

        # Non Deafault test
        request = network_analytics_node_importance_pb2.PeripheryRequest(graph=self.client.get_graph(self.graph), usebounds=True)
        result = self.client.find_Periphery(self.stub, request)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(list(result.output), expected_result)

        # Graph With No Nodes Test
        request = network_analytics_node_importance_pb2.PeripheryRequest(graph=self.client.get_graph(self.graph_01))
        result = self.client.find_Periphery(self.stub, request)
        self.assertIn('graph should at least contain two nodes',result[1])


        # Graph With No edges Test
        request = network_analytics_node_importance_pb2.PeripheryRequest(graph=self.client.get_graph(self.graph_02))
        result = self.client.find_Periphery(self.stub, request)
        self.assertIn('graph should at least contain one edge',result[1])

        # weight less graph test
        request = network_analytics_node_importance_pb2.PeripheryRequest(graph=self.client.get_graph(self.graph_03))
        result = self.client.find_Periphery(self.stub, request)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(list(result.output), expected_result)

        periphery_req = network_analytics_node_importance_pb2.PeripheryRequest(graph=self.client.get_graph(self.graph_05))

        try:
            response = self.stub.Periphery(periphery_req)
        except Exception as e:
            response = str(e)

        self.assertIn('edge value at [3][1] is not a node', response)

    def test_find_degree_centrality(self):

        # Default test
        request = network_analytics_node_importance_pb2.DegreeCentralityRequest(graph=self.client.get_graph(self.graph))
        result = self.client.find_degree_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.2857142857142857, '2': 0.5714285714285714, '3': 0.5714285714285714,
                                  '4': 0.2857142857142857, '5': 0.14285714285714285, '6': 0.14285714285714285,
                                  '7': 0.14285714285714285, '8': 0.14285714285714285}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.DegreeCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)

        # Non Default test
        request = network_analytics_node_importance_pb2.DegreeCentralityRequest(graph=self.client.get_graph(self.graph),in_out='in')
        result = self.client.find_degree_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.14285714285714285, '3': 0.14285714285714285,
                                    '4': 0.2857142857142857,
                                    '5': 0.14285714285714285, '6': 0.14285714285714285,
                                    '7': 0.14285714285714285,
                                    '8': 0.14285714285714285}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.DegreeCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)

        # # Graph With No Nodes Test
        request = network_analytics_node_importance_pb2.DegreeCentralityRequest(graph=self.client.get_graph(self.graph_01))
        result = self.client.find_degree_centrality(self.stub, request)
        self.assertIn('graph should at least contain two nodes', result[1])

    def test_find_closeness_centrality(self):

        # Deafault test

        request = network_analytics_node_importance_pb2.ClosenessCentralityRequest(graph=self.client.get_graph(self.graph))
        result = self.client.find_closeness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.5, '2': 0.7, '3': 0.7, '4': 0.5, '5': 0.4375, '6': 0.4375, '7': 0.4375, '8': 0.4375}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.ClosenessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)

        # Deafault test 2

        request = network_analytics_node_importance_pb2.ClosenessCentralityRequest(
            graph=self.client.get_graph(self.graph),wf_improved='wf_improved')
        result = self.client.find_closeness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.5, '2': 0.7, '3': 0.7, '4': 0.5, '5': 0.4375, '6': 0.4375, '7': 0.4375,
                     '8': 0.4375}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.ClosenessCentralityResponse(status=True, message='success',
                                                                                     output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)

        # Deafault test 3

        request = network_analytics_node_importance_pb2.ClosenessCentralityRequest(
            graph=self.client.get_graph(self.graph), wf_improved='')
        result = self.client.find_closeness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.5, '2': 0.7, '3': 0.7, '4': 0.5, '5': 0.4375, '6': 0.4375, '7': 0.4375,
                     '8': 0.4375}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.ClosenessCentralityResponse(status=True, message='success',
                                                                                     output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)



        # Non Deafault test

        request = network_analytics_node_importance_pb2.ClosenessCentralityRequest(graph=self.client.get_graph(self.graph),distance=True, wf_improved='not_wf_improved', reverse=True, directed=True)
        result = self.client.find_closeness_centrality(self.stub, request)

        dict_resp = []
        for n,v in {'1': 0.5, '2': 0.6666666666666666, '3': 1.0, '4': 0.0, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n,output=v))


        expected = network_analytics_node_importance_pb2.ClosenessCentralityResponse(status=True,message='success', output=dict_resp)

        self.assertEqual([result.status,result.message],[expected.status,expected.message])
        self.assertCountEqual(result.output, expected.output)

        # # Graph With No Nodes Test
        request = network_analytics_node_importance_pb2.ClosenessCentralityRequest(graph=self.client.get_graph(self.graph_01))
        result = self.client.find_closeness_centrality(self.stub, request)
        self.assertIn('graph should at least contain two nodes', result[1])

    def test_find_betweenness_centrality(self):

        # Default Test

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph))
        result = self.client.find_betweenness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.07142857142857142, '2': 0.5952380952380952,'3': 0.5952380952380952, '4': 0.07142857142857142,'5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success',
                                                                                       output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # Default Test 2

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph), normalized='n', type='node')
        result = self.client.find_betweenness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.07142857142857142, '2': 0.5952380952380952, '3': 0.5952380952380952,
                     '4': 0.07142857142857142, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success',
                                                                                       output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # non Default Test with weight for node betweeness

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph), k=1, normalized='u', weight=True, endpoints=True, seed=1, directed=True)
        result = self.client.find_betweenness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)


        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # non Default Test with weight for node betweeness and with type parameter specified

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph), k=1, normalized='u', weight=True, endpoints=True, seed=1, directed=True, type='node')
        result = self.client.find_betweenness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # non Default Test 2 with weight for node betweeness and with type parameter specified with ''

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(
            graph=self.client.get_graph(self.graph), k=1, normalized='u', weight=True, endpoints=True, seed=1,directed=True, type='')
        result = self.client.find_betweenness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success',
                                                                                       output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # non Default Test 2 with weight for node betweeness and without type parameter specified

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph), k=1, normalized='u', weight=True, endpoints=True, seed=1, directed=True)
        result = self.client.find_betweenness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success',
                                                                                       output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)


        # non Default Test without weight for node betweeness

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph),k=1, normalized='u', endpoints=True, seed=1, directed=True)
        result = self.client.find_betweenness_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)



        # non Default Test with weight for edge betweeness

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph),k=1, normalized='u',
                                                         seed=1, directed=True, type='edge', weight=True)
        result = self.client.find_betweenness_centrality(self.stub, request)


        dict_resp = []
        for e, v in {('1', '2'): 0.0, ('1', '4'): 0.0, ('2', '3'): 0.0, ('2', '5'): 0.0, ('2', '7'): 0.0, ('3', '4'): 1.0,
                                   ('3', '6'): 1.0, ('3', '8'): 1.0}.items():

            edges_resp = network_analytics_node_importance_pb2.Edge(edge=list(e))
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(edge=edges_resp, output=v))

        expected = network_analytics_node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # error raising test

        request = network_analytics_node_importance_pb2.BetweennessCentralityRequest(graph=self.client.get_graph(self.graph),k=15, normalized='u', weight=True, endpoints=True, seed=1, directed=True)
        result = self.client.find_betweenness_centrality(self.stub, request)


        self.assertIn('parameter k is larger than the number of nodes in the graph',result[1])


    def test_find_pagerank(self):
        # Default Test
        request = network_analytics_node_importance_pb2.PageRankRequest(graph=self.client.get_graph(self.graph))
        result = self.client.find_pagerank(self.stub, request)
        print(result)

        dict_resp = []
        for n, v in {'1': 0.12113884655309373, '2': 0.23955113566709454, '3': 0.23955113566709454,
                         '4': 0.12113884655309375, '5': 0.06965500888990583, '6': 0.06965500888990583,
                         '7': 0.06965500888990583, '8': 0.06965500888990583}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.PageRankResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # Non Default Test

        personalizatoin = []
        for k,vv in {'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                       '6': 0.125, '7': 0.125, '8': 0.125}.items():
            personalizatoin.append(network_analytics_node_importance_pb2.DictIn(node=k,value=vv))

        nstart = []
        for k, vv in {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1}.items():
            nstart.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))

        dangling = []
        for k, vv in {'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                '6': 0.125, '7': 0.125, '8': 0.125}.items():
            dangling.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))

        request = network_analytics_node_importance_pb2.PageRankRequest(graph=self.client.get_graph(self.graph),alpha=0.95,personalization=personalizatoin, max_iter=100,tol=1e-07,nstart=nstart,weight=True,dangling=dangling,directed=True)
        result = self.client.find_pagerank(self.stub, request)
        print(result)

        dict_resp = []
        for n, v in {'1': 0.08514279383409741, '2': 0.1255854995423924, '3': 0.12491155064890427, '4': 0.16514082203112918, '5': 0.12491155064890427, '6': 0.12469811632283417, '7': 0.12491155064890427, '8': 0.12469811632283417}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.PageRankResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # Error raising test

        personalizatoin = []
        for k, vv in {'1': 0.125, '2': 0.125, '31': 0.125, '4': 0.125, '5': 0.125,
                      '6': 0.125, '7': 0.125, '8': 0.125}.items():
            personalizatoin.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))



        request = network_analytics_node_importance_pb2.PageRankRequest(graph=self.client.get_graph(self.graph), personalization=personalizatoin)
        result = self.client.find_pagerank(self.stub, request)
        self.assertIn('personalization parameter contains a node at zero-indexed position 2 that does not exist in the graph', result[1])


    def test_find_eigenvector_centrality(self):

        # Default Test

        request = network_analytics_node_importance_pb2.EigenvectorCentralityRequest(graph=self.client.get_graph(self.graph))
        result = self.client.find_eigenvector_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 0.35775018836999806, '2': 0.5298994260311778,
                                                                '3': 0.5298994260311778, '4': 0.35775018836999806,
                                                                '5': 0.2135666184274351, '6': 0.2135666184274351,
                                                                '7': 0.2135666184274351, '8': 0.2135666184274351}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.EigenvectorCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)
        #
        # # Non Default Test

        nstart = []
        for k, vv in {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                                                            '8': 1}.items():
            nstart.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))

        request = network_analytics_node_importance_pb2.EigenvectorCentralityRequest(graph=self.client.get_graph(self.graph),max_iter=500, tol=1e-05,nstart=nstart, weight=True, directed=True,in_out='in')
        result = self.client.find_eigenvector_centrality(self.stub, request)


        dict_resp = []
        for n, v in {'1': 1.9935012399077745e-07, '2': 5.183103223760218e-05,
                                                                '3': 0.0067123180248934745, '4': 0.5773456687445266,
                                                                '5': 0.0067123180248934745, '6': 0.5772940370624132, '7': 0.0067123180248934745, '8': 0.5772940370624132}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.EigenvectorCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # # Non Default Test 2 when in_out=''

        nstart = []
        for k, vv in {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                      '8': 1}.items():
            nstart.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))

        request = network_analytics_node_importance_pb2.EigenvectorCentralityRequest(graph=self.client.get_graph(self.graph), max_iter=500, tol=1e-05, nstart=nstart, weight=True, directed=True)
        result = self.client.find_eigenvector_centrality(self.stub, request)

        dict_resp = []
        for n, v in {'1': 1.9935012399077745e-07, '2': 5.183103223760218e-05,
                     '3': 0.0067123180248934745, '4': 0.5773456687445266,
                     '5': 0.0067123180248934745, '6': 0.5772940370624132, '7': 0.0067123180248934745,
                     '8': 0.5772940370624132}.items():
            dict_resp.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.EigenvectorCentralityResponse(status=True, message='success',
                                                                                       output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)


        #
        # # Error raising test

        nstart = []
        for k, vv in {'1': 0.125, '2': 0.125, '31': 0.125, '4': 0.125, '5': 0.125,
                      '6': 0.125, '7': 0.125, '8': 0.125}.items():
            nstart.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))

        request = network_analytics_node_importance_pb2.EigenvectorCentralityRequest(graph=self.client.get_graph(self.graph), nstart=nstart)
        result = self.client.find_eigenvector_centrality(self.stub, request)

        self.assertIn('nstart parameter contains a node at zero-indexed position 2 that does not exist in the graph',result[1])
        

    def test_find_hits(self):

        # Default Test
        request = network_analytics_node_importance_pb2.HitsRequest(graph=self.client.get_graph(self.graph_no_weights))
        result = self.client.find_hits(self.stub, request)

        dict_resp_hubs = []
        for n, v in {'1': 0.13604957690850644, '2': 0.2015158583139189, '3': 0.2015158583139189, '4': 0.13604957690850644, '5': 0.08121728238878734, '6': 0.08121728238878734, '7': 0.08121728238878734, '8': 0.08121728238878734}.items():
            dict_resp_hubs.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        dict_resp_authorities = []
        for n, v in {'1': 0.13604957688814256, '2': 0.2015158585243154, '3': 0.2015158585243154, '4': 0.13604957688814256, '5': 0.08121728229377104, '6': 0.08121728229377104, '7': 0.08121728229377104, '8': 0.08121728229377104}.items():
            dict_resp_authorities.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.HitsResponse(status=True, message='success', hubs=dict_resp_hubs, authorities=dict_resp_authorities)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.hubs, expected.hubs)
        self.assertCountEqual(result.authorities, expected.authorities)

        # Default Test 2
        request = network_analytics_node_importance_pb2.HitsRequest(graph=self.client.get_graph(self.graph_no_weights), normalized='n')
        result = self.client.find_hits(self.stub, request)

        dict_resp_hubs = []
        for n, v in {'1': 0.13604957690850644, '2': 0.2015158583139189, '3': 0.2015158583139189,
                     '4': 0.13604957690850644, '5': 0.08121728238878734, '6': 0.08121728238878734,
                     '7': 0.08121728238878734, '8': 0.08121728238878734}.items():
            dict_resp_hubs.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        dict_resp_authorities = []
        for n, v in {'1': 0.13604957688814256, '2': 0.2015158585243154, '3': 0.2015158585243154,
                     '4': 0.13604957688814256, '5': 0.08121728229377104, '6': 0.08121728229377104,
                     '7': 0.08121728229377104, '8': 0.08121728229377104}.items():
            dict_resp_authorities.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.HitsResponse(status=True, message='success',
                                                                      hubs=dict_resp_hubs,
                                                                      authorities=dict_resp_authorities)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.hubs, expected.hubs)
        self.assertCountEqual(result.authorities, expected.authorities)

        # Default Test 3
        request = network_analytics_node_importance_pb2.HitsRequest(graph=self.client.get_graph(self.graph_no_weights), normalized='')
        result = self.client.find_hits(self.stub, request)

        dict_resp_hubs = []
        for n, v in {'1': 0.13604957690850644, '2': 0.2015158583139189, '3': 0.2015158583139189,
                     '4': 0.13604957690850644, '5': 0.08121728238878734, '6': 0.08121728238878734,
                     '7': 0.08121728238878734, '8': 0.08121728238878734}.items():
            dict_resp_hubs.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        dict_resp_authorities = []
        for n, v in {'1': 0.13604957688814256, '2': 0.2015158585243154, '3': 0.2015158585243154,
                     '4': 0.13604957688814256, '5': 0.08121728229377104, '6': 0.08121728229377104,
                     '7': 0.08121728229377104, '8': 0.08121728229377104}.items():
            dict_resp_authorities.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.HitsResponse(status=True, message='success',
                                                                      hubs=dict_resp_hubs,
                                                                      authorities=dict_resp_authorities)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.hubs, expected.hubs)
        self.assertCountEqual(result.authorities, expected.authorities)

        # # Non Default Test

        nstart = []
        for k, vv in {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1}.items():
            nstart.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))

        request = network_analytics_node_importance_pb2.HitsRequest(graph=self.client.get_graph(self.graph_no_weights),max_iter=110,tol=11.0e-7,nstart=nstart,normalized='u',directed=True)
        result = self.client.find_hits(self.stub, request)

        dict_resp_hubs = []
        for n, v in {'1': 0.6180339887498948, '2': 5.309100041157175e-06, '3': 1.0, '4': 0.0, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}.items():
            dict_resp_hubs.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        dict_resp_authorities = []
        for n, v in {'1': 0.0, '2': 0.38196601125010515, '3': 3.957169530458124e-06, '4': 1.0, '5': 3.957169530458124e-06, '6': 0.6180339887498948, '7': 3.957169530458124e-06, '8': 0.6180339887498948}.items():
            dict_resp_authorities.append(network_analytics_node_importance_pb2.DictOutput(node=n, output=v))

        expected = network_analytics_node_importance_pb2.HitsResponse(status=True, message='success', hubs=dict_resp_hubs,
                                                    authorities=dict_resp_authorities)

        print(result.hubs)
        print(expected.hubs)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.hubs, expected.hubs)
        self.assertCountEqual(result.authorities, expected.authorities)

        # # Error raising test

        nstart = []
        for k, vv in {'1': 0.125, '2': 0.125, '31': 0.125, '4': 0.125, '5': 0.125,
                      '6': 0.125, '7': 0.125, '8': 0.125}.items():
            nstart.append(network_analytics_node_importance_pb2.DictIn(node=k, value=vv))

        request = network_analytics_node_importance_pb2.HitsRequest(graph=self.client.get_graph(self.graph), nstart=nstart)
        result = self.client.find_hits(self.stub, request)

        self.assertIn('nstart parameter contains a node at zero-indexed position 2 that does not exist in the graph',result[1])



    def tearDown(self):
        self.server.stop_server()


if __name__ == '__main__':
    unittest.main()
