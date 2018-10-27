# Tested on python3.6

import unittest
import bipartite_graphs
import networkx as nx


class TestBipartiteGraphs(unittest.TestCase):


    def test_bipartite_graph_validation(self):

        b = bipartite_graphs.BipartiteGraphs()

        input_0_0={"bipartite_1":['a'],"bipartite_2":[3,4]}
        input_0_1={"edges":[[2,3]]}
        ret = b.bipartite_graph(input_0_0,input_0_1)
        self.assertEqual([False,'Parameter bipartite_0 does not exist in given input',{}],ret)

        input_0_0={"bipartite_0":'a',"bipartite_1":[3,4]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Parameter bipartite_0 does not have an array value', {}], ret)

        input_0_0={"bipartite_0":['a'],"bipartite_2":[3,4]}
        ret = b.bipartite_graph(input_0_0,input_0_1)
        self.assertEqual([False,'Parameter bipartite_1 does not exist in given input',{}],ret)

        input_0_0 = {"bipartite_0": ['a'], "bipartite_1": 3}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Parameter bipartite_1 does not have an array value', {}], ret)

        input_0_0={"bipartite_0":['a'],"bipartite_1":[3,4]}
        input_0_1={"ledges":[[2,3]]}
        ret = b.bipartite_graph(input_0_0,input_0_1)
        self.assertEqual([False,'Parameter edges does not exist in given input',{}],ret)

        input_0_0 = {"bipartite_0": ['a'], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": 'non-array element'}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Parameter edges does not have an array value', {}], ret)

        input_0_0={"bipartite_0":[],"bipartite_1":[3,4]}
        input_0_1={"edges":[[2,3]]}
        ret = b.bipartite_graph(input_0_0,input_0_1)
        self.assertEqual([False,'Parameter bipartite_0 does not contain at least one element',{}],ret)

        input_0_0={"bipartite_0":[8],"bipartite_1":[]}
        input_0_1={"edges":[[2,3]]}
        ret = b.bipartite_graph(input_0_0,input_0_1)
        self.assertEqual([False,'Parameter bipartite_1 does not contain at least one element',{}],ret)

        input_0_0={"bipartite_0":[8],"bipartite_1":[3,4]}
        input_0_1={"edges":[]}
        ret = b.bipartite_graph(input_0_0,input_0_1)
        self.assertEqual([False,'Parameter edges does not contain at least one element',{}],ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 0 does not contain two edges', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[0,1],5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 is not an array', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": ['a',[0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 0 is not an array', {}],ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q','w'],'a',[0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 1 is not an array', {}],ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a','y'], 5, [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 is not an array', {}],ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], [5], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain two edges', {}],ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], [5,3,4,5], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain two edges', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], [], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain two edges', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], [5,'r','w'], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain two edges', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], ['','w'], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain at least one element', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], ['',None], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain at least one element', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], ['a',''], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain at least one element', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], [None,'1'], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain at least one element', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], ['a',None], [0, 1], 5]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Element of the input array edges at zero-indexed poistion 2 does not contain at least one element', {}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [['q', 'w'], ['a', 'y'], ['a', 9], [0, 1], [9,5]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 0 is not contained in either of the bipartitions',{}], ret)

        input_0_0 = {"bipartite_0": [8], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8, 'w'], ['a', 'y'], ['a', 9], [0, 1], [9,5]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 0 is not contained in either of the bipartitions',{}], ret)

        input_0_0 = {"bipartite_0": [8,7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8,3], [18,4], [9,5]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 1 is not contained in either of the bipartitions',{}], ret)

        input_0_0 = {"bipartite_0": [8,7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8,3], [8,41], [9,5]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 1 is not contained in either of the bipartitions',{}], ret)

        input_0_0 = {"bipartite_0": [8,7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8,3], [8,4], [8,5]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 2 is not contained in either of the bipartitions',{}], ret)

        input_0_0 = {"bipartite_0": [8,7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8,31]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 0 is not contained in either of the bipartitions',{}], ret)

        input_0_0 = {"bipartite_0": [8,7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8,3],[4,3]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 1 belongs to the wrong bipartition',{}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8, 3], [8, 3]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[8, 3], [8, 3]]}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8, 3], [7, 3]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[8, 3], [7, 3]]} ],ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8, 3], [7, 4]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[8, 3], [7, 4]]}],ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8], [3, 7]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8], [3, 7]]}],ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8], [4, 7]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8], [4, 7]]}],ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4]}
        input_0_1 = {"edges": [[3, 8], [4, 7]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4],"edges": [[3, 8], [4, 7]]}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4]}
        input_0_1 = {"edges": [[3, 8], [4, 7], [5, 6]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4],"edges": [[3, 8], [4, 7], [5, 6]]}], ret)

        input_0_0 = {"bipartite_0": [8,7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3,8],[3,4]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 1 belongs to the wrong bipartition',{}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8], [3,7], [3, 4]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 2 belongs to the wrong bipartition', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[8, 3], [7, 3], [4, 3]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 2 belongs to the wrong bipartition', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8], [3, 4], [3, 7]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 1 belongs to the wrong bipartition', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8], [3, 7]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8], [3, 7]]}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8], [3, 8]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8], [3, 8]]}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[7, 7]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 0 belongs to the wrong bipartition',{}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[7, 8]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([False, 'Edge element at zero-indexed position 0 belongs to the wrong bipartition',{}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8]]}], ret)

        input_0_0 = {"bipartite_0": [8, 7], "bipartite_1": [3, 4]}
        input_0_1 = {"edges": [[3, 8], [3, 8]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8], [3, 8]]}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4]}
        input_0_1 = {"edges": [[3, 8], [4, 7], [5, 6]]}
        ret = b.bipartite_graph(input_0_0, input_0_1)
        self.assertEqual([True,'success',{"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4],"edges":[[3, 8], [4, 7], [5, 6]]}], ret)

        # Seems quite extensive test for the moment. Might need to return in the future.

        print('ret=',ret)

    def test_projected_graph_validation(self):

        b = bipartite_graphs.BipartiteGraphs()

        input_0_0 = {"bipartite_2": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [8, 7]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False,'Parameter bipartite_0 does not exist in given input',{}],ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_2": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [8, 7]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Parameter bipartite_1 does not exist in given input', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "ledges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [8, 7]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Parameter edges does not exist in given input', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodess": [8, 7]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Parameter nodes does not exist in given input', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 3]]}
        input_0_1 = {"nodes": [8, 7]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Edge element at zero-indexed position 1 belongs to the wrong bipartition', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4],"edges":[[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": 8}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Parameter nodes does not contain an array', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": 'll'}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Parameter nodes does not contain an array', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": []}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Parameter nodes does not contain at least one element', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [[]]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 0 is not contained in either of the bipartitions', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [[8,41]]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 0 is not contained in either of the bipartitions', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [18, 41]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 0 is not contained in either of the bipartitions', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [8, 41]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 1 is not contained in bipartite_0', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [8, 41,77]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 1 is not contained in bipartite_0', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [8, 6, 41]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 2 is not contained in bipartite_0', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [5, 6, 4]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 1 is not contained in bipartite_1', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [5, 3, 41]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 2 is not contained in bipartite_1', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [5, 5, 41]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 2 is not contained in bipartite_1', {}], ret)

        input_0_0 = {"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [6, 5, 4]}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Node element at zero-indexed position 1 is not contained in bipartite_0', {}], ret)

        # Next: verify true conditions for each of the projection types ... then any other unit tests that need to be done

        input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'], "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai', 'French', 'Hungarian', 'Lebanese', 'Greek'], "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'], ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'], ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'], ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'], ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'], ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'], ['Charlie', 'Chinese']]}
        input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
        input_0_2 = 'none'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        resp = {}
        resp['edges'] = [['Pam', 'Sam'], ['Pam', 'Jane'], ['Charlie', 'Sam'], ['Charlie', 'Goeff'], ['Goeff', 'Sam'], ['Fred', 'Sam'], ['Fred', 'Philip'], ['Fred', 'Sue'], ['Sam', 'Philip'], ['Sam', 'Jane'], ['Sue', 'Philip']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = []

        self.assertEqual([True,'success'],ret[:2])
        self.assertCountEqual(resp['nodes'],ret[2]['nodes'])
        self.assertCountEqual(resp['weights'],ret[2]['weights'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret[2]['edges'])):
            self.assertIn(set(ret[2]['edges'][r]), set_list)
            set_list[set_list.index(set(ret[2]['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']), len(ret[2]['edges']))  # Just as a checkup; not needed

        input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'], "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai', 'French', 'Hungarian', 'Lebanese', 'Greek'], "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'], ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'], ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'], ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'], ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'], ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'], ['Charlie', 'Chinese']]}
        input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
        input_0_2 = 'multigraph'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        resp = {}
        resp['edges'] = [['Sam', 'Pam'], ['Sam', 'Jane'], ['Sam', 'Goeff'], ['Sam', 'Charlie'], ['Sam', 'Fred'], ['Sam', 'Philip'], ['Pam', 'Jane'], ['Pam', 'Jane'], ['Pam', 'Jane'], ['Goeff', 'Charlie'], ['Goeff', 'Charlie'], ['Goeff', 'Charlie'], ['Fred', 'Sue'], ['Fred', 'Sue'], ['Fred', 'Philip'], ['Fred', 'Philip'], ['Sue', 'Philip']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = []
        self.assertEqual([True,'success'],ret[:2])
        self.assertCountEqual(resp['nodes'],ret[2]['nodes'])
        self.assertCountEqual(resp['weights'],ret[2]['weights'])


        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret[2]['edges'])):
            self.assertIn(set(ret[2]['edges'][r]),set_list)
            set_list[set_list.index(set(ret[2]['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']),len(ret[2]['edges'])) # Just as a checkup; not needed

        input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'], "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai', 'French', 'Hungarian', 'Lebanese', 'Greek'], "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'], ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'], ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'], ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'], ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'], ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'], ['Charlie', 'Chinese']]}
        input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
        input_0_2 = 'degree'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        resp = {}
        resp['edges'] = [['Charlie', 'Goeff'], ['Charlie', 'Sam'], ['Sue', 'Philip'], ['Sue', 'Fred'], ['Philip', 'Fred'], ['Philip', 'Sam'], ['Goeff', 'Sam'], ['Sam', 'Jane'], ['Sam', 'Pam'], ['Sam', 'Fred'], ['Jane', 'Pam']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = [1, 3, 2, 1, 2, 1, 1, 1, 3, 1, 1]


        self.assertEqual([True,'success'],ret[:2])
        self.assertCountEqual(resp['nodes'],ret[2]['nodes'])
        self.assertCountEqual(resp['weights'],ret[2]['weights'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret[2]['edges'])):
            self.assertIn(set(ret[2]['edges'][r]),set_list)
            set_list[set_list.index(set(ret[2]['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']),len(ret[2]['edges'])) # Just as a checkup; not needed

        input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
                     "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
                                     'French', 'Hungarian', 'Lebanese', 'Greek'],
                     "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
                               ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
                               ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
                               ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
                               ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
                               ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
                               ['Charlie', 'Chinese']]}
        input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
        input_0_2 = 'degree_ratio'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        resp = {}
        resp['edges'] = [['Charlie', 'Goeff'], ['Charlie', 'Sam'], ['Sue', 'Philip'], ['Sue', 'Fred'],
                         ['Philip', 'Fred'], ['Philip', 'Sam'], ['Goeff', 'Sam'], ['Sam', 'Jane'], ['Sam', 'Pam'],
                         ['Sam', 'Fred'], ['Jane', 'Pam']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = [0.09090909090909091, 0.09090909090909091, 0.09090909090909091, 0.09090909090909091, 0.09090909090909091, 0.09090909090909091, 0.2727272727272727, 0.18181818181818182, 0.18181818181818182, 0.2727272727272727, 0.09090909090909091]

        self.assertEqual([True, 'success'], ret[:2])
        self.assertCountEqual(resp['nodes'], ret[2]['nodes'])
        self.assertCountEqual(resp['weights'], ret[2]['weights'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret[2]['edges'])):
            self.assertIn(set(ret[2]['edges'][r]), set_list)
            set_list[set_list.index(set(ret[2]['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']), len(ret[2]['edges']))  # Just as a checkup; not needed

        input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
                     "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
                                     'French', 'Hungarian', 'Lebanese', 'Greek'],
                     "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
                               ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
                               ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
                               ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
                               ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
                               ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
                               ['Charlie', 'Chinese']]}
        input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
        input_0_2 = 'Newman'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        resp = {}
        resp['edges'] = [['Charlie', 'Goeff'], ['Charlie', 'Sam'], ['Sue', 'Philip'], ['Sue', 'Fred'],
                         ['Philip', 'Fred'], ['Philip', 'Sam'], ['Goeff', 'Sam'], ['Sam', 'Jane'], ['Sam', 'Pam'],
                         ['Sam', 'Fred'], ['Jane', 'Pam']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = [2.5, 0.5, 2.5, 0.5, 0.5, 0.5, 1.0, 0.5, 1.5, 0.5, 0.5]

        self.assertEqual([True, 'success'], ret[:2])
        self.assertCountEqual(resp['nodes'], ret[2]['nodes'])
        self.assertCountEqual(resp['weights'], ret[2]['weights'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret[2]['edges'])):
            self.assertIn(set(ret[2]['edges'][r]), set_list)
            set_list[set_list.index(set(ret[2]['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']), len(ret[2]['edges']))  # Just as a checkup; not needed


        input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
                     "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
                                     'French', 'Hungarian', 'Lebanese', 'Greek'],
                     "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
                               ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
                               ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
                               ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
                               ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
                               ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
                               ['Charlie', 'Chinese']]}
        input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
        input_0_2 = 'Jaccard'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        resp = {}
        resp['edges'] = [['Charlie', 'Goeff'], ['Charlie', 'Sam'], ['Sue', 'Philip'], ['Sue', 'Fred'],
                         ['Philip', 'Fred'], ['Philip', 'Sam'], ['Goeff', 'Sam'], ['Sam', 'Jane'], ['Sam', 'Pam'],
                         ['Sam', 'Fred'], ['Jane', 'Pam']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = [0.2, 0.5, 0.2, 1.0, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 1.0]

        self.assertEqual([True, 'success'], ret[:2])
        self.assertCountEqual(resp['nodes'], ret[2]['nodes'])
        self.assertCountEqual(resp['weights'], ret[2]['weights'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret[2]['edges'])):
            self.assertIn(set(ret[2]['edges'][r]), set_list)
            set_list[set_list.index(set(ret[2]['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']), len(ret[2]['edges']))  # Just as a checkup; not needed

        input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
                     "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
                                     'French', 'Hungarian', 'Lebanese', 'Greek'],
                     "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
                               ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
                               ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
                               ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
                               ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
                               ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
                               ['Charlie', 'Chinese']]}
        input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
        input_0_2 = 'Jaccard_modified'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        resp = {}
        resp['edges'] = [['Charlie', 'Goeff'], ['Charlie', 'Sam'], ['Sue', 'Philip'], ['Sue', 'Fred'],
                         ['Philip', 'Fred'], ['Philip', 'Sam'], ['Goeff', 'Sam'], ['Sam', 'Jane'], ['Sam', 'Pam'],
                         ['Sam', 'Fred'], ['Jane', 'Pam']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = [0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.6666666666666666, 0.6666666666666666, 1.0, 0.3333333333333333, 1.0]

        self.assertEqual([True, 'success'], ret[:2])
        self.assertCountEqual(resp['nodes'], ret[2]['nodes'])
        self.assertCountEqual(resp['weights'], ret[2]['weights'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret[2]['edges'])):
            self.assertIn(set(ret[2]['edges'][r]), set_list)
            set_list[set_list.index(set(ret[2]['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']), len(ret[2]['edges']))  # Just as a checkup; not needed

        input_0_0 = {"bipartite_0": [8, 7, 6,10,12,13], "bipartite_1": [5, 3, 4,1,2,3],"edges":[[3, 8], [4, 7], [5, 6], [3, 7]]}
        input_0_1 = {"nodes": [8, 7]}
        input_0_2 = 'false_logic'
        ret = b.projected_graph(input_0_0, input_0_1, input_0_2)
        self.assertEqual([False, 'Unkown weighting logic specified', {}], ret)

        # input_0_0 = {"bipartite_0": [8, 7, 6,10,12,13], "bipartite_1": [5, 3, 4,1,2,3],"edges":[[3, 8], [4, 7], [5, 6], [3, 7]]}
        # input_0_1 = {"nodes": [8, 7]}
        # input_0_2 = 'none'
        # ret = b.projected_graph(input_0_0, input_0_1, input_0_2)

        print('ret=', ret)

    def test_min_nodes_to_remove(self):

        b = bipartite_graphs.BipartiteGraphs()

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
        self.assertEqual([False, 'node 4 doesn’t exist in the graph',{}],ret)

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

        b = bipartite_graphs.BipartiteGraphs()

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
        self.assertEqual([False, 'the length of supplied edges and weights does not much',{}],ret)

        graph = {
            "nodes": [1,2],
            "edges": [[1,2]],
            "weights": [3]
        }

        ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes, 17)
        self.assertEqual([False, 'type can only be 0 or 1',{}],ret)

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
        self.assertEqual([False, 'node 10 doesn’t exist in the graph',{}],ret)

        source_nodes = [5,7]
        target_nodes = [6,11]

        ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'node 11 doesn’t exist in the graph',{}],ret)

        graph = {
            "nodes": [1,2,3,4,5,6,7,8,20],
            "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]]
        }
        source_nodes = [5,7,20]
        target_nodes = [6]

        ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
        self.assertEqual([False, 'no path exists from node 20 to node 6', {}],ret)


        graph = {
            "nodes": [1,2,3,4,5,6,7,8],
            "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]]
        }
        source_nodes = [5,7]
        target_nodes = [6]

        ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes)
        self.assertEqual([True, 'success', {'betweenness_centrality':{3: 0.5833333333333333,2: 0.16666666666666666,4: 0.16666666666666666,1: 0.08333333333333333}}],ret)

        graph = {
            "nodes": [1,2,3,4,5,6,7,8],
            "edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],
            "weights": [3,4,5,6,7,8,9,10]
        }
        source_nodes = [5,7]
        target_nodes = [6]

        ret = b.most_important_nodes_edges(graph, source_nodes, target_nodes, 1)
        self.assertEqual([True, 'success', {'betweenness_centrality':{(2, 3): 0.125, (1, 2): 0.07500000000000001, (3, 8): 0.05, (1, 4): 0.025, (3, 4): 0.025}}],ret)

__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()

