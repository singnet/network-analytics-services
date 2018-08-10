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

        try:
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
        except Exception as e:

            self.assertEqual('bipartite_graph parameter is required', str(e))

        try:
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
                               ['Charlie', 'Chinese']]},"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],"weight":"Newman"})
        except Exception as e:

            self.assertEqual('nodes parameter is required', str(e))


        try:
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
        except Exception as e:

            self.assertEqual('weight parameter is required', str(e))


        try:
            resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                     {"bipartite_graph":{"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]},"nodes": [5, 5, 41],"weight":"none"})
        except Exception as e:

            self.assertEqual('Node element at zero-indexed position 2 is not contained in bipartite_1', str(e))


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

        self.assertCountEqual(resp['nodes'], ret['nodes'])
        self.assertCountEqual(resp['weights'], ret['weights'])

        set_list = []
        for s in resp['edges']:
            set_list.append(set(s))
        for r in range(len(ret['edges'])):
            self.assertIn(set(ret['edges'][r]), set_list)
            set_list[set_list.index(set(ret['edges'][r]))] = ''
        self.assertEqual(len(resp['edges']), len(ret['edges']))  # Just as a checkup; not needed


__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()

