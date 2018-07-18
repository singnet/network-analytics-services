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

        # next: Make sure all edge labels are found in the respecitve bipartitions
        print('ret=',ret)



__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()

