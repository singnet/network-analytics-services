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



        try:

            edges_list = []


            for edges_proto in edges:
                edges_list.append(list(edges_proto.edge))


            nodes_in = {"bipartite_0":list(nodes.bipartite_0),"bipartite_1":list(nodes.bipartite_1)}
            edges_in = {"edges": edges_list}

            ret = b.bipartite_graph(nodes_in, edges_in)

            resp = network_analytics_pb2.BipartiteGraphResponse(status=ret[0],message=ret[1])

            if resp.status:
                edges_resp = []
                for edge_ret in ret[2]["edges"]:
                    edges_resp.append(network_analytics_pb2.Edge(edge=edge_ret))

                graph_resp = network_analytics_pb2.BipartiteGraph(bipartite_0=ret[2]["bipartite_0"],bipartite_1=ret[2]["bipartite_1"],edges=edges_resp)


                resp = network_analytics_pb2.BipartiteGraphResponse(status=ret[0],message=ret[1],output=graph_resp)


            print('status:',resp.status)
            print('message:',resp.message)
            print('Waiting for next call on port 5000.')

            return resp


        except Exception as e:

            logging.exception("message")

            resp = network_analytics_pb2.BipartiteGraphResponse(status=False,message=str(e))

            print('status:', resp.status)
            print('message:', resp.message)
            print('Waiting for next call on port 5000.')

            return resp



    def ProjectedGraph(self,request,context):

        pass




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










