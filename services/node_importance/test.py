import networkx as nx
from node_importance import NodeImportance

import Graphs
import check_graph_validity
import networkx as nx

graph = {"nodes": [1,2,3,4,5,6,7,8],"edges": [[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[2,7],[3,8]],"weights": [3,4,5,6,7,8,9,10]}




N = NodeImportance()

result = N.find_central_nodes(graph)
print("find_central_nodes",result)

result = N.find_eccentricity(graph)
print("find_eccentricity",result)

result = N.find_degree_centrality(graph)
print("find_degree_centrality",result)

# result = N.find_closeness_centrality(graph)
# print("find_closeness_centrality",result)

result = N.find_betweenness_centrality(graph)
print("find_betweenness_centrality",result)

result = N.find_pagerank(graph)
print("find_betweenness_centrality",result)

result = N.find_eigenvector_centrality(graph)
print("find_betweenness_centrality",result)
