# Tested on python3.6

import grpc
from concurrent import futures
import time


import network_analytics_pb2
import network_analytics_pb2_grpc

import time
import bipartite_graphs
import graphs
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

        print('>>>>>>>>>>>>>>In endpoint ProjectedGraph')
        print(time.strftime("%c"))

        bipartite_graph = request.graph
        nodes = request.nodes
        weight = request.weight

        print (bipartite_graph)

        b = bipartite_graphs.BipartiteGraphs()

        try:

            edges_list = []


            for edges_proto in bipartite_graph.edges:
                edges_list.append(list(edges_proto.edge))

            bipartite_graph_in = {"bipartite_0":list(bipartite_graph.bipartite_0),"bipartite_1":list(bipartite_graph.bipartite_1),"edges":edges_list}
            nodes_in = {"nodes": list(nodes)}

            ret = b.projected_graph(bipartite_graph_in, nodes_in, weight)

            resp = network_analytics_pb2.ProjecetedGraphResponse(status=ret[0],message=ret[1])

            if resp.status:
                edges_resp = []
                for edge_ret in ret[2]["edges"]:
                    edges_resp.append(network_analytics_pb2.Edge(edge=edge_ret))

                graph_resp = network_analytics_pb2.Graph(nodes=ret[2]["nodes"],edges=edges_resp,weights=ret[2]["weights"])


                resp = network_analytics_pb2.ProjecetedGraphResponse(status=ret[0],message=ret[1],output=graph_resp)


            print('status:',resp.status)
            print('message:',resp.message)
            print('Waiting for next call on port 5000.')

            return resp


        except Exception as e:

            logging.exception("message")

            resp = network_analytics_pb2.ProjecetedGraphResponse(status=False,message=str(e))

            print('status:', resp.status)
            print('message:', resp.message)
            print('Waiting for next call on port 5000.')

            return resp



    def MinNodeGraph(self,request,context):

        print('>>>>>>>>>>>>>>In endpoint MinNodeGraph')
        print(time.strftime("%c"))

        graph = request.graph
        source_nodes = request.source_node
        target_nodes = request.target_node
    
        print(source_nodes)
        print(target_nodes)

        g = graphs.Graphs()

        try:

            edges_list = []


            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            
        
            graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
            source_nodes_in = str(source_nodes)
            target_nodes_in = str(target_nodes)

            print(graph_in)
            print(source_nodes_in)
            print(target_nodes_in)

            ret = g.min_nodes_to_remove(graph_in,source_nodes_in,target_nodes_in)    
            print (ret[0])
            print (ret[1])
            
            resp = network_analytics_pb2.MinNodeGraphResponse(status=ret[0],message=ret[1])

            if resp.status:
                nodes_resp=ret[2]["nodes"]
                print(nodes_resp)
                edges_resp = []
                for edge_ret in ret[2]["edges"]:
                    edges_resp.append(network_analytics_pb2.Edge(edge=edge_ret))

                print(edges_resp)
                resp = network_analytics_pb2.MinNodeGraphResponse(status=ret[0],message=ret[1],nodes_output=nodes_resp,edges_output=edges_resp)


            print('status:',resp.status)
            print('message:',resp.message)
            print('Waiting for next call on port 5000.')

            return resp


        except Exception as e:

            logging.exception("message")

            resp = network_analytics_pb2.MinNodeGraphResponse(status=False,message=str(e))

            print('status:', resp.status)
            print('message:', resp.message)
            print('Waiting for next call on port 5000.')

            return resp

   
    def MostImportantGraph(self,request,context):

        print('>>>>>>>>>>>>>>In endpoint MostImportantGraph')
        print(time.strftime("%c"))

        graph = request.graph
        source_nodes = request.source_nodes
        target_nodes = request.target_nodes
        T = request.Type

        print(source_nodes)
        print(target_nodes)
        print(T)

        g = graphs.Graphs()

        try:

            edges_list = []


            for edges_proto in graph.edges:
                edges_list.append(list(edges_proto.edge))
            
        
            graph_in ={"nodes":list(graph.nodes),"edges":edges_list}
            source_nodes_in = list(source_nodes)
            target_nodes_in = list(target_nodes)

            print(graph_in)
            print(source_nodes_in)
            print(target_nodes_in)

            ret = g.most_important_nodes_edges(graph_in,source_nodes_in,target_nodes_in,T)    
            print (ret[0])
            print (ret[1])
            
            resp = network_analytics_pb2.MostImportantGraphResponse(status=ret[0],message=ret[1])

            if resp.status:
                betweenness_centrality=ret[2]["betweenness_centrality"]
                print([betweenness_centrality[1]][0])

                if (T==0):
                    node_resp=network_analytics_pb2.node_betweenness(node=[betweenness_centrality[0]][0], node_centrality_value=[betweenness_centrality[1]][0])
                    resp = network_analytics_pb2.MostImportantGraphResponse(status=ret[0],message=ret[1],node_betweenness_centrality=node_resp)
                
                elif(T==1):
                    edge=list([betweenness_centrality[0]][0])
                    print(edge)
                    print(edge[1])
                    proto_edge=network_analytics_pb2.Edge(edge=edge)
                    edge_resp=network_analytics_pb2.edge_betweenness(edge=proto_edge, edge_centrality_value=[betweenness_centrality[1]][0]) 
                    resp = network_analytics_pb2.MostImportantGraphResponse(status=ret[0],message=ret[1],edge_betweenness_centrality=edge_resp) 


            print('status:',resp.status)
            print('message:',resp.message)
            print('message:',resp.node_betweenness_centrality)
            print('message:',resp.edge_betweenness_centrality)
            print('Waiting for next call on port 5000.')

            return resp


        except Exception as e:

            logging.exception("message")

            resp = network_analytics_pb2.MostImportantGraphResponse(status=False,message=str(e))

            print('status:', resp.status)
            print('message:', resp.message)
            print('Waiting for next call on port 5000.')

            return resp            


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










