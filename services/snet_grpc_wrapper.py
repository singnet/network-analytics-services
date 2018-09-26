# Tested on python3.6

import grpc
from concurrent import futures
import time


import network_analytics_pb2
import network_analytics_pb2_grpc

import time
import bipartite_graphs
import logging

SLEEP_TIME = 86400 # One day


class NetworkAnalytics(network_analytics_pb2_grpc.NetowrkAnalyticsServicer):

    def BipartiteGraph(self,request,context):

        print('>>>>>>>>>>>>>>In endpoint BipartiteGraph')
        print(time.strftime("%c"))

        nodes = request.nodes
        edges = request.edges


        b = bipartite_graphs.BipartiteGraphs()

        res = network_analytics_pb2.BipartiteGraphResponse()

        try:

            nodes_in = {'bipartite_0':nodes.bipartite_0,'bipartite_1':nodes.bipartite_1}
            edges_in = {'edges': edges}

            ret = b.bipartite_graph(nodes_in, edges_in)

            res =  protofy(ret,res)

            if res.status:
                edges_res = []
                for edge_ret in ret[2]['edges']:
                    edges_res.append(network_analytics_pb2.Edge(edge=edge_ret))
                graph_res = network_analytics_pb2.BipartiteGraph()
                graph_res.bipartite_0 = res[2]['bipartite_0']
                graph_res.bipartite_1 = res[2]['bipartite_1']
                graph_res.edges = res[2]['edges']
                res.output = graph_res


            return res


        except Exception as e:

            logging.exception("message")

            return protofy([False, str(e)],res)



    def ProjectedGraph(self,request,context):

        pass


def protofy(ret,res):

    res.status = ret[0]
    res.message = ret[1]

    return res



def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_analytics_pb2_grpc.add_NetowrkAnalyticsServicer_to_server(NetworkAnalytics(), server)
    print('Starting server. Listening on port 5000.')
    server.add_insecure_port('127.0.0.1:5000')
    server.start()
    try:
        while True:
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        server.stop(0)



__end__ = '__end__'



if __name__ == '__main__':


    serve()

    pass










