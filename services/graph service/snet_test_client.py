# Tested on python3.6

import logging
import time

import grpc

import network_analytics_pb2
import network_analytics_pb2_grpc
from google.protobuf.json_format import MessageToJson, Parse

import subprocess
import yaml


def test_1():#Check MinNodesToRemove
    channel = grpc.insecure_channel('localhost:5000')
    stub = network_analytics_pb2_grpc.NetowrkAnalyticsStub(channel)

    graph = {
        "nodes": ['1','2','3','4','5'],
        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['4','6']]
        }
    source_node = '1'
    target_node = '6'
     
    edges_req = []
    for e in graph["edges"]:
        edges_req.append(network_analytics_pb2.Edge(edge=e))

    graph_in = network_analytics_pb2.Graph(nodes=graph["nodes"],edges=edges_req)

    graph_1 = network_analytics_pb2.MinNodeGraphRequest(graph=graph_in,source_node=source_node,target_node=target_node)

    response = stub.MinNodeGraph(graph_1)
    print(response.status)
    print(response.message)
    print(response.nodes_output)
    print(response.edges_output)

def test_2():#Check MostImportantNodes
    channel = grpc.insecure_channel('localhost:5000')
    stub = network_analytics_pb2_grpc.NetowrkAnalyticsStub(channel)

    graph = {
        "nodes": ['1','2','3','4','5','6','7','8'],
        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
        "weights": [3,4,5,6,7,8,9,10]
    }
    source_nodes = ['5','7']
    target_nodes = ['6']

     
    edges_req = []
    for e in graph["edges"]:
        edges_req.append(network_analytics_pb2.Edge(edge=e))

    if('weights' in graph):
        graph_in = network_analytics_pb2.Graph(nodes=graph["nodes"],edges=edges_req, weights=graph['weights'])
    else:    
        graph_in = network_analytics_pb2.Graph(nodes=graph["nodes"],edges=edges_req)


    graph_1 = network_analytics_pb2.MostImportantGraphRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=1)

    response = stub.MostImportantGraph(graph_1)
    print(response.status)
    print(response.message)
    print(response.node_betweenness_centrality)
    print(response.edge_betweenness_centrality)


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
     test_1()
     test_2()
 
