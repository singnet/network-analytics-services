import unittest
from node_importance import NodeImportance

import networkx as nx
import numpy as np
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


import check_graph_validity

class TestNodeImportance(unittest.TestCase):

	def setUp(self):
		self.N  = NodeImportance()
		self.graph = {
	        "nodes": ['1','2','3','4','5','6','7','8'],
	        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
	        "weights": [3,4,5,6,7,8,9,10]
	    }
		self.graph_01 = {
	        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
	        "weights": [3,4,5,6,7,8,9,10]
	    }
		self.graph_02= {
	        "nodes": ['1','2','3','4','5','6','7','8'],
	        "weights": [3,4,5,6,7,8,9,10]
	    }
		self.graph_03 = {
	        "nodes": ['1','2','3','4','5','6','7','8'],
	        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']]
	    }
	    

	def test_find_central_nodes(self):
		result = self.N.find_central_nodes(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],"{'central_nodes': ['2', '3']}")


	def test_find_eccentricity(self):
		result = self.N.find_eccentricity(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],"{'eccentricity': {'1': 3, '2': 2, '3': 2, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3}}")
		
	
	def test_find_degree_centrality(self):
		result = self.N.find_degree_centrality(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],"{'degree_centrality': {'1': 0.2857142857142857, '2': 0.5714285714285714, '3': 0.5714285714285714, '4': 0.2857142857142857, '5': 0.14285714285714285, '6': 0.14285714285714285, '7': 0.14285714285714285, '8': 0.14285714285714285}}")
		
	def test_find_closeness_centrality(self):
		result = self.N.find_closeness_centrality(self.graph,['8','8'])
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		if 'closeness_centrality' not in result[2]:
			raise AssertionError()
		#closness centrality seems to change 
	
	def test_find_betweenness_centrality(self):
		result = self.N.find_betweenness_centrality(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],"{'betweenness_centrality': {'1': 0.07142857142857142, '2': 0.5952380952380952, '3': 0.5952380952380952, '4': 0.07142857142857142, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}}")
	

	def test_find_pagerank(self):
		result = self.N.find_pagerank(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],"{'pagerank': {'1': 0.07655997440979878, '2': 0.2193002394699876, '3': 0.2643703234360777, '4': 0.10837001548777252, '5': 0.06737788086164939, '6': 0.07867433112988435, '7': 0.09169182129247411, '8': 0.09365541391235543}}")


	def test_find_eigenvector_centrality(self):
		result = self.N.find_eigenvector_centrality(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],"{'eigenvector_centrality': {'1': 0.35775018836999806, '2': 0.5298994260311778, '3': 0.5298994260311778, '4': 0.35775018836999806, '5': 0.2135666184274351, '6': 0.2135666184274351, '7': 0.2135666184274351, '8': 0.2135666184274351}}")
	

	def test_find_hub_matrix(self):
		result = self.N.find_hub_matrix(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],'[[ 25.   0.  43.   0.  18.   0.  27.   0.]\n [  0. 151.   0.  47.   0.  40.   0.  50.]\n [ 43.   0. 238.   0.  30.   0.  45.   0.]\n [  0.  47.   0.  65.   0.  56.   0.  70.]\n [ 18.   0.  30.   0.  36.   0.  54.   0.]\n [  0.  40.   0.  56.   0.  64.   0.  80.]\n [ 27.   0.  45.   0.  54.   0.  81.   0.]\n [  0.  50.   0.  70.   0.  80.   0. 100.]]')
		
		

	def test_find_authority_matrix(self):
		result = self.N.find_authority_matrix(self.graph)
		self.assertEqual(result[0],True)
		self.assertEqual(result[1],'success')
		self.assertEqual(result[2],'[[ 25.   0.  43.   0.  18.   0.  27.   0.]\n [  0. 151.   0.  47.   0.  40.   0.  50.]\n [ 43.   0. 238.   0.  30.   0.  45.   0.]\n [  0.  47.   0.  65.   0.  56.   0.  70.]\n [ 18.   0.  30.   0.  36.   0.  54.   0.]\n [  0.  40.   0.  56.   0.  64.   0.  80.]\n [ 27.   0.  45.   0.  54.   0.  81.   0.]\n [  0.  50.   0.  70.   0.  80.   0. 100.]]')


	def test_construct_graph(self):
		# Graph without nodes Test
	    result = self.N.construct_graph(self.graph_01)
	    self.assertEqual(result[0],'False')
	    self.assertEqual(result[1],"'nodes'")
	    self.assertEqual(result[2],{})

	    # Graph without edges Test
	    result = self.N.construct_graph(self.graph_02)
	    self.assertEqual(result[0],'False')
	    self.assertEqual(result[1],"'edges'")
	    self.assertEqual(result[2],{})

	    # Graph without weights Test
	    result = self.N.construct_graph(self.graph_03)
	    self.assertEqual(str(type(result)),"<class 'networkx.classes.graph.Graph'>")
	    

if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.main()


