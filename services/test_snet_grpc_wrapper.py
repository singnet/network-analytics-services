# Tested on python3.6

import unittest
import grpc
import network_analytics_pb2
import network_analytics_pb2_grpc


# You need to start running 'python3.6 snet_grpc_wrapper.py' first before running these tests



class TestSnetWrapper(unittest.TestCase):


    def test_BipartiteGraph(self):

        channel = grpc.insecure_channel('localhost:5000')
        stub = network_analytics_pb2_grpc.NetowrkAnalyticsStub(channel)


        edges_list = [['3', '8'], ['4', '7']]
        edges = []
        for e in edges_list:
            edges.append(network_analytics_pb2.Edge(edge=e))
        bgr = network_analytics_pb2.BipartiteGraphRequest(edges=edges)
        resp =stub.BipartiteGraph(bgr)
        expected = network_analytics_pb2.BipartiteGraphResponse(status=False,message='Parameter bipartite_0 does not contain at least one element')

        self.assertEqual(resp,expected)

        nodes_list = {"bipartite_0": ['8', '7'], "bipartite_1": ['3', '4']}
        nodes = network_analytics_pb2.BipartiteNodes(bipartite_0=nodes_list["bipartite_0"],bipartite_1=nodes_list["bipartite_1"])
        bgr = network_analytics_pb2.BipartiteGraphRequest(nodes=nodes)
        resp =stub.BipartiteGraph(bgr)
        expected = network_analytics_pb2.BipartiteGraphResponse(status=False,message='Parameter edges does not contain at least one element')

        self.assertEqual(resp,expected)

        nodes_list = {"bipartite_1": ['3', '4']}
        edges_list = [['3', '8'], ['4', '7']]
        nodes = network_analytics_pb2.BipartiteNodes(bipartite_1=nodes_list["bipartite_1"])
        edges = []
        for e in edges_list:
            edges.append(network_analytics_pb2.Edge(edge=e))
        bgr = network_analytics_pb2.BipartiteGraphRequest(nodes=nodes,edges=edges)
        resp =stub.BipartiteGraph(bgr)
        expected = network_analytics_pb2.BipartiteGraphResponse(status=False,message='Parameter bipartite_0 does not contain at least one element')

        self.assertEqual(resp,expected)


        nodes_list = {"bipartite_0": ['8', '7'], "bipartite_1": ['3', '4']}
        edges_list = [['3', '8'], ['4', '7']]
        nodes = network_analytics_pb2.BipartiteNodes(bipartite_0=nodes_list["bipartite_0"],bipartite_1=nodes_list["bipartite_1"])
        edges = []
        for e in edges_list:
            edges.append(network_analytics_pb2.Edge(edge=e))
        bgr = network_analytics_pb2.BipartiteGraphRequest(nodes=nodes,edges=edges)
        resp =stub.BipartiteGraph(bgr)
        expected_graph = network_analytics_pb2.BipartiteGraph(bipartite_0=['8', '7'],bipartite_1=['3', '4'],edges=edges)
        expected = network_analytics_pb2.BipartiteGraphResponse(status=True,message='success',output=expected_graph)

        self.assertEqual(resp,expected)




    def test_ProjectedGraph(self):

        # resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
        #                              {"bipartite_graphh":{"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
        #              "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
        #                              'French', 'Hungarian', 'Lebanese', 'Greek'],
        #              "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
        #                        ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
        #                        ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
        #                        ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
        #                        ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
        #                        ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
        #                        ['Charlie', 'Chinese']]},"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],"weight":"Newman"})
        #
        # self.assertEqual(resp,jsonify_response([False,'bipartite_graph parameter is required',{}]))
        #
        # resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
        #                              {"bipartite_graph":{"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
        #              "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
        #                              'French', 'Hungarian', 'Lebanese', 'Greek'],
        #              "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
        #                        ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
        #                        ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
        #                        ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
        #                        ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
        #                        ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
        #                        ['Charlie', 'Chinese']]},"nodess": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],"weight":"Newman"})
        #
        #
        # self.assertEqual(resp,jsonify_response([False,'nodes parameter is required',{}]))
        #
        #
        # resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
        #                              {"bipartite_graph":{"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
        #              "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai',
        #                              'French', 'Hungarian', 'Lebanese', 'Greek'],
        #              "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
        #                        ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
        #                        ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
        #                        ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
        #                        ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
        #                        ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
        #                        ['Charlie', 'Chinese']]},"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],"weightt":"Newman"})
        #
        # self.assertEqual(resp,jsonify_response([False,'weight parameter is required',{}]))
        #
        #
        # resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
        #                              {"bipartite_graph":{"bipartite_0": [8, 7, 6], "bipartite_1": [5, 3, 4], "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]},"nodes": [5, 5, 41],"weight":"none"})
        #
        # self.assertEqual(resp,jsonify_response([False,'Node element at zero-indexed position 2 is not contained in bipartite_1',{}]))
        #
        #
        # ret = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
        #                              {"bipartite_graph": {
        #                                  "bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue',
        #                                                  'Charlie'],
        #                                  "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese',
        #                                                  'Tapas', 'Thai',
        #                                                  'French', 'Hungarian', 'Lebanese', 'Greek'],
        #                                  "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'],
        #                                            ['Goeff', 'American Diner'],
        #                                            ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'],
        #                                            ['Philip', 'Italian'],
        #                                            ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'],
        #                                            ['Sam', 'Italian'],
        #                                            ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'],
        #                                            ['Jane', 'French'],
        #                                            ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'],
        #                                            ['Sue', 'Tapas'],
        #                                            ['Sue', 'Thai'], ['Charlie', 'American Diner'],
        #                                            ['Charlie', 'Indian'],
        #                                            ['Charlie', 'Chinese']]},
        #                               "nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane'],
        #                               "weight": "Newman"})
        #
        #
        # resp = {}
        # resp['edges'] = [['Charlie', 'Goeff'], ['Charlie', 'Sam'], ['Sue', 'Philip'], ['Sue', 'Fred'],
        #                  ['Philip', 'Fred'], ['Philip', 'Sam'], ['Goeff', 'Sam'], ['Sam', 'Jane'], ['Sam', 'Pam'],
        #                  ['Sam', 'Fred'], ['Jane', 'Pam']]
        # resp['nodes'] = ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']
        # resp['weights'] = [2.5, 0.5, 2.5, 0.5, 0.5, 0.5, 1.0, 0.5, 1.5, 0.5, 0.5]
        #
        # self.assertCountEqual(resp['nodes'], ret['output']['nodes'])
        # self.assertCountEqual(resp['weights'], ret['output']['weights'])
        # self.assertEqual(True, ret['status'])
        # self.assertEqual('success', ret['message'])
        #
        # set_list = []
        # for s in resp['edges']:
        #     set_list.append(set(s))
        # for r in range(len(ret['output']['edges'])):
        #     self.assertIn(set(ret['output']['edges'][r]), set_list)
        #     set_list[set_list.index(set(ret['output']['edges'][r]))] = ''
        # self.assertEqual(len(resp['edges']), len(ret['output']['edges']))  # Just as a checkup; not needed

        pass

__end__ = '__end__'

if __name__ == '__main__':
    unittest.main()

