#Tested on python3.6

import unittest
import robustness

import networkx as nx



class TestRobustness(unittest.TestCase):


    def test_min_nodes_to_remove(self):
        b = robustness.Robustness()
        graph = {
        "nodes": [],
        "edges": [[1,2]]
        }

        source_node = 1
        target_node = 2
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual([False, 'graph should at least contain two nodes',{}],ret)
        graph = {
        "nodes": [1],
        "edges": []
        }
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual([False, 'graph should at least contain one edge',{}],ret)
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
        # a
        graph = {
            "nodes": [1, 2, 3],
            "edges": [[1, 2], ['',2]]
        }
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual(
            [False, 'Element of the input array edges at zero-indexed poistion 1 does contain an empty node', {}], ret)
        # a
        # a
        graph = {
            "nodes": [1, 2, 3],
            "edges": [['', 2], [5, 2]]
        }
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual(
            [False, 'Element of the input array edges at zero-indexed poistion 0 does contain an empty node', {}], ret)
        # a
        # a
        graph = {
            "nodes": [1, 2, 3],
            "edges": [[3, 2], [2, 2],['', 2], [5, 2]]
        }
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual(
            [False, 'Element of the input array edges at zero-indexed poistion 2 does contain an empty node', {}], ret)
        # a
        graph = {
        "nodes": [1,2,3],
        "edges": [[1,2],[2,3]]
        }
        source_node = 1
        target_node = 4
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual([False, 'The target node does not exist in graph',{}], ret)
        graph = {
        "nodes": [1,2,3],
        "edges": [[1,2],[2,3]]
        }
        source_node = 5
        target_node = 3
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual([False, 'The source node does not exist in graph',{}],ret)
        graph = {
        "nodes": [1,2,3,4],
        "edges": [[1,2],[2,3]]
        }
        # source_node = 1
        # target_node = 4
        # ret = b.min_nodes_to_remove(graph, source_node, target_node)
        # self.assertEqual([False, 'no path exists between node 1 and node 4',{}],ret)
        graph = {
        "nodes": [1,2,3,4,5],
        "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[4,6]]
        }
        source_node = 1
        target_node = 6
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual([False, 'edge value at [5][1] is not a node',{}],ret)

        # a

        graph = {
            "nodes": [1, 2, 3, 4, 5],
            "edges": [[1, 2], [1, 4], [2, 3], [2, 5], [3, 4], [6, 3], [4, 6]]
        }
        source_node = 1
        target_node = 6
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual([False, 'edge value at [5][0] is not a node', {}], ret)

        # a

        graph = {
        "nodes": [1,2,3,4,5,6],
        "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[4,6]]
        }
        source_node = 1
        target_node = 6
        ret = b.min_nodes_to_remove(graph, source_node, target_node)
        self.assertEqual([True, 'success', {'edges': [[4, 6], [3, 6]], 'nodes': [3, 4]}],ret)



    def test_most_important_nodes_edges_subset(self):
        b = robustness.Robustness()
        graph = {
            "nodes": [],
            "edges": [[1,2]]
        }
        source_nodes = [1]
        target_nodes = [2]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'graph should at least contain two nodes',{}],ret)
        graph = {
            "nodes": [1],
            "edges": []
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'graph should at least contain one edge',{}],ret)
        graph = {
            "nodes": [1,2],
            "edges": 3
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'the supplied edge is not type array',{}],ret)
        # v
        graph = {
            "nodes": 1,
            "edges": 3
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'the supplied nodes is not type array', {}], ret)
        # v
        graph = {
            "nodes": [1,2],
            "edges": [[1,2]],
            "weights": 3
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'the supplied weight is not type array',{}],ret)
        graph = {
            "nodes": [1,2],
            "edges": [[1,2]],
            "weights": [3,4]
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'the length of supplied edges and weights does not match',{}],ret) 
        graph = {
            "nodes": [1,2],
            "edges": [[1,2]],
            "weights": [3]
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 17)
        self.assertEqual([False, 'Parameter T can only be 0 or 1',{}],ret) # type=0(most important nodes) type=1(most important edges)
        graph = {
            "nodes": [1,2,3],
            "edges": [[1,2],2,3]
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 is not an array',{}],ret)
        graph = {
            "nodes": [1,2,3],
            "edges": [[1,2],[2]]
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does not contain two nodes',{}],ret)
        graph = {
            "nodes": [1,2,3],
            "edges": [[1,2],[2,'']]
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does contain an empty node',{}],ret)
        graph = {
            "nodes": [1,2,3],
            "edges": [[1,2],[2,None]]
        }
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 does contain an empty node',{}],ret)
        graph = {
            "nodes": [1,2,3,4,5,6,7,8],
            "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]]
        }
        source_nodes = 5
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'Element of the input source_nodes is not an array',{}],ret)
        source_nodes = [5,7]
        target_nodes = 6
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'Element of the input target_nodes is not an array',{}],ret)
        
        source_nodes = [5,7,10]
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 0)
        self.assertEqual([False, 'source_nodes [2] does not exist in graph',{}],ret) #everything in source/target nodes must be in graph

        source_nodes = [5,7]
        target_nodes = [6,11]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'target_nodes [1] does not exist in graph',{}],ret)


        graph = {
            "nodes": [1,2,3,4,5,6,7,8],
            "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],
            "weights": [0,4,5,6,7,8,9,10]
        }
        source_nodes = [5,7]
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 1)
        self.assertEqual([False, 'all edge weights must be greater than zero', {}],ret)

        # Error
        graph = {
            "nodes": [1, 2, 3, 4, 5, 6, 7, 8],
            "edges": [[1, 2], [1, 4], [2, 3], [2, 5], [3, 4], [3, 6], [2, 7], [3, 8]],
        }
        source_nodes = [5, 7]
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 1, weight=True)
        self.assertEqual([False,'weight parameter specified but weights are not given in input graph'],ret)

        graph = {
            "nodes": [1,2,3,4,5,6,7,8],
            "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]]
          
        }
        
        source_nodes = [5,7]
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 0)
        self.assertEqual([True, 'success',{'betweenness_centrality': [[2, 3], 1.0]}],ret)


        graph = {
            "nodes": [1,2,3,4,5,6,7,8],
            "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],
            "weights": [3,4,5,6,7,8,9,10]
        }
        source_nodes = [5,7]
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 1)
        self.assertEqual([True, 'success', {'betweenness_centrality': [[(2, 3), (3, 6)], 1.0]}],ret)


        ### For directed graphs

        graph = {
            "nodes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "edges": [[1, 2], [1, 4], [2, 3], [2, 5], [3, 4], [3, 6], [2, 7], [3, 8], [7, 9], [5, 9], [9, 10], [10, 6]]

        }

        source_nodes = [5,7]
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 0, False, True)
        self.assertEqual([True, 'success',{'betweenness_centrality': [[9,10],2.0]}],ret)

        graph = {
            "nodes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "edges": [[1, 2], [1, 4], [2, 3], [2, 5], [3, 4], [3, 6], [2, 7], [3, 8], [7, 9], [5, 9], [9, 10], [10, 6]]

        }

        source_nodes = [5,7]
        target_nodes = [6]
        ret = b.most_important_nodes_edges_subset(graph, source_nodes, target_nodes, 1, False, True)
        self.assertEqual([True, 'success', {'betweenness_centrality': [[(9, 10), (10, 6)], 2.0]}],ret)




__end__ = '__end__'


if __name__ == '__main__':
    unittest.main()
