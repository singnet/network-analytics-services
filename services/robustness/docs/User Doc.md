
1. min_nodes_to_remove

Expected input format 

graph_in = {
    "nodes": ['1','2','3','4','5'],
    "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['4','6']]
    }
source_node = '1'
target_node = '6'

Expected output 

[True, 'success', {'edges': [[4, 6], [3, 6]], 'nodes': [3, 4]}]

Function call format: 
MinNodeGraphRequest(graph=graph_in,source_node=source_node,target_node=target_node)

2. most_important_nodes_edges
Expected input format 

graph = {
    "nodes": ['1','2','3','4','5','6','7','8'],
    "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
    "weights": [3,4,5,6,7,8,9,10]
}
source_nodes = ['5','7']
target_nodes = ['6']

A. T=0

Expected output 
[True, 'success',{'betweenness_centrality': ['2', 0.047619047619047616]}]

Function call format: 
MinNodeGraphRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=0)

B. T=1

Expected output 
[True, 'success', {'betweenness_centrality': [('2', '3'), 0.03571428571428571]}]

Function call format: 
MinNodeGraphRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=1)


