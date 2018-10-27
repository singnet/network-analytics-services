# Tested on python3.6

import unittest
import jsonrpcclient


# You need to start running 'python3.6 snet_wrapper.py' first before running these tests

def jsonify_response(resp):
    return {'status': resp[0], 'message': resp[1], 'output': resp[2]}

class TestSnetWrapper(unittest.TestCase):



    def test_bipartite_graph(self):

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodess': {"bipartite_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edges": [[3, 8], [4, 7]]})

        self.assertEqual(resp,jsonify_response([False,'nodes parameter is required',{}]))



        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodes': {"bipartite_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edgess": [[3, 8], [4, 7]]})

        self.assertEqual(resp,jsonify_response([False,'edges parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodes': {"bipartitee_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edges": [[3, 8], [4, 7]]})

        self.assertEqual(resp,jsonify_response([False,'Parameter bipartite_0 does not exist in given input',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'bipartite_graph',
                                     {'nodes': {"bipartite_0": [8, 7], "bipartite_1": [3, 4]},
                                      "edges": [[3, 8], [4, 7]]})

        self.assertEqual(resp,jsonify_response([True,'success',{"bipartite_0": [8, 7], "bipartite_1": [3, 4],"edges": [[3, 8], [4, 7]]}]))




    def test_projected_graph(self):

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                     {"bipartite_graphh":{"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
                     "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
                                     'French', 'Hungarian', 'Lebanese', 'Greek'],
                     "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
                               ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
                               ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
                               ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
                               ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
                               ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
                               ['Charlie', 'Chinese']]},"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],"weight":"Newman"})

        self.assertEqual(resp,jsonify_response([False,'bipartite_graph parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                     {"bipartite_graph":{"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
                     "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
                                     'French', 'Hungarian', 'Lebanese', 'Greek'],
                     "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
                               ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
                               ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
                               ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
                               ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
                               ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
                               ['Charlie', 'Chinese']]},"nodess": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],"weight":"Newman"})


        self.assertEqual(resp,jsonify_response([False,'nodes parameter is required',{}]))


        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                     {"bipartite_graph":{"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
                     "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
                                     'French', 'Hungarian', 'Lebanese', 'Greek'],
                     "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
                               ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
                               ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
                               ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
                               ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
                               ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
                               ['Charlie', 'Chinese']]},"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],"weightt":"Newman"})

        self.assertEqual(resp,jsonify_response([False,'weight parameter is required',{}]))


        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                     {"bipartite_graph":{"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]},"nodes": [5, 5, 41],"weight":"none"})

        self.assertEqual(resp,jsonify_response([False,'Node element at zero-indexed position 2 is not contained in bipartite_1',{}]))


        ret = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                     {"bipartite_graph": {
                                         "bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue',
                                                         'Charlie'],
                                         "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese',
                                                         'Tapas', 'Thai',
                                                         'French', 'Hungarian', 'Lebanese', 'Greek'],
                                         "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'],
                                                   ['Goeff', 'American Diner'],
                                                   ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'],
                                                   ['Philip', 'Italian'],
                                                   ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'],
                                                   ['Sam', 'Italian'],
                                                   ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'],
                                                   ['Jane', 'French'],
                                                   ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'],
                                                   ['Sue', 'Tapas'],
                                                   ['Sue', 'Thai'], ['Charlie', 'American Diner'],
                                                   ['Charlie', 'Indian'],
                                                   ['Charlie', 'Chinese']]},
                                      "nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],
                                      "weight": "Newman"})


        resp = {}
        resp['edges'] = [['Charlie', 'Goeff'], ['Charlie', 'Sam'], ['Sue', 'Philip'], ['Sue', 'Fred'],
                         ['Philip', 'Fred'], ['Philip', 'Sam'], ['Goeff', 'Sam'], ['Sam', 'Jane'], ['Sam', 'Pam'],
                         ['Sam', 'Fred'], ['Jane', 'Pam']]
        resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        resp['weights'] = [2.5, 0.5, 2.5, 0.5, 0.5, 0.5, 1.0, 0.5, 1.5, 0.5, 0.5]

        self.assertCountEqual(resp['nodes'], ret['output']['nodes'])
        self.assertCountEqual(resp['weights'], ret['output']['weights'])
        self.assertEqual(True, ret['status'])
        self.assertEqual('success', ret['message'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret['output']['edges'])):
            self.assertIn(set(ret['output']['edges'][r]), set_list)
            set_list[set_list.index(set(ret['output']['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']), len(ret['output']['edges']))  # Just as a checkup; not needed


    def test_min_nodes_to_remove(self):

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'min_nodes_to_remove',
                                     {'edges':[[1,3]],'source_node':1,'target_node':3}
                                    )

        self.assertEqual(resp,jsonify_response([False,'nodes parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'min_nodes_to_remove',
                                     {'nodes':[1,2,3],'source_node':1,'target_node':3}
                                    )

        self.assertEqual(resp,jsonify_response([False,'edges parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'min_nodes_to_remove',
                                     {'nodes':[1,2,3],'edges':[[1,2],[3,4]],'target_node':3}
                                    )

        self.assertEqual(resp,jsonify_response([False,'source_node parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'min_nodes_to_remove',
                                     {'nodes':[1,2,3],'edges':[[1,2],[3,4]],'source_node':1}
                                    )

        self.assertEqual(resp,jsonify_response([False,'target_node parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'min_nodes_to_remove',
                                     {'nodes':[1,2,3,4,5],
                                      'edges':[[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[4,6]],
                                      'source_node': 1,
                                      'target_node': 6
                                      }
                                    )

        self.assertEqual(resp,jsonify_response([True, 'success', {'edges': [[4, 6], [3, 6]], 'nodes': [3, 4]}]))

    def test_most_important_nodes_edges(self):
        self.assertEqual.__self__.maxDiff = None

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'most_important_nodes_edges',
                                     {'edges':[[1,3]],'source_nodes':[1],'target_node':[3]}
                                    )

        self.assertEqual(resp,jsonify_response([False,'nodes parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'most_important_nodes_edges',
                                     {'nodes':[1,2,3],'source_node':[1],'target_node':[3]}
                                    )

        self.assertEqual(resp,jsonify_response([False,'edges parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'most_important_nodes_edges',
                                     {'nodes':[1,2,3],'edges':[[1,2],[3,4]],'target_nodes':[3]}
                                    )

        self.assertEqual(resp,jsonify_response([False,'source_nodes parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'most_important_nodes_edges',
                                     {'nodes':[1,2,3],'edges':[[1,2],[3,4]],'source_nodes':[1]}
                                    )

        self.assertEqual(resp,jsonify_response([False,'target_nodes parameter is required',{}]))

        resp = jsonrpcclient.request('http://127.0.0.1:5000', 'most_important_nodes_edges',
                                     {'nodes':[1,2,3,4,5,6,7,8],
                                      'edges':[[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],
                                      'source_nodes': [5,7],
                                      'target_nodes': [6]
                                      }
                                    )

        self.assertEqual(resp,jsonify_response([True, 'success', {'betweenness_centrality':{'3': 0.5833333333333333,'2': 0.16666666666666666,'4': 0.16666666666666666,'1': 0.08333333333333333}}]))


__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()

