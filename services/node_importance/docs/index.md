
# Network Analytics Services
## Node Importance


### Welcome

This repository contains various network analytics services for SingularityNET. The services are wrapped using gRPC. To work with the service wrapper code "snet_grpc_wrapper.py" and other code that make use of gRPC functionality, run the following in the "services" directory


### How Does It Work
This service have The following functionalities
       
       - find_central_nodes
       - find_eccentricity
       - find_degree_centrality
       - find_closeness_centrality
       - find_betweenness_centrality
       - find_pagerank
       - find_eigenvector_centrality
       - find_hub_matrix
       - find_authority_matrix


The user must provide a request satisfying the [proto descriptions](https://github.com/IsraelAbebe/network-analytics-services/blob/master/services/node_importance/node_importance.proto) given.

#### Example input 
The following Graph is used as an input for the following examples
```bash
graph = {
	"nodes": ['1','2','3','4','5','6','7','8'],
	"edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
	"weights": [3,4,5,6,7,8,9,10]
}
```
### Example output
All Outputs have the following form:
```bash
message CentralNodeOutput{
	bool status = 6;
	string message = 7;
	string output = 8;
  
}
```

### Sample Outputs
#### Find Central Nodes [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.distance_measures.center.html?highlight=algorithms%20distance_measures%20center#networkx.algorithms.distance_measures.center)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "{\'central_nodes\': [\'2\', \'3\']}"
```

#### Find Eccentricity [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.distance_measures.eccentricity.html?highlight=algorithms%20distance_measures%20eccentricity#networkx.algorithms.distance_measures.eccentricity)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "{\'eccentricity\': {\'1\': 3, \'2\': 2, \'3\': 2, \'4\': 3, \'5\': 3, \'6\': 3, \'7\': 3, \'8\': 3}}"
```
 
#### Find Degree Centrality [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.bipartite.centrality.degree_centrality.html?highlight=algorithms%20centrality%20degree_centrality#networkx.algorithms.bipartite.centrality.degree_centrality)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "{\'degree_centrality\': {\'1\': 0.2857142857142857, \'2\': 0.5714285714285714, \'3\': 0.5714285714285714, \'4\': 0.2857142857142857, \'5\': 0.14285714285714285, \'6\': 0.14285714285714285, \'7\': 0.14285714285714285, \'8\': 0.14285714285714285}}"
```

#### Find Closeness Centrality [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.bipartite.centrality.closeness_centrality.html?highlight=algorithms%20bipartite%20centrality%20closeness_centrality#networkx.algorithms.bipartite.centrality.closeness_centrality)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "{\'closeness_centrality\': {\'1\': 0.5714285714285714, \'2\': 0.8, \'3\': 1.2, \'6\': 0.75, \'8\': 0.75, \'7\': 0.75, \'4\': 0.8571428571428571, \'5\': 0.75}}"
```

#### Find Betweenness Centrality [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.bipartite.centrality.betweenness_centrality.html?highlight=algorithms%20centrality%20betweenness_centrality#networkx.algorithms.bipartite.centrality.betweenness_centrality)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "{\'betweenness_centrality\': {\'1\': 0.07142857142857142, \'2\': 0.5952380952380952, \'3\': 0.5952380952380952, \'4\': 0.07142857142857142, \'5\': 0.0, \'6\': 0.0, \'7\': 0.0, \'8\': 0.0}}"
```

#### Find Page Rank [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html#networkx.algorithms.link_analysis.pagerank_alg.pagerank)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "{\'pagerank\': {\'1\': 0.12113884655309373, \'2\': 0.23955113566709454, \'3\': 0.23955113566709454, \'4\': 0.12113884655309375, \'5\': 0.06965500888990583, \'6\': 0.06965500888990583, \'7\': 0.06965500888990583, \'8\': 0.06965500888990583}}"
```

#### Find Eigen Vector Centrality [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.centrality.eigenvector_centrality.html?highlight=algorithms%20centrality%20eigenvector_centrality#networkx.algorithms.centrality.eigenvector_centrality)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "{\'eigenvector_centrality\': {\'1\': 0.35775018836999806, \'2\': 0.5298994260311778, \'3\': 0.5298994260311778, \'4\': 0.35775018836999806, \'5\': 0.2135666184274351, \'6\': 0.2135666184274351, \'7\': 0.2135666184274351, \'8\': 0.2135666184274351}}"
```

#### Find Hub Matrix [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.link_analysis.hits_alg.hub_matrix.html?highlight=algorithms%20link_analysis%20hits_alg%20hub_matrix#networkx.algorithms.link_analysis.hits_alg.hub_matrix)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "[[2. 0. 2. 0. 1. 0. 1. 0.]\n [0. 4. 0. 2. 0. 1. 0. 1.]\n [2. 0. 4. 0. 1. 0. 1. 0.]\n [0. 2. 0. 2. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]]"
```

#### Find Authority Matrix [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.link_analysis.hits_alg.authority_matrix.html)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output: "[[2. 0. 2. 0. 1. 0. 1. 0.]\n [0. 4. 0. 2. 0. 1. 0. 1.]\n [2. 0. 4. 0. 1. 0. 1. 0.]\n [0. 2. 0. 2. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]\n [1. 0. 1. 0. 1. 0. 1. 0.]\n [0. 1. 0. 1. 0. 1. 0. 1.]]"
```



