import unittest
from node_importance import NodeImportance

import networkx as nx
import numpy as np
from client import ClientTest
from snet_grpc_wrapper_node_importance import *

from service_spec_node_importance import node_importance_pb2
from service_spec_node_importance import node_importance_pb2_grpc


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

        center_req = node_importance_pb2.CentralNodeRequest(graph=self.client.get_graph(self.graph))
        resp = self.stub.CentralNodes(center_req)

        self.assertEqual(resp.status, True)
        self.assertEqual(resp.message, 'success')
        self.assertCountEqual(list(resp.output), ['2', '3'])

        center_req = node_importance_pb2.CentralNodeRequest(graph=self.client.get_graph(self.graph_05), usebounds=True)

        try:
            response = self.stub.CentralNodes(center_req)
        except Exception as e:
            response = str(e)

        self.assertIn('edge value at [3][1] is not a node', response)



    def test_find_Periphery(self):
        expected_result = ['1', '4', '5', '6', '7', '8']

        # Default Test
        result = self.client.find_Periphery(self.stub, self.graph)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(list(result.output), expected_result)

        # Non Deafault test
        result = self.client.find_Periphery(self.stub, self.graph, usebounds=True)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(list(result.output), expected_result)

        # Graph With No Nodes Test
        result = self.client.find_Periphery(self.stub, self.graph_01)
        self.assertIn('graph should at least contain two nodes',result[1])


        # Graph With No edges Test
        result = self.client.find_Periphery(self.stub, self.graph_02)
        self.assertIn('graph should at least contain one edge',result[1])

        # weight less graph test
        result = self.client.find_Periphery(self.stub, self.graph_03)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(list(result.output), expected_result)

        periphery_req = node_importance_pb2.PeripheryRequest(graph=self.client.get_graph(self.graph_05))

        try:
            response = self.stub.Periphery(periphery_req)
        except Exception as e:
            response = str(e)

        self.assertIn('edge value at [3][1] is not a node', response)

    def test_find_degree_centrality(self):

        # Default test
        result = self.client.find_degree_centrality(self.stub, self.graph)

        dict_resp = []
        for n, v in {'1': 0.2857142857142857, '2': 0.5714285714285714, '3': 0.5714285714285714,
                                  '4': 0.2857142857142857, '5': 0.14285714285714285, '6': 0.14285714285714285,
                                  '7': 0.14285714285714285, '8': 0.14285714285714285}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.DegreeCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)

        # Non Default test
        result = self.client.find_degree_centrality(self.stub, self.graph,'in')

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.14285714285714285, '3': 0.14285714285714285,
                                    '4': 0.2857142857142857,
                                    '5': 0.14285714285714285, '6': 0.14285714285714285,
                                    '7': 0.14285714285714285,
                                    '8': 0.14285714285714285}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.DegreeCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)

        # # Graph With No Nodes Test
        result = self.client.find_degree_centrality(self.stub, self.graph_01)
        self.assertIn('graph should at least contain two nodes', result[1])

    def test_find_closeness_centrality(self):

        # Deafault test
        result = self.client.find_closeness_centrality(self.stub, self.graph)

        dict_resp = []
        for n, v in {'1': 0.5, '2': 0.7, '3': 0.7, '4': 0.5, '5': 0.4375, '6': 0.4375, '7': 0.4375, '8': 0.4375}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.ClosenessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual([result.status, result.message], [expected.status, expected.message])
        self.assertCountEqual(result.output, expected.output)

        # Non Deafault test
        result = self.client.find_closeness_centrality(self.stub, self.graph, distance=True, wf_improved=False, reverse=True, directed=True)

        dict_resp = []
        for n,v in {'1': 0.5, '2': 0.6666666666666666, '3': 1.0, '4': 0.0, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n,output=v))


        expected = node_importance_pb2.ClosenessCentralityResponse(status=True,message='success', output=dict_resp)

        self.assertEqual([result.status,result.message],[expected.status,expected.message])
        self.assertCountEqual(result.output, expected.output)

        # # Graph With No Nodes Test
        result = self.client.find_closeness_centrality(self.stub, self.graph_01)
        self.assertIn('graph should at least contain two nodes', result[1])

    def test_find_betweenness_centrality(self):
        # non Default Test with weight for node betweeness

        result = self.client.find_betweenness_centrality(self.stub, self.graph, k=1, normalized=False, weight=True,
                                                         endpoints=True, seed=1, directed=True)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)


        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # non Default Test with weight for node betweeness and with type parameter specified

        result = self.client.find_betweenness_centrality(self.stub, self.graph, k=1, normalized=False, weight=True,
                                                         endpoints=True, seed=1, directed=True, type='node')

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # non Default Test without weight for node betweeness

        result = self.client.find_betweenness_centrality(self.stub, self.graph, k=1, normalized=False,
                                                         endpoints=True, seed=1, directed=True)

        dict_resp = []
        for n, v in {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)



        # non Default Test with weight for edge betweeness

        result = self.client.find_betweenness_centrality(self.stub, self.graph, k=1, normalized=False,
                                                         seed=1, directed=True, type='edge', weight=True)

        dict_resp = []
        for e, v in {('1', '2'): 0.0, ('1', '4'): 0.0, ('2', '3'): 0.0, ('2', '5'): 0.0, ('2', '7'): 0.0, ('3', '4'): 1.0,
                                   ('3', '6'): 1.0, ('3', '8'): 1.0}.items():

            edges_resp = node_importance_pb2.Edge(edge=list(e))
            dict_resp.append(node_importance_pb2.DictOutput(edge=edges_resp, output=v))

        expected = node_importance_pb2.BetweennessCentralityResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # error raising test

        result = self.client.find_betweenness_centrality(self.stub, self.graph, k=15, normalized=False, weight=True,
                                                         endpoints=True, seed=1, directed=True)
        self.assertIn('parameter k is larger than the number of nodes in the graph',result[1])


    def test_find_pagerank(self):
        # Default Test
        result = self.client.find_pagerank(self.stub, self.graph)
        print(result)

        dict_resp = []
        for n, v in {'1': 0.12113884655309373, '2': 0.23955113566709454, '3': 0.23955113566709454,
                         '4': 0.12113884655309375, '5': 0.06965500888990583, '6': 0.06965500888990583,
                         '7': 0.06965500888990583, '8': 0.06965500888990583}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.PageRankResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # Non Default Test

        personalizatoin = []
        for k,vv in {'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                       '6': 0.125, '7': 0.125, '8': 0.125}.items():
            personalizatoin.append(node_importance_pb2.DictIn(node=k,value=vv))

        nstart = []
        for k, vv in {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1}.items():
            nstart.append(node_importance_pb2.DictIn(node=k, value=vv))

        dangling = []
        for k, vv in {'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                '6': 0.125, '7': 0.125, '8': 0.125}.items():
            dangling.append(node_importance_pb2.DictIn(node=k, value=vv))

        result = self.client.find_pagerank(self.stub, self.graph,alpha=0.95,
                                      personalization=personalizatoin, max_iter=100,
                                      tol=1e-07,
                                      nstart=nstart,
                                      weight=True,
                                      dangling=dangling,directed=True)
        print(result)

        dict_resp = []
        for n, v in {'1': 0.08514279383409741, '2': 0.1255854995423924, '3': 0.12491155064890427, '4': 0.16514082203112918, '5': 0.12491155064890427, '6': 0.12469811632283417, '7': 0.12491155064890427, '8': 0.12469811632283417}.items():
            dict_resp.append(node_importance_pb2.DictOutput(node=n, output=v))

        expected = node_importance_pb2.PageRankResponse(status=True, message='success', output=dict_resp)

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertCountEqual(result.output, expected.output)

        # Error raising test

        personalizatoin = []
        for k, vv in {'1': 0.125, '2': 0.125, '31': 0.125, '4': 0.125, '5': 0.125,
                      '6': 0.125, '7': 0.125, '8': 0.125}.items():
            personalizatoin.append(node_importance_pb2.DictIn(node=k, value=vv))



        result = self.client.find_pagerank(self.stub, self.graph, personalization=personalizatoin)
        self.assertIn('personalization parameter contains a node at zero-indexed position 2 that does not exist in the graph', result[1])


    def test_find_eigenvector_centrality(self):
        # Default test
        expected_output = {
            'eigenvector_centrality': {'1': 0.35775018836999806, '2': 0.5298994260311778, '3': 0.5298994260311778,
                                       '4': 0.35775018836999806, '5': 0.2135666184274351, '6': 0.2135666184274351,
                                       '7': 0.2135666184274351, '8': 0.2135666184274351}}

        eigenvector_output_edges = []
        eigenvector_output_value = []
        for k, v in expected_output["eigenvector_centrality"].items():
            eigenvector_output_edges.append(k)
            eigenvector_output_value.append(v)

        output = node_importance_pb2.DictOutput(node=eigenvector_output_edges,
                                                output=eigenvector_output_value)

        result = self.client.find_eigenvector_centrality(self.stub, self.graph, )
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertEqual(result.output, output)

        # non Default Test
        expected_output_nstart = {
            'eigenvector_centrality': {'1': 0.35774203080090017, '2': 0.5299019638339402, '3': 0.5299019638339402,
                                       '4': 0.3577420308009002, '5': 0.21357030238703748, '6': 0.21357030238703748,
                                       '7': 0.21357030238703748, '8': 0.21357030238703748}}

        eigenvector_output_edges = []
        eigenvector_output_value = []
        for k, v in expected_output_nstart["eigenvector_centrality"].items():
            eigenvector_output_edges.append(k)
            eigenvector_output_value.append(v)

        output = node_importance_pb2.DictOutput(node=eigenvector_output_edges,
                                                output=eigenvector_output_value)

        result = self.client.find_eigenvector_centrality(self.stub, self.graph, max_iter=110, tol=1e-05,
                                                         nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                                                                 '8': 1}, weight=True, directed=False)
        # print(result)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertEqual(result.output, output)

        # Graph With No Nodes Test
        result = self.client.find_eigenvector_centrality(self.stub, self.graph_01)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "'nodes'")
        self.assertEqual(result[2], {})

        # Graph With No edges Test
        result = self.client.find_eigenvector_centrality(self.stub, self.graph_02)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "Parameter to MergeFrom() must be instance of same class: expected Graph got list.")
        self.assertEqual(result[2], {})

        # directed Test
        result = self.client.find_eigenvector_centrality(self.stub, self.graph, max_iter=110, tol=1e-05,
                                                         nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                                                                 '8': 1}, weight=True, directed=True)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertEqual(result.output, output)

        # weight less Test
        expected_out = {
            'eigenvector_centrality': {'1': 0.35775018836999806, '2': 0.5298994260311778, '3': 0.5298994260311778,
                                       '4': 0.35775018836999806, '5': 0.2135666184274351, '6': 0.2135666184274351,
                                       '7': 0.2135666184274351, '8': 0.2135666184274351}}
        eigenvector_output_edges = []
        eigenvector_output_value = []
        for k, v in expected_out["eigenvector_centrality"].items():
            eigenvector_output_edges.append(k)
            eigenvector_output_value.append(v)

        output = node_importance_pb2.DictOutput(node=eigenvector_output_edges,
                                                output=eigenvector_output_value)

        result = self.client.find_eigenvector_centrality(self.stub, self.graph_03)
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        self.assertEqual(result.output, output)

    def test_find_hits(self):
        # Hub Matrix Hits Test with default node
        hub_matrix_expected_out = {
            'hub_matrix': [[25.0, 0.0, 43.0, 0.0, 18.0, 0.0, 27.0, 0.0], [0.0, 151.0, 0.0, 47.0, 0.0, 40.0, 0.0, 50.0],
                           [43.0, 0.0, 238.0, 0.0, 30.0, 0.0, 45.0, 0.0], [0.0, 47.0, 0.0, 65.0, 0.0, 56.0, 0.0, 70.0],
                           [18.0, 0.0, 30.0, 0.0, 36.0, 0.0, 54.0, 0.0], [0.0, 40.0, 0.0, 56.0, 0.0, 64.0, 0.0, 80.0],
                           [27.0, 0.0, 45.0, 0.0, 54.0, 0.0, 81.0, 0.0], [0.0, 50.0, 0.0, 70.0, 0.0, 80.0, 0.0, 100.0]]}

        hits_list = []
        for i in hub_matrix_expected_out["hub_matrix"]:
            hits_list.append(node_importance_pb2.HitsOutput(hits_out=list(i)))

        result = self.client.find_hits(self.stub, self.graph, nodelist=None, mode='hub_matrix')
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        for i in range(len(result.output)):
            self.assertEqual(result.output[i], hits_list[i])

        # Authority Matrix Hits Test with default node
        authority_matrix_expected_out = {
            'authority_matrix': [[25.0, 0.0, 43.0, 0.0, 18.0, 0.0, 27.0, 0.0],
                                 [0.0, 151.0, 0.0, 47.0, 0.0, 40.0, 0.0, 50.0],
                                 [43.0, 0.0, 238.0, 0.0, 30.0, 0.0, 45.0, 0.0],
                                 [0.0, 47.0, 0.0, 65.0, 0.0, 56.0, 0.0, 70.0],
                                 [18.0, 0.0, 30.0, 0.0, 36.0, 0.0, 54.0, 0.0],
                                 [0.0, 40.0, 0.0, 56.0, 0.0, 64.0, 0.0, 80.0],
                                 [27.0, 0.0, 45.0, 0.0, 54.0, 0.0, 81.0, 0.0],
                                 [0.0, 50.0, 0.0, 70.0, 0.0, 80.0, 0.0, 100.0]]}
        hits_list = []
        for i in authority_matrix_expected_out["authority_matrix"]:
            hits_list.append(node_importance_pb2.HitsOutput(hits_out=list(i)))

        result = self.client.find_hits(self.stub, self.graph, nodelist=None, mode='authority_matrix')
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        for i in range(len(result.output)):
            self.assertEqual(result.output[i], hits_list[i])

        # Hub Matrix Hits Test with  node

        expected_with_node_hub = {'hub_matrix': [[9.0, 0.0], [0.0, 9.0]]}

        result = self.client.find_hits(self.stub, self.graph, nodelist=['1', '2'], mode='hub_matrix')
        hits_list = []
        for i in expected_with_node_hub["hub_matrix"]:
            hits_list.append(node_importance_pb2.HitsOutput(hits_out=list(i)))

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        for i in range(len(result.output)):
            self.assertEqual(result.output[i], hits_list[i])

        # Authority Matrix Hits Test with  node

        expected_with_node_authority = {'authority_matrix': [[9.0, 0.0], [0.0, 9.0]]}

        result = self.client.find_hits(self.stub, self.graph, nodelist=['1', '2'], mode='authority_matrix')
        hits_list = []
        for i in expected_with_node_authority["authority_matrix"]:
            hits_list.append(node_importance_pb2.HitsOutput(hits_out=list(i)))

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        for i in range(len(result.output)):
            self.assertEqual(result.output[i], hits_list[i])

        # Graph With No Nodes Test
        result = self.client.find_hits(self.stub, self.graph_01, mode='authority_matrix')
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "'nodes'")
        self.assertEqual(result[2], {})

        result = self.client.find_hits(self.stub, self.graph_01, mode='hub_matrix')
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "'nodes'")
        self.assertEqual(result[2], {})

        # Graph With No edges Test
        result = self.client.find_hits(self.stub, self.graph_02, mode='authority_matrix')
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "Parameter to MergeFrom() must be instance of same class: expected Graph got list.")
        self.assertEqual(result[2], {})

        result = self.client.find_hits(self.stub, self.graph_02, mode='hub_matrix')
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "Parameter to MergeFrom() must be instance of same class: expected Graph got list.")
        self.assertEqual(result[2], {})

        # directed Graph test

        expected_with_node_authority = {'hub_matrix': [[9.0, 0.0], [0.0, 9.0]]}

        result = self.client.find_hits(self.stub, self.graph, nodelist=['1', '2'], directed=True)
        hits_list = []
        for i in expected_with_node_authority["hub_matrix"]:
            hits_list.append(node_importance_pb2.HitsOutput(hits_out=list(i)))

        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        for i in range(len(result.output)):
            self.assertEqual(result.output[i], hits_list[i])

        # weightless test
        expected_result = {'hub_matrix': [[1.0, 0.0], [0.0, 1.0]]}

        hits_list = []
        for i in expected_result["hub_matrix"]:
            hits_list.append(node_importance_pb2.HitsOutput(hits_out=list(i)))

        result = self.client.find_hits(self.stub, self.graph_03, nodelist=['1', '2'])
        self.assertEqual(result.status, True)
        self.assertEqual(result.message, 'success')
        for i in range(len(result.output)):
            self.assertEqual(result.output[i], hits_list[i])

    def test_additional(self):
        # wrong Number of wrights test taking one functionality as example
        result = self.client.find_central(self.stub, self.graph_04)
        self.assertEqual(result.status, False)
        self.assertEqual(result.message, 'the length of supplied edges and weights does not match')

    def tearDown(self):
        self.server.stop_server()


if __name__ == '__main__':
    suite = unittest.TestSuite()

    unittest.main()
