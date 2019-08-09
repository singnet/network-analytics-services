# Tested on python3.6

import logging


import multiprocessing as mp
import grpc
import pem
import time
import datetime

from service_spec_node_importance import network_analytics_node_importance_pb2
from service_spec_node_importance import network_analytics_node_importance_pb2_grpc

import subprocess
import yaml



def multi_pro_sample():

    output = mp.Queue()

    processes = [mp.Process(target=f, args=[output]) for x in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]

    print(results)

def f(output):
    print(3)
    output.put(4)


def multi_pro(num_requests):

    output = mp.Queue()

    processes = [mp.Process(target=find_central_nodes(output), args=[output]) for x in range(num_requests)]


    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]

    print(results)
    summed = sum([t[0] for t in results])
    print(summed , '/' , len(results))



def find_central_nodes(output):


    try:
        channel = grpc.insecure_channel('tz-services-1.snet.sh:2234')
        # channel = grpc.insecure_channel('localhost:5001')
        stub = network_analytics_node_importance_pb2_grpc.NetworkAnalyticsNodeImportanceStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, 5, 6, 7, 8, 9, 10]
        }


        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_node_importance_pb2.Edge(edge=e))

        graph_in = network_analytics_node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req)



        center_req = network_analytics_node_importance_pb2.CentralNodeRequest(graph=graph_in)
        resp = stub.CentralNodes(center_req)

        output.put((1,resp.message))

    except  Exception as e:
        output.put((0,str(e)))




if __name__ == '__main__':

    start_time = time.time()

    multi_pro(1)


    # find_central_nodes()

    end_time = time.time()

    print('Testing took ' + str(((end_time - start_time) )) + ' seconds.')
    print('Testing took ' + str(((end_time - start_time) / 60)) + ' minutes.')

    pass
