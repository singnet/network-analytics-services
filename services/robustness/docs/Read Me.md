Read Me

In graphs there are functions - 
	most important nodes and edges - this calculates _____, given parameters such as _____ the output is _______
	minimum number of nodes to remove - this calculates _____, given parameters such as _____ the output is _______

In test_graphs there are unit_tests for the functions in graphs - here we test the validity of a graph with messed up parameters as well as the expected output for valid input

In snet_grpc_wrapper there are the grpc services for each of the functions - 
In the .proto file you will find the definitions of differnt types of 

In check_validity there are a couple of funtions that check the validity of the graph passed in for each of the functions



--------------------------------------------------------------------------------------------------------------------------------------------------

This repository contains various network analytics services for SingularityNET. The services are wrapped using gRPC. To work with the service wrapper code "snet_grpc_wrapper.py" and other code that make use of gRPC functionality, run the following in the "services" directory

python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. network_analytics.proto
This will generate the files "network_analytics_pb2.py" and "network_analytics_pb2_grpc.py" in the "services" directory which you can then use with the rest of the code in the repository.

Below is a list of currently available services under different categories. Also detailed services input/output specifications.

List of Services

Bipartite robustness
Bipartite Graph: Create a bipartite graph from two given nodes and a set of edges
Projected Graph: Returns the projection of a bipartite graph on a given set of nodes.

robustness
min_nodes_to_remove: gives the minimum set of nodes/edges to disconnect source node and targert node.
most_important_nodes_edges: provides the betweness centrality of the subset

Input/Output Service Specification
min_nodes_to_remove
Description: gives the minimum set of nodes/edges to disconnect source node and targert node

 Detailed specs
Service endpoint: min_nodes_to_remove

graph: a dictionary containing nodes, edges and optionally weights

Key name: nodes - a one dimentional list of nodes in the graph

sample input:

graph = {
		"nodes": ['1','2','3','4','5','6'],
		"edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['4','6']]
		}

Key name: edges - a two dimentional array (list in a list) containing all the connected nodes in the graph. If its a directed graph the direction is by default assumed to be from the first to the secnod node.

Key name: weights - No weight is used for the calculations, if this attribute is supplied in the graph it will be ignored. 

input name: source_node - a node element of the graph 
sample input:

source_node = '1'

input name: target_node - a node element of the graph 
sample input: 

target_node = '6'


output: If no error is raised, a list of edges and nodes that can be removed is returned along with a boolean true and a ‘success’ text message. If an error is raised a false boolean value is returned along with a specific error message and an empty dictionary {}.

sample output 1 for error free invocation:

[True,
'success',
{'edges': [['4', '6'], ['3', '6']],
'nodes': ['3', '4']}]

sample output 2 for ERROR invocation:

[False, 
'node 5 doesn’t exist in the graph'
,{}]

Error handling:

All specified input arguments must be present as named above. And arrays should be used strictly as indicated.
Making sure graph contains at least two nodes and one edge.
Making sure each edge contains two nodes.
Making sure that all elements in edges are contained in the graph.
Making sure that source_node and target_node are contained in the graph.
If any of the above is found to be true an error message will be returned.

Service:most_important_nodes_edges
Description: provides the betweness centrality of the subset.

 Detailed specs
Service endpoint: most_important_nodes_edges

most_important_nodes_edges(graph, source_nodes, target_nodes,)
graph = {
    "nodes": ['1','2','3','4','5','6','7','8'],
    "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
    "weights": [3,4,5,6,7,8,9,10]
}
 
Key name: edges - a two dimentional array (list in a list) containing all the connected nodes in the graph. If its a directed graph the direction is by default assumed to be from the first to the secnod node.

Key name: weights (not required)- if weights are supplied in the graph then each value is assigned to the edges one by one.

input name: source_nodes - a node element of the graph 
sample input:

source_nodes = ['5','7']


input name: target_nodes - a node element of the graph 
sample input: 

target_nodes = ['6']		

 T=0, normalized=True, directed=False
input name: T - a binary input, at T=0 the funtion will calculate the node betweenness centrality of the subset and at T=1 the edge betweenness centrality of the subset.

sample input: T=0 or T=1 (default is 0)


input name:normalized -  If True the betweenness values are normalized by 2/((n−1)(n−2)) for graphs, and 1/((n−1)(n−2)) for directed graphs where n is the number of nodes in the supplied graph.	

sample input: True or False (default is True)

input name:directed - Describes weather the supplied graph shall be treated as a directed or an undirected graph.
sample input: True or False (default is False)


output: most_important_nodes_edges

sample output 1 for error free invocation where T=0 and node betweenness centrality is calculated:

[True,
'success',
{'betweenness_centrality': [2, 0.047619047619047616]}
]

sample output 2 for error free invocation where T=1 and edge betweenness centrality is calculated:

[True,
 'success',
 {'betweenness_centrality': [(2, 3), 0.03571428571428571]}
]

sample output 3 for ERROR invocation:

[False, 
'node 11 doesn’t exist in the graph',
{}
]

Error handling:

All specified input arguments must be present as named above. And arrays should be used strictly as indicated.
Making sure graph contains at least two nodes and one edge.
Making sure each edge contains two nodes.
Making sure that all elements in edges are contained in the graph.
Making sure the supplied weight (if any) is in an array format 
Making sure the length of the supplied weight (if any) matches that of the provided edges.
Making sure that all elements in source_nodes and target_nodes are in an array format.
Making sure that all elements in source_nodes and target_nodes are contained in the graph.
Making sure that type T has a value of either zero or one.
If any of the above is found to be true an error message will be returned.