# Tested on python3.6

import grpc
from concurrent import futures
import time
import logging

import bipartite_graphs
from service_spec_bipartite import network_analytics_bipartite_pb2
from service_spec_bipartite import network_analytics_bipartite_pb2_grpc

SLEEP_TIME = 86400 # One day


class NetworkAnalyticsBipartite(network_analytics_bipartite_pb2_grpc.NetworkAnalyticsBipartiteServicer):

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

            resp = network_analytics_bipartite_pb2.BipartiteGraphResponse(status=ret[0], message=ret[1])

            if resp.status:
                edges_resp = []
                for edge_ret in ret[2]["edges"]:
                    edges_resp.append(network_analytics_bipartite_pb2.Edge(edge=edge_ret))

                graph_resp = network_analytics_bipartite_pb2.BipartiteGraph(bipartite_0=ret[2]["bipartite_0"], bipartite_1=ret[2]["bipartite_1"], edges=edges_resp)


                resp = network_analytics_bipartite_pb2.BipartiteGraphResponse(status=ret[0], message=ret[1], output=graph_resp)

            else:

                print(time.strftime("%c"))
                print('Waiting for next call on port 5000.')

                raise grpc.RpcError(grpc.StatusCode.UNKNOWN, ret[1])

            print('status:',resp.status)
            print('message:',resp.message)
            print(time.strftime("%c"))
            print('Waiting for next call on port 5000.')

            return resp


        except Exception as e:

            logging.exception("message")

            print(time.strftime("%c"))
            print('Waiting for next call on port 5000.')

            raise grpc.RpcError(grpc.StatusCode.UNKNOWN, str(e))




    def ProjectedGraph(self,request,context):

        print('>>>>>>>>>>>>>>In endpoint ProjectedGraph')
        print(time.strftime("%c"))

        bipartite_graph = request.graph
        nodes = request.nodes
        weight = request.weight


        b = bipartite_graphs.BipartiteGraphs()

        try:

            edges_list = []


            for edges_proto in bipartite_graph.edges:
                edges_list.append(list(edges_proto.edge))

            bipartite_graph_in = {"bipartite_0":list(bipartite_graph.bipartite_0),"bipartite_1":list(bipartite_graph.bipartite_1),"edges":edges_list}
            nodes_in = {"nodes": list(nodes)}

            ret = b.projected_graph(bipartite_graph_in, nodes_in, weight)

            resp = network_analytics_bipartite_pb2.ProjecetedGraphResponse(status=ret[0], message=ret[1])

            if resp.status:
                edges_resp = []
                for edge_ret in ret[2]["edges"]:
                    edges_resp.append(network_analytics_bipartite_pb2.Edge(edge=edge_ret))

                graph_resp = network_analytics_bipartite_pb2.Graph(nodes=ret[2]["nodes"], edges=edges_resp, weights=ret[2]["weights"])


                resp = network_analytics_bipartite_pb2.ProjecetedGraphResponse(status=ret[0], message=ret[1], output=graph_resp)

            else:

                print(time.strftime("%c"))
                print('Waiting for next call on port 5000.')

                raise grpc.RpcError(grpc.StatusCode.UNKNOWN, ret[1])

            print('status:',resp.status)
            print('message:',resp.message)
            print(time.strftime("%c"))
            print('Waiting for next call on port 5000.')

            return resp


        except Exception as e:

            logging.exception("message")

            print(time.strftime("%c"))
            print('Waiting for next call on port 5000.')

            raise grpc.RpcError(grpc.StatusCode.UNKNOWN, str(e))



def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_analytics_bipartite_pb2_grpc.add_NetworkAnalyticsBipartiteServicer_to_server(NetworkAnalyticsBipartite(), server)
    print('Starting server. Listening on port 5000.')
    server.add_insecure_port('127.0.0.1:5000')
    server.start()
    try:
        while True:
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        server.stop(0)

def serve_test():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_analytics_bipartite_pb2_grpc.add_NetworkAnalyticsBipartiteServicer_to_server(NetworkAnalyticsBipartite(), server)
    print('Starting server. Listening on port 5000.')
    server.add_insecure_port('127.0.0.1:5000')
    return server




__end__ = '__end__'



if __name__ == '__main__':


    serve()

    pass










