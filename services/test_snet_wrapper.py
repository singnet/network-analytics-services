# Tested on python3.6

import unittest
import jsonrpcclient


# You need to start running 'python3.6 snet_wrapper.py' first before running these tests

class TestSnetWrapper(unittest.TestCase):

    def test_bipartite_graph(self):


        try:
            resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodess': {"bipartite_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edges": [[3, 8], [4, 7]]})
        except Exception as e:

            self.assertEqual('nodes parameter is required', str(e))



        try:
            resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodes': {"bipartite_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edgess": [[3, 8], [4, 7]]})
        except Exception as e:

            self.assertEqual('edges parameter is required', str(e))

        try:
            resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodes': {"bipartitee_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edges": [[3, 8], [4, 7]]})
        except Exception as e:

            self.assertEqual('Parameter bipartite_0 does not exist in given input', str(e))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodes': {"bipartite_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edges": [[3, 8], [4, 7]]})

        self.assertEqual(resp,{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8], [4, 7]]})




    def test_projected_graph(self):

        pass





__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()

