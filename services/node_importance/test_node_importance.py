import unittest
from node_importance import NodeImportance
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import check_graph_validity


class TestNodeImportance(unittest.TestCase):

    def setUp(self):
        self.N = NodeImportance()
        self.cv = check_graph_validity.Graphs()
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

        self.graph_06 = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
        }

        self.graph_07 = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, -5, 6, 7, 8, 9, 10]
        }

    def test_find_central_nodes(self):
        # Default Test
        result = self.N.find_central_nodes(self.graph)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertCountEqual(result[2], ['2','3'])

        # Nondefault Test
        result = self.N.find_central_nodes(self.graph,usebounds=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertCountEqual(result[2], ['2', '3'])

        # Incorrect input data
        result = self.N.find_central_nodes(self.graph_05)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'edge value at [3][1] is not a node')


    def test_find_Periphery(self):
        # Default Test
        result = self.N.find_Periphery(self.graph)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertCountEqual(result[2], ['1', '4', '5', '6', '7', '8'])

        # Non Default Test
        result = self.N.find_Periphery(self.graph, usebounds=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertCountEqual(result[2], ['1', '4', '5', '6', '7', '8'])

        # Non weighted Test
        result = self.N.find_Periphery(self.graph_03)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertCountEqual(result[2], ['1', '4', '5', '6', '7', '8'])

        # Incorrect input data
        result = self.N.find_central_nodes(self.graph_05)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'edge value at [3][1] is not a node')

    def test_find_degree_centrality(self):
        # Default Test
        result = self.N.find_degree_centrality(self.graph)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {
            'degree_centrality': {'1': 0.2857142857142857, '2': 0.5714285714285714, '3': 0.5714285714285714,
                                  '4': 0.2857142857142857, '5': 0.14285714285714285, '6': 0.14285714285714285,
                                  '7': 0.14285714285714285, '8': 0.14285714285714285}})

        # Default Test 2
        result = self.N.find_degree_centrality(self.graph, in_out='')
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {
            'degree_centrality': {'1': 0.2857142857142857, '2': 0.5714285714285714, '3': 0.5714285714285714,
                                  '4': 0.2857142857142857, '5': 0.14285714285714285, '6': 0.14285714285714285,
                                  '7': 0.14285714285714285, '8': 0.14285714285714285}})

        # Non Default Test 1
        result = self.N.find_degree_centrality(self.graph, in_out='out')
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {
            'degree_centrality': {'1': 0.2857142857142857, '2': 0.42857142857142855,
                                     '3': 0.42857142857142855, '4': 0.0,
                                     '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0}})

        # Non Default Test 2
        result = self.N.find_degree_centrality(self.graph, in_out='in')
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {
            'degree_centrality': {'1': 0.0, '2': 0.14285714285714285, '3': 0.14285714285714285,
                                    '4': 0.2857142857142857,
                                    '5': 0.14285714285714285, '6': 0.14285714285714285,
                                    '7': 0.14285714285714285,
                                    '8': 0.14285714285714285}})

        # INvalid input
        result = self.N.find_degree_centrality(self.graph, in_out='inn')
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'Wrong in_out parameter specified')

        # INvalid input 2
        result = self.N.find_degree_centrality(self.graph_05,in_out='')
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'edge value at [3][1] is not a node')

    def test_find_closeness_centrality(self):
        # Default Test
        result = self.N.find_closeness_centrality(self.graph)

        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertDictEqual(result[2]['closeness_centrality'],{'1': 0.5, '2': 0.7, '3': 0.7, '4': 0.5, '5': 0.4375, '6': 0.4375, '7': 0.4375, '8': 0.4375})


        # # Non Default Test
        result = self.N.find_closeness_centrality(self.graph, distance=True, wf_improved=False, reverse=True, directed=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertDictEqual(result[2]['closeness_centrality'],{'1': 0.5, '2': 0.6666666666666666, '3': 1.0, '4': 0.0, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0})

        # # Non Default Test
        result = self.N.find_closeness_centrality(self.graph_06, distance=True, wf_improved=False, reverse=True,
                                                  directed=True)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'distance parameter specified but weights are not given in input graph')

        # Incorrect input data
        result = self.N.find_closeness_centrality(self.graph_05)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'edge value at [3][1] is not a node')

    def test_find_betweenness_centrality(self):

        # Error 1
        result = self.N.find_betweenness_centrality(self.graph, type='xxx')
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'type parameter can only be node or edge')

        # Error 2
        result = self.N.find_betweenness_centrality(self.graph_06, type='node',weight=True)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'weight parameter specified but weights are not given in input graph')

        # Error 3
        result = self.N.find_betweenness_centrality(self.graph_06, type='node', k=9)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'parameter k is larger than the number of nodes in the graph')

        # Error 4
        result = self.N.find_betweenness_centrality(self.graph_07, weight=True)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'one or more weights in the graph are less than zero')

        # Default Test
        result = self.N.find_betweenness_centrality(self.graph)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertDictEqual(result[2]['betweenness_centrality'], {'1': 0.07142857142857142, '2': 0.5952380952380952,'3': 0.5952380952380952, '4': 0.07142857142857142,'5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0})

        # Default test edge
        result = self.N.find_betweenness_centrality(self.graph, type='edge')
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertDictEqual(result[2]['betweenness_centrality'],
            {('1', '2'): 0.21428571428571427, ('1', '4'): 0.14285714285714285,
                                       ('2', '3'): 0.42857142857142855, ('2', '5'): 0.25, ('2', '7'): 0.25,
                                       ('3', '4'): 0.21428571428571427, ('3', '6'): 0.25, ('3', '8'): 0.25})
        # Non Default Test 1
        result = self.N.find_betweenness_centrality(self.graph, k=1, normalized=False, weight=True, endpoints=True,
                                                    seed=1)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertDictEqual(result[2]['betweenness_centrality'], {'1': 4.0, '2': 14.0, '3': 28.0, '4': 6.0, '5': 4.0, '6': 4.0, '7': 4.0,'8': 4.0})

        # Non weighted Test 1
        result = self.N.find_betweenness_centrality(self.graph_03, k=1, normalized=False, weight=False, endpoints=True,
                                                    seed=1)

        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertDictEqual(result[2]['betweenness_centrality'],
            {'1': 4.0, '2': 14.0, '3': 28.0, '4': 6.0, '5': 4.0, '6': 4.0, '7': 4.0,
                                       '8': 4.0})

        # Non Default Test 2
        result = self.N.find_betweenness_centrality(self.graph_03, k=1, normalized=False, weight=False, endpoints=True,
                                                    seed=1, directed=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2]['betweenness_centrality'], {'1': 0.0, '2': 0.0, '3': 3.0, '4': 1.0, '5': 0.0, '6': 1.0, '7': 0.0, '8': 1.0})

        # Non Default Test 1
        result = self.N.find_betweenness_centrality(self.graph, k=1, normalized=False, weight=True, seed=1,directed=True,type='edge')
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertDictEqual(result[2]['betweenness_centrality'],
                             {('1', '2'): 0.0, ('1', '4'): 0.0, ('2', '3'): 0.0, ('2', '5'): 0.0, ('2', '7'): 0.0,
                              ('3', '4'): 1.0, ('3', '6'): 1.0, ('3', '8'): 1.0})

    def test_find_pagerank(self):
        # Default Test
        result = self.N.find_pagerank(self.graph)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {
            'pagerank': {'1': 0.12113884655309373, '2': 0.23955113566709454, '3': 0.23955113566709454,
                         '4': 0.12113884655309375, '5': 0.06965500888990583, '6': 0.06965500888990583,
                         '7': 0.06965500888990583, '8': 0.06965500888990583}})

        # Non Default Test, all default values used expect directed
        result = self.N.find_pagerank(self.graph, alpha=0.95,
                                      personalization={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                       '6': 0.125, '7': 0.125, '8': 0.125}, max_iter=100,
                                      tol=1e-07,
                                      nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1},
                                      weight=True,
                                      dangling={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                '6': 0.125, '7': 0.125, '8': 0.125})
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2],
                         {'pagerank': {'1': 0.12353302891578935, '2': 0.24675733134387767, '3': 0.2467573313438777,
                                       '4': 0.12353302891578932, '5': 0.06485481987016649, '6': 0.06485481987016647,
                                       '7': 0.06485481987016649, '8': 0.06485481987016647}})

        # Non weighted Test
        result = self.N.find_pagerank(self.graph_03, alpha=0.95,
                                      personalization={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                       '6': 0.125, '7': 0.125, '8': 0.125}, max_iter=100,
                                      tol=1e-07,
                                      nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1},
                                      weight=False,
                                      dangling={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                '6': 0.125, '7': 0.125, '8': 0.125})
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2],
                         {'pagerank': {'1': 0.12353302891578935, '2': 0.24675733134387767, '3': 0.2467573313438777,
                                       '4': 0.12353302891578932, '5': 0.06485481987016649, '6': 0.06485481987016647,
                                       '7': 0.06485481987016649, '8': 0.06485481987016647}})

        # Non default Test 2
        result = self.N.find_pagerank(self.graph_03, alpha=0.95,
                                      personalization={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                       '6': 0.125, '7': 0.125, '8': 0.125}, max_iter=100,
                                      tol=1e-07,
                                      nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1},
                                      weight=False,
                                      dangling={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                '6': 0.125, '7': 0.125, '8': 0.125}, directed=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2],
                         {'pagerank': {'1': 0.08514279383409741, '2': 0.1255854995423924, '3': 0.12491155064890427,
                                       '4': 0.16514082203112918, '5': 0.12491155064890427, '6': 0.12469811632283417,
                                       '7': 0.12491155064890427, '8': 0.12469811632283417}})

        result = self.N.find_pagerank(self.graph,personalization={'1': 0.125, '112': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                       '6': 0.125, '7': 0.125, '8': 0.125})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'personalization parameter contains a node at zero-indexed position 1 that does not exist in the graph')

        result = self.N.find_pagerank(self.graph,
                                      personalization={'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
                                                       '6': 0, '7': 0, '8': 0})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'one personalization value should at lease be non-zero')

        result = self.N.find_pagerank(self.graph,
                                      nstart={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                       '6': 0.125, '71': 0.125, '8': 0.125})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'nstart parameter contains a node at zero-indexed position 6 that does not exist in the graph')

        result = self.N.find_pagerank(self.graph,
                                      dangling={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                              '6': 0.125, '71': 0.125, '18': 0.125})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'dangling parameter contains a node at zero-indexed position 6 that does not exist in the graph')

        result = self.N.find_pagerank(self.graph,
                                      dangling={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                '6': 0.125, '7': 0.125, '181': 0.125})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'dangling parameter contains a node at zero-indexed position 7 that does not exist in the graph')

        result = self.N.find_pagerank(self.graph,
                                      dangling={'111': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                                '6': 0.125, '7': 0.125, '181': 0.125})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'dangling parameter contains a node at zero-indexed position 0 that does not exist in the graph')

        result = self.N.find_pagerank(self.graph_05)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'edge value at [3][1] is not a node')

        result = self.N.find_pagerank(self.graph_06, weight=True)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'weight parameter specified but weights are not given in input graph')

    def test_find_eigenvector_centrality(self):

        # Invalid graph
        result = self.N.find_eigenvector_centrality(self.graph_05)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],'edge value at [3][1] is not a node')

        # nstart ... faulty node
        result = self.N.find_eigenvector_centrality(self.graph,
                                      nstart={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,
                                              '6': 0.125, '71': 0.125, '8': 0.125})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'nstart parameter contains a node at zero-indexed position 6 that does not exist in the graph')

        # nstart ... all zero values
        result = self.N.find_eigenvector_centrality(self.graph,
                                      nstart={'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
                                                       '6': 0, '7': 0, '8': 0})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],
                         'one nstart value should at lease be non-zero')

        # Default Test
        result = self.N.find_eigenvector_centrality(self.graph)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {'eigenvector_centrality': {'1': 0.35775018836999806, '2': 0.5298994260311778,
                                                                '3': 0.5298994260311778, '4': 0.35775018836999806,
                                                                '5': 0.2135666184274351, '6': 0.2135666184274351,
                                                                '7': 0.2135666184274351, '8': 0.2135666184274351}})

        # Weight parameter fallacy
        result = self.N.find_eigenvector_centrality(self.graph_06, weight=True)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'weight parameter specified but weights are not given in input graph')

        # Non Default Test ... undirected graph
        result = self.N.find_eigenvector_centrality(self.graph, max_iter=110, tol=1e-05,
                                                    nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                                                            '8': 1}, weight=True, directed=False)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {
            'eigenvector_centrality': {'1': 0.35774203080090017, '2': 0.5299019638339402, '3': 0.5299019638339402,
                                       '4': 0.3577420308009002, '5': 0.21357030238703748, '6': 0.21357030238703748,
                                       '7': 0.21357030238703748, '8': 0.21357030238703748}})

        # Non weighted Test ... directed graph ... in_out=False
        result = self.N.find_eigenvector_centrality(self.graph, max_iter=500, tol=1e-05,
                                                    nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                                                            '8': 1}, weight=True, directed=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {'eigenvector_centrality': {'1': 1.9935012399077745e-07, '2': 5.183103223760218e-05,
                                                                '3': 0.0067123180248934745, '4': 0.5773456687445266,
                                                                '5': 0.0067123180248934745, '6': 0.5772940370624132,
                                                                '7': 0.0067123180248934745, '8': 0.5772940370624132}})

        # Non weighted Test ... undirected graph ... in_out=True
        result = self.N.find_eigenvector_centrality(self.graph, max_iter=500, tol=1e-05,
                                                    nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                                                            '8': 1}, weight=True, directed=True,in_out=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2], {'eigenvector_centrality': {'1': 1.9935012399077745e-07, '2': 5.183103223760218e-05,
                                                                '3': 0.0067123180248934745, '4': 0.5773456687445266,
                                                                '5': 0.0067123180248934745, '6': 0.5772940370624132, '7': 0.0067123180248934745, '8': 0.5772940370624132}})

    def test_find_hits(self):
        # Invalid graph
        result = self.N.find_hits(self.graph_05)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'edge value at [3][1] is not a node')

        # nstart ... faulty node
        result = self.N.find_hits(self.graph,nstart={'1': 0.125, '2': 0.125, '3': 0.125, '4': 0.125, '5': 0.125,'6': 0.125, '71': 0.125, '8': 0.125})
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],'nstart parameter contains a node at zero-indexed position 6 that does not exist in the graph')


        # Default Test
        result = self.N.find_hits(self.graph_no_weights)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2]['hubs'],{'1': 0.13604957690850644, '2': 0.2015158583139189, '3': 0.2015158583139189, '4': 0.13604957690850644, '5': 0.08121728238878734, '6': 0.08121728238878734, '7': 0.08121728238878734, '8': 0.08121728238878734})
        self.assertEqual(result[2]['authorities'],{'1': 0.13604957688814256, '2': 0.2015158585243154, '3': 0.2015158585243154, '4': 0.13604957688814256, '5': 0.08121728229377104, '6': 0.08121728229377104, '7': 0.08121728229377104, '8': 0.08121728229377104})


        # # non Default Test
        result = self.N.find_hits(self.graph_no_weights,max_iter=110,tol=11.0e-7,nstart={'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1},normalized=False,directed=True)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 'success')
        self.assertEqual(result[2]['hubs'],{'1': 0.6180339887498948, '2': 5.309100041157175e-06, '3': 1.0, '4': 0.0, '5': 0.0, '6': 0.0, '7': 0.0, '8': 0.0})
        self.assertEqual(result[2]['authorities'],{'1': 0.0, '2': 0.38196601125010515, '3': 3.957169530458124e-06, '4': 1.0, '5': 3.957169530458124e-06, '6': 0.6180339887498948, '7': 3.957169530458124e-06, '8': 0.6180339887498948})



    def test_construct_graph(self):
        # Default Test
        result = self.N.construct_graph(self.graph)
        self.assertEqual(str(result.edges(data=True)),
                         "[('1', '2', {'weight': 3}), ('1', '4', {'weight': 4}), ('2', '3', {'weight': 5}),"
                         " ('2', '5', {'weight': 6}), ('2', '7', {'weight': 9}), ('3', '4', {'weight': 7}), "
                         "('3', '6', {'weight': 8}), ('3', '8', {'weight': 10})]")

        # Graph without nodes Test
        result = self.N.construct_graph(self.graph_01)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "'nodes'")
        self.assertEqual(result[2], {})

        # Graph without edges Test
        result = self.N.construct_graph(self.graph_02)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "'edges'")
        self.assertEqual(result[2], {})

    def test_check_graph_validity(self):
        # Graph without wrong number of weights
        result = self.cv.is_valid_graph(self.graph_04)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], 'the length of supplied edges and weights does not match')


if __name__ == '__main__':
    unittest.main()
