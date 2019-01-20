# Tested on python3.6

import logging

import grpc

from service_spec_bipartite import network_analytics_bipartite_pb2_grpc, network_analytics_bipartite_pb2

import subprocess
import yaml



def test_1():

    import jsonrpcclient

    resp = jsonrpcclient.request('http://127.0.0.1:5000','bipartite_graph',{'nodes':{"bipartite_0": [8, 7], "bipartite_1": [3, 4]},"edges": [[3, 8], [4, 7]]})
    # resp = jsonrpcclient.request('http://159.69.56.49:35000','bipartite_graph',{'nodes':{"bipartite_0": [8, 7], "bipartite_1": [3, 4]},"edges": [[3, 8], [4, 7]]})

    print(resp)





def test_2():

    import aiohttp
    import asyncio
    from jsonrpcclient.aiohttp_client import aiohttpClient

    async def main(loop):
        async with aiohttp.ClientSession(loop=loop) as session:
            client = aiohttpClient(session, 'http://127.0.0.1:5000')
            print('hi')

            try:
                response = await client.request('bipartite_graph',{'noddes':{"bipartite_0": [8, 7], "bipartite_1": [3, 4]},"edges": [[3, 8], [4, 7]]})
                print(response)

            except Exception as e:

                logging.exception("message")

                print('error message:',str(e))



    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

def test_3():
    import jsonrpcclient

    input_0_0 = {"bipartite_0": [8, 7, 6, 10, 12, 13], "bipartite_1": [5, 3, 4, 1, 2, 3],
                 "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
    input_0_1 = [8, 7]
    input_0_2 = 'none'

    resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                 {'bipartite_graph':input_0_0, "nodes": input_0_1, 'weight':'kk'})



def test_4():
    channel = grpc.insecure_channel('localhost:5000')
    stub = network_analytics_pb2_grpc.NetowrkAnalyticsStub(channel)

    input_0_0 = {"bipartite_0": ['8', '7', '6'], "bipartite_1": ['5', '3', '4']}
    input_0_1 = {"edges": [[3, 8], [4, 7], [5, 6]]}

    edgess = [['3', '8'], ['4', '7'], ['5', '6']]
    i = 1

    edge_1 = network_analytics_pb2.Edge(edge=edgess[i])
    edge_2 = network_analytics_pb2.Edge(edge=['5', '6'])

    edges_1= [edge_1,edge_2]
    # print("edge_1:")
    # print(type(edge_1.edge))


    graph_in = network_analytics_pb2.BipartiteNodes(bipartite_0=input_0_0["bipartite_0"], bipartite_1=input_0_0["bipartite_1"])
    # graph_in = network_analytics_pb2.BipartiteNodes(bipartite_1=input_0_0["bipartite_1"])


    graph_1 = network_analytics_pb2.BipartiteGraphRequest(nodes=graph_in, edges=edges_1)
    # graph1 = network_analytics_pb2.BipartiteGraphRequest(graph=)
    # graph1 = network_analytics_pb2.BipartiteGraphRequest(graph.nodes=input_0_0,graph.edges=input_0_1)

    response = stub.BipartiteGraph(graph_1)
    print(response.status)
    print(response.message)
    print(response.output)

def test_5():
    channel = grpc.insecure_channel('localhost:5000')
    stub = network_analytics_pb2_grpc.NetowrkAnalyticsStub(channel)

    input_0_0 = {"bipartite_0": ['8', '7', '6', '10', '12', '13'], "bipartite_1": ['5', '3', '4', '1', '2', '3'],
                 "edges": [['3', '8'], ['4', '7'], ['5', '6'], ['3', '7']]}
    input_0_1 = {"nodes":['8', '7']}
    input_0_2 = 'none'

    # input_0_0 = {"bipartite_0": ['Pam', 'Goeff', 'Philip', 'Sam', 'Fred', 'Jane', 'Sue', 'Charlie'],
    #              "bipartite_1": ['American Diner', 'Sushi', 'Italian', 'Indian', 'Chinese', 'Tapas', 'Thai', 'French',
    #                              'Hungarian', 'Lebanese', 'Greek'],
    #              "edges": [['Pam', 'French'], ['Pam', 'Hungarian'], ['Pam', 'Sushi'], ['Goeff', 'American Diner'],
    #                        ['Goeff', 'Indian'], ['Goeff', 'Chinese'], ['Philip', 'Lebanese'], ['Philip', 'Italian'],
    #                        ['Philip', 'Tapas'], ['Sam', 'American Diner'], ['Sam', 'Sushi'], ['Sam', 'Italian'],
    #                        ['Fred', 'Italian'], ['Fred', 'Tapas'], ['Fred', 'Thai'], ['Jane', 'French'],
    #                        ['Jane', 'Hungarian'], ['Jane', 'Sushi'], ['Sue', 'Greek'], ['Sue', 'Tapas'],
    #                        ['Sue', 'Thai'], ['Charlie', 'American Diner'], ['Charlie', 'Indian'],
    #                        ['Charlie', 'Chinese']]}
    # input_0_1 = {"nodes": ['Pam', 'Charlie', 'Goeff', 'Fred', 'Sam', 'Sue', 'Philip', 'Jane']}
    # input_0_2 = 'degree'

    edges_req = []
    for e in input_0_0["edges"]:
        edges_req.append(network_analytics_pb2.Edge(edge=e))


    graph_in = network_analytics_pb2.BipartiteGraph(bipartite_0=input_0_0["bipartite_0"], bipartite_1=input_0_0["bipartite_1"], edges=edges_req)


    graph_1 = network_analytics_pb2.ProjecetedGraphRequest(graph=graph_in, nodes=input_0_1["nodes"], weight=input_0_2)

    response = stub.ProjectedGraph(graph_1)
    print(response.status)
    print(response.message)
    print(response.output)



def test_6():

    endpoint = "159.69.56.49:2222" # NetworkAnalyticsServices deployed to Kovan
    channel = grpc.insecure_channel(endpoint)
    stub = network_analytics_pb2_grpc.NetowrkAnalyticsStub(channel)

    job_address = ''
    job_signature = ''

    nodes_list = {"bipartite_0": ['8', '7'], "bipartite_1": ['3', '4']}
    edges_list = [['3', '8'], ['4', '7']]
    nodes = network_analytics_pb2.BipartiteNodes(bipartite_0=nodes_list["bipartite_0"],
                                                 bipartite_1=nodes_list["bipartite_1"])
    edges = []
    for e in edges_list:
        edges.append(network_analytics_pb2.Edge(edge=e))

    response = stub.BipartiteGraph(network_analytics_pb2.BipartiteGraphRequest(nodes=nodes, edges=edges), metadata=[("snet-job-address", job_address), ("snet-job-signature", job_signature)])
    print(response.status)
    print(response.message)
    print(response.output)

def generate_call_credentials():
    agent_address = "0xb57B4c70379E84CD8d42a867cF326d5e0743E11d"  # NetworkAnalyticsServices deployed to Kovan
    result = subprocess.check_output(["snet", "agent", "--at", agent_address, "create-jobs", "--funded", "--signed", "--no-confirm", "--max-price","3"])
    job = yaml.load(result)["jobs"][0]
    job_address = job["job_address"]
    job_signature = job["job_signature"]
    print("job_address------------------------------")
    print(job_address)
    print("job_signature----------------------------")
    print(job_signature)


if __name__ == '__main__':

    # generate_call_credentials()
    #test_6()
    test_5()
    test_4()
    # test_1()
    # print('Using test_2')
    # time.sleep(2)
    # print('Hi')
    # test_1()
    # test_2()
    # test_3()
