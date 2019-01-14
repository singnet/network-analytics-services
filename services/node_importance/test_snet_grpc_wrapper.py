import unittest
from node_importance import NodeImportance

import networkx as nx
import numpy as np
from client import ClientTest
from server import *



class TestNodeImportance(unittest.TestCase):

	def setUp(self):
		self.server = Server()
		self.server.start_server()
		self.client = ClientTest()
		self.stub = self.client.open_grpc_channel()
		self.graph = {
	        "nodes": ['1','2','3','4','5','6','7','8'],
	        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
	        "weights": [3,4,5,6,7,8,9,10]
	    	}
	def test_find_central_nodes(self):
		result = self.client.find_central(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,"{'central_nodes': ['2', '3']}")

	def test_find_eccentricity(self):
		result = self.client.find_eccentricity(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,"{'eccentricity': ['2', '3', '1', '4', '5', '6', '7', '8']}")
		

	def test_find_degree_centrality(self):
		result = self.client.find_degree_centrality(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,"{'degree_centrality': {'1': 0.2857142857142857, '2': 0.5714285714285714, '3': 0.5714285714285714, '4': 0.2857142857142857, '5': 0.14285714285714285, '6': 0.14285714285714285, '7': 0.14285714285714285, '8': 0.14285714285714285}}")
		
	def test_find_closeness_centrality(self):
		result = self.client.find_closeness_centrality(self.stub,self.graph,[1,2])
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		# self.assertEqual(repr(result.output),"{'closeness_centrality': {'1': 0.5714285714285714, '2': 0.8, '8': 0.75, '6': 0.75, '3': 1.2, '5': 0.75, '4': 0.8571428571428571, '7': 0.75}}")
		# self.assertEqual(repr(result.output),"{'closeness_centrality': {'2': 0.8, '1': 0.5714285714285714, '5': 0.75, '8': 0.75, '3': 1.2, '7': 0.75, '6': 0.75, '4': 0.8571428571428571}}")
		

	def test_find_betweenness_centrality(self):
		result = self.client.find_betweenness_centrality(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,"{'betweenness_centrality': {'1': 0.07142857142857142, '2': 0.5952380952380952, '3': 0.5952380952380952, '4': 0.07142857142857142, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}}")
	
	def test_find_pagerank(self):
		result = self.client.find_pagerank(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,"{'pagerank': {'1': 0.12113884655309373, '2': 0.23955113566709454, '3': 0.23955113566709454, '4': 0.12113884655309375, '5': 0.06965500888990583, '6': 0.06965500888990583, '7': 0.06965500888990583, '8': 0.06965500888990583}}")

	def test_find_eigenvector_centrality(self):
		result = self.client.find_eigenvector_centrality(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,"{'eigenvector_centrality': {'1': 0.35775018836999806, '2': 0.5298994260311778, '3': 0.5298994260311778, '4': 0.35775018836999806, '5': 0.2135666184274351, '6': 0.2135666184274351, '7': 0.2135666184274351, '8': 0.2135666184274351}}")
	
	def test_find_hub_matrix(self):
		result = self.client.find_hub_matrix(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,'[[2. 0. 2. 0. 1. 0. 1. 0.]\n [0. 4. 0. 2. 0. 1. 0. 1.]\n [2. 0. 4. 0. 1. 0. 1. 0.]\n [0. 2. 0. 2. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]]')
		
	def test_find_authority_matrix(self):
		result = self.client.find_authority_matrix(self.stub,self.graph)
		self.assertEqual(result.status,True)
		self.assertEqual(result.messgae,'success')
		self.assertEqual(result.output,'[[2. 0. 2. 0. 1. 0. 1. 0.]\n [0. 4. 0. 2. 0. 1. 0. 1.]\n [2. 0. 4. 0. 1. 0. 1. 0.]\n [0. 2. 0. 2. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]]')

	def tearDown(self):
		self.server.stop_server()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(TestNodeImportance("test_find_central_nodes"))
    # suite.addTest(TestNodeImportance("test_find_eccentricity"))
    # suite.addTest(TestNodeImportance("test_find_degree_centrality"))
    # suite.addTest(TestNodeImportance("test_find_closeness_centrality"))
    # suite.addTest(TestNodeImportance("test_find_betweenness_centrality"))
    # suite.addTest(TestNodeImportance("test_find_pagerank"))
    # suite.addTest(TestNodeImportance("test_find_eigenvector_centrality"))
    # suite.addTest(TestNodeImportance("test_find_hub_matrix"))
    # suite.addTest(TestNodeImportance("test_find_authority_matrix"))

    unittest.main()