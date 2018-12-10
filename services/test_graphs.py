# coding: utf-8


import unittest
import graphs

import networkx as nx



class TestGraphs(unittest.TestCase):


	def test_min_nodes_to_remove(self):
		b = graphs.Graphs()
		graph = {
		"nodes": [],
		"edges": [[1,2]]
		}

		source_node = 1
		target_node = 2
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'graph should atleast contain two nodes',{}],ret)
		graph = {
		"nodes": [1],
		"edges": []
		}
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'graph should atleast contain one edge',{}],ret)
		graph = {
		"nodes": [1,2],
		"edges": 3
		}
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'the supplied edge is not type array',{}],ret)
		graph = {
		"nodes": [1,2,3],
		"edges": [[1,2],2,3]
		}
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 is not an array',{}],ret)
		graph = {
		"nodes": [1,2,3],
		"edges": [[1,2],[2]]
		}
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does not contain two nodes',{}],ret)
		graph = {
		"nodes": [1,2,3],
		"edges": [[1,2],[2,'']]
		}
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does contain an empty node',{}],ret)
		graph = {
		"nodes": [1,2,3],
		"edges": [[1,2],[2,None]]
		}
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does contain an empty node',{}],ret)
		graph = {
		"nodes": [1,2,3],
		"edges": [[1,2],[2,3]]
		}
		source_node = 1
		target_node = 4
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'node 4 doesn’t exist in the graph',{}], ret)
		graph = {
		"nodes": [1,2,3],
		"edges": [[1,2],[2,3]]
		}
		source_node = 5
		target_node = 3
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'node 5 doesn’t exist in the graph',{}],ret)
		graph = {
		"nodes": [1,2,3,4],
		"edges": [[1,2],[2,3]]
		}
		source_node = 1
		target_node = 4
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([False, 'no path exists between node 1 and node 4',{}],ret)
		graph = {
		"nodes": [1,2,3,4,5],
		"edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[4,6]]
		}
		source_node = 1
		target_node = 6
		ret = b.min_nodes_to_remove(graph, source_node, target_node)
		self.assertEqual([True, 'success', {'edges': [[4, 6], [3, 6]], 'nodes': [3, 4]}],ret)



	def test_most_important_nodes_edges(self):
		b = graphs.Graphs()
		graph = {
		    "nodes": [],
		    "edges": [[1,2]]
		}
		source_nodes = [1]
		target_nodes = [2]
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'graph should atleast contain two nodes',{}],ret)
		graph = {
		    "nodes": [1],
		    "edges": []
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'graph should atleast contain one edge',{}],ret)
		graph = {
		    "nodes": [1,2],
		    "edges": 3
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'the supplied edge is not type array',{}],ret)
		graph = {
		    "nodes": [1,2],
		    "edges": [[1,2]],
		    "weights": 3
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'the supplied weight is not type array',{}],ret)
		graph = {
		    "nodes": [1,2],
		    "edges": [[1,2]],
		    "weights": [3,4]
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'the length of supplied edges and weights does not match',{}],ret) 
		graph = {
		    "nodes": [1,2],
		    "edges": [[1,2]],
		    "weights": [3]
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes, 17) 
		self.assertEqual([False, 'type can only be 0 or 1',{}],ret) # type=0(most important nodes) type=1(most important edges)
		graph = {
		    "nodes": [1,2,3],
		    "edges": [[1,2],2,3]
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 is not an array',{}],ret)
		graph = {
		    "nodes": [1,2,3],
		    "edges": [[1,2],[2]]
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does not contain two nodes',{}],ret)
		graph = {
		    "nodes": [1,2,3],
		    "edges": [[1,2],[2,'']]
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does contain an empty node',{}],ret)
		graph = {
		    "nodes": [1,2,3],
		    "edges": [[1,2],[2,None]]
		}
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does contain an empty node',{}],ret)
		graph = {
		    "nodes": [1,2,3,4,5,6,7,8],
		    "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]]
		}
		source_nodes = 5
		target_nodes = [6]
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'Element of the input source_nodes is not an array',{}],ret)
		source_nodes = [5,7]
		target_nodes = 6
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'Element of the input target_nodes is not an array',{}],ret)
		
		source_nodes = [5,7,10]
		target_nodes = [6]
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes,0)
		self.assertEqual([False, 'node 10 doesn’t exist in the graph',{}],ret) #everything in source/target nodes must be in graph

		source_nodes = [5,7]
		target_nodes = [6,11]
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		self.assertEqual([False, 'node 11 doesn’t exist in the graph',{}],ret)

		# graph = {
		#     "nodes": [1,2,3,4,5,6,7,8,20],
		#     "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]]
		# }
		# source_nodes = [5,7,20]
		# target_nodes = [6]
		# ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
		# self.assertEqual([False, 'no path exists from node 20 to node 6', {}],ret) #since 5,6,7 are consecutive and are ok?!
		graph = {
		    "nodes": [1,2,3,4,5,6,7,8],
		    "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],
		  
		}
		
		source_nodes = [5,7]
		target_nodes = [6]
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes, 0)
		self.assertEqual([True, 'success', {'betweenness_centrality':{1: 0.0, 2: 0.047619047619047616, 3: 0.047619047619047616, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0}}],ret)
		
		graph = {
		    "nodes": [1,2,3,4,5,6,7,8],
		    "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],
		    "weights": [3,4,5,6,7,8,9,10]
		}
		source_nodes = [5,7]
		target_nodes = [6]
		ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes, 1)
		self.assertEqual([True, 'success', {'betweenness_centrality':{(1, 2): 0.0, (1, 4): 0.0, (2, 3): 0.03571428571428571, (2, 5): 0.017857142857142856, (2, 7): 0.017857142857142856, (3, 4): 0.0, (3, 6): 0.03571428571428571, (3, 8): 0.0}}],ret)




__end__ = '__end__'


if __name__ == '__main__':
    unittest.main()
