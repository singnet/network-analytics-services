# Tested on python3.6

import logging
import time

import grpc

import network_analytics_pb2
import network_analytics_pb2_grpc



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
    edge_2 = network_analytics_pb2.Edge(edge=['5','6'])

    edges_1= [edge_1,edge_2]
    # print("edge_1:")
    # print(type(edge_1.edge))


    # graph_in = network_analytics_pb2.BipartiteNodes(bipartite_0=input_0_0["bipartite_0"],bipartite_1=input_0_0["bipartite_1"])
    graph_in = network_analytics_pb2.BipartiteNodes(bipartite_1=input_0_0["bipartite_1"])


    graph_1 = network_analytics_pb2.BipartiteGraphRequest(nodes=graph_in,edges=edges_1)
    # graph1 = network_analytics_pb2.BipartiteGraphRequest(graph=)
    # graph1 = network_analytics_pb2.BipartiteGraphRequest(graph.nodes=input_0_0,graph.edges=input_0_1)

    response = stub.BipartiteGraph(graph_1)
    print(response.status)
    print(response.message)
    print(response.output)



if __name__ == '__main__':

    test_4()
    # test_1()
    # print('Using test_2')
    # time.sleep(2)
    # print('Hi')
    # test_1()
    # test_2()
    # test_3()
