# Tested on python3.6


import networkx as nx


def betweeness_centrality_subset():

    nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    edges_sources = [[1,2],[1,3],[3,4],[4,5],[5,6],[6,7]]
    edges_targets = [[8,9],[10,11],[11,12],[12,13],[13,14],[14,15],[10,13],[9,15],[8,14]]
    edges_interconnections = [[4,8],[6,10],[7,14]]  # Connection between source and target nodes

    edges = []

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges_sources)
    G.add_edges_from(edges_targets)
    G.add_edges_from(edges_interconnections)

    # print(G.edges)

    result = nx.betweenness_centrality_subset(G, [1,2,3,4,5], [1,13,14,15])
    print(result)
    result = nx.betweenness_centrality_subset(G, [1, 2, 3,], [13, 14, 15])
    print(result)
    result = nx.edge_betweenness_centrality_subset(G, [1,2,3,4,5], [12,13,14,15])
    print(result)

    print('--------------------------')


    nodes = [1,2,3,4,5,6,7,10,11,12,13,14,15]
    edges_sources = [[1,2],[1,3],[3,4],[4,6],[6,7]] # 5 removed here
    edges_targets = [[8,9],[10,11],[11,13],[13,14],[14,15],[10,13],[9,15],[8,14]] # 12 removed here
    edges_interconnections = [[4,8],[6,10],[7,14]]  # Connection between source and target nodes

    edges = []

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges_sources)
    G.add_edges_from(edges_targets)
    G.add_edges_from(edges_interconnections)

    # print(G.edges)

    result = nx.betweenness_centrality_subset(G, [1,2,3,4,5], [13,14,15])
    print(result)
    result = nx.betweenness_centrality_subset(G, [1, 2, 3, 4], [13, 14, 15])
    print(result)
    result = nx.edge_betweenness_centrality_subset(G, [1,2,3,4,5], [12,13,14,15])
    print(result)


    print('-------------------------')
    print(G.edges)
    G[1][2]['weight']=0.8
    G[1][2]['weightre']=0.83
    print(G[1][2])























__end__ = '__end__'

if __name__ == '__main__':

    betweeness_centrality_subset()