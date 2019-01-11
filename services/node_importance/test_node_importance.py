import unittest
import graphs
from node_importance import NodeImportance

import networkx as nx



class TestNodeImportance(unittest.TestCase):

	def setUp(self):
		self.N  = NodeImportance()
		self.graph = {
		"nodes": [1,2,3,4,5,6,7,8],
		"edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],
		"weights": [3,4,5,6,7,8,9,10]
		}


	def test_find_central_nodes(self):
		result = self.N.find_central_nodes(self.graph)
		assert(result==[2,3])

	def test_find_eccentricity(self):
		result = self.N.find_eccentricity(self.graph)
		assert(result==[2, 3, 1, 4, 5, 6, 7, 8])

	def test_find_degree_centrality(self):
		result = self.N.find_degree_centrality(self.graph)
		assert(result=={1: 0.2857142857142857, 2: 0.5714285714285714, 3: 0.5714285714285714, 4: 0.2857142857142857, 5: 0.14285714285714285, 6: 0.14285714285714285, 7: 0.14285714285714285, 8: 0.14285714285714285})

	def test_find_closeness_centrality(self):
		result = self.N.find_closeness_centrality(self.graph,[1,2])
		assert(result=={1: 0.5714285714285714, 2: 0.8, 3: 1.2, 4: 0.8571428571428571, 5: 0.75, 6: 0.75, 7: 0.75, 8: 0.75})

	def test_find_betweenness_centrality(self):
		result = self.N.find_betweenness_centrality(self.graph)
		assert(result=={1: 0.07142857142857142, 2: 0.5952380952380952, 3: 0.5952380952380952, 4: 0.07142857142857142, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0})

	def test_find_pagerank(self):
		result = self.N.find_pagerank(self.graph)
		assert(result=={1: 0.07655997440979878, 2: 0.2193002394699876, 3: 0.2643703234360777, 4: 0.10837001548777252, 5: 0.06737788086164939, 6: 0.07867433112988435, 7: 0.09169182129247411, 8: 0.09365541391235543}
)

	def test_find_eigenvector_centrality(self):
		result = self.N.find_eigenvector_centrality(self.graph)
		assert(result=={1: 0.35775018836999806, 2: 0.5298994260311778, 3: 0.5298994260311778, 4: 0.35775018836999806, 5: 0.2135666184274351, 6: 0.2135666184274351, 7: 0.2135666184274351, 8: 0.2135666184274351})


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestNodeImportance("test_find_central_nodes"))
    suite.addTest(TestNodeImportance("test_find_eccentricity"))
    suite.addTest(TestNodeImportance("test_find_degree_centrality"))
    suite.addTest(TestNodeImportance("test_find_closeness_centrality"))
    suite.addTest(TestNodeImportance("test_find_betweenness_centrality"))
    suite.addTest(TestNodeImportance("test_find_pagerank"))
    suite.addTest(TestNodeImportance("test_find_eigenvector_centrality"))
    unittest.main()


