# Tested on python3.6

import grpc
from concurrent import futures
import time
import logging

from service_spec_robustness import network_analytics_robustness_pb2
from service_spec_robustness import network_analytics_robustness_pb2_grpc

import robustness



SLEEP_TIME = 86400 # One day


class NetworkAnalyticsRobustness(network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessServicer):

    def MinNodesToRemove(self, request, context):

        print('>>>>>>>>>>>>>>In endpoint MinNodesToRemove')
        print(time.strftime("%c"))

        graph = request.graph
        source_nodes = request.source_node
        target_nodes = request.target_node


        g = robustness.Robustness()

        try:

            edges_list = []


            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            
        
            graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
            source_nodes_in = str(source_nodes)
            target_nodes_in = str(target_nodes)


            ret = g.min_nodes_to_remove(graph_in,source_nodes_in,target_nodes_in)    

            
            resp = network_analytics_robustness_pb2.MinNodesToRemoveResponse(status=ret[0],message=ret[1])

            if resp.status:
                nodes_resp=ret[2]["nodes"]
                edges_resp = []
                for edge_ret in ret[2]["edges"]:
                    edges_resp.append(network_analytics_robustness_pb2.Edge(edge=edge_ret))

                resp = network_analytics_robustness_pb2.MinNodesToRemoveResponse(status=ret[0],message=ret[1],nodes_output=nodes_resp,edges_output=edges_resp)

            else:

                print(time.strftime("%c"))
                print('Waiting for next call on port 5002.')

                raise grpc.RpcError(grpc.StatusCode.UNKNOWN, ret[1])



            print('status:',resp.status)
            print('message:',resp.message)
            print(time.strftime("%c"))
            print('Waiting for next call on port 5002.')

            return resp


        except Exception as e:

            logging.exception("message")

            print(time.strftime("%c"))
            print('Waiting for next call on port 5002.')

            raise grpc.RpcError(grpc.StatusCode.UNKNOWN, str(e))



   
    def MostImportantNodesEdgesSubset(self, request, context):

        print('>>>>>>>>>>>>>>In endpoint MostImportantNodesEdgesSubset')
        print(time.strftime("%c"))

        graph = request.graph
        source_nodes = request.source_nodes
        target_nodes = request.target_nodes
        T = request.Type



        g = robustness.Robustness()

        try:

            edges_list = []


            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))

            weights_list = list(graph.weights)

            nodes_list = list(graph.nodes)

            if len(weights_list) > 0:
                graph_in = {"nodes": nodes_list, "edges": edges_list, "weights": weights_list}
            else:
                graph_in = {"nodes": nodes_list, "edges": edges_list}

            source_nodes_in = list(source_nodes)
            target_nodes_in = list(target_nodes)


            ret = g.most_important_nodes_edges_subset(graph_in, source_nodes_in, target_nodes_in, T, request.normalized, request.directed, request.weight)
            
            resp = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=ret[0],message=ret[1])

            if resp.status:
                betweenness_centrality=ret[2]["betweenness_centrality"]

                if (T==0):
                    node_resp=network_analytics_robustness_pb2.node_betweenness(node=betweenness_centrality[0], node_centrality_value=betweenness_centrality[1])
                    resp = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=ret[0],message=ret[1],node_betweenness_centrality=node_resp)
                
                elif(T==1):
                    edges_resp = []
                    for edge_ret in betweenness_centrality[0]:
                        edges_resp.append(network_analytics_robustness_pb2.Edge(edge=list(edge_ret)))
                    graph_resp=network_analytics_robustness_pb2.edge_betweenness(edge=edges_resp, edge_centrality_value=betweenness_centrality[1])
                    resp = network_analytics_robustness_pb2.MostImportantNodesEdgesSubsetResponse(status=ret[0],message=ret[1],edge_betweenness_centrality=graph_resp)

            else:

                print(time.strftime("%c"))
                print('Waiting for next call on port 5002.')

                raise grpc.RpcError(grpc.StatusCode.UNKNOWN, ret[1])




            print('status:',resp.status)
            print('message:',resp.message)
            print(time.strftime("%c"))
            print('Waiting for next call on port 5002.')

            return resp


        except Exception as e:

            logging.exception("message")

            print(time.strftime("%c"))
            print('Waiting for next call on port 5002.')

            raise grpc.RpcError(grpc.StatusCode.UNKNOWN, str(e))


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_analytics_robustness_pb2_grpc.add_NetworkAnalyticsRobustnessServicer_to_server(NetworkAnalyticsRobustness(), server)
    print('Starting server. Listening on port 5002.')
    server.add_insecure_port('127.0.0.1:5002')
    server.start()
    try:
        while True:
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        server.stop(0)


def serve_test():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_analytics_robustness_pb2_grpc.add_NetworkAnalyticsRobustnessServicer_to_server(NetworkAnalyticsRobustness(), server)
    print('Starting server. Listening on port 5000.')
    server.add_insecure_port('127.0.0.1:5000')
    return server



__end__ = '__end__'



if __name__ == '__main__':


    serve()

    pass










