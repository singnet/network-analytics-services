# Tested on python3.6

import unittest
import bipartite_graphs


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


__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()

