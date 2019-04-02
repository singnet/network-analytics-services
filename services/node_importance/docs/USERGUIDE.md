[![SingnetLogo](../../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')](https://singularitynet.io/)

# Network Analytics Services
## Node Importance


### Welcome

This repository contains various network analytics services for SingularityNET. The services are wrapped using gRPC. To work with the service wrapper code "snet_grpc_wrapper.py" and other code that make use of gRPC functionality, run the following in the "services" directory


### How Does It Work
This service have The following functionalities
       
       - find_central_nodes
       - find_eccentricity
       - find_Periphery
       - find_closeness_centrality
       - find_betweenness_centrality
       - find_pagerank
       - find_eigenvector_centrality
       - find_Hits


The user must provide a request satisfying the [proto descriptions](https://github.com/IsraelAbebe/network-analytics-services/blob/master/services/node_importance/service_spec/node_importance.proto) given.

#### Example input 
The following Graph is used as an input for the following examples
```bash
graph = {
	"nodes": ['1','2','3','4','5','6','7','8'],
	"edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
	"weights": [3,4,5,6,7,8,9,10]
}
```

### Sample  Outputs
#### Find Central Nodes [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.distance_measures.center.html?highlight=algorithms%20distance_measures%20center#networkx.algorithms.distance_measures.center)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output {
  output_nodes: "2"
  output_nodes: "3"
}
```

#### Find Periphery [networkx](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.periphery.html#networkx.algorithms.distance_measures.periphery)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output {
  output_nodes: "1"
  output_nodes: "4"
  output_nodes: "5"
  output_nodes: "6"
  output_nodes: "7"
  output_nodes: "8"
}
```
 
#### Find Degree Centrality [networkx](https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output {
  edge: "1"
  edge: "2"
  edge: "3"
  edge: "4"
  edge: "5"
  edge: "6"
  edge: "7"
  edge: "8"
  output: 0.2857142984867096
  output: 0.4285714328289032
  output: 0.4285714328289032
  output: 0.0
  output: 0.0
  output: 0.0
  output: 0.0
  output: 0.0
}
```

#### Find Closeness Centrality [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.bipartite.centrality.closeness_centrality.html?highlight=algorithms%20bipartite%20centrality%20closeness_centrality#networkx.algorithms.bipartite.centrality.closeness_centrality)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output {
  edge: "1"
  edge: "2"
  edge: "8"
  edge: "4"
  edge: "5"
  edge: "7"
  edge: "3"
  edge: "6"
  output: 0.5714285969734192
  output: 0.800000011920929
  output: 0.75
  output: 0.8571428656578064
  output: 0.75
  output: 0.75
  output: 1.2000000476837158
  output: 0.75
}
```

#### Find Betweenness Centrality [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.bipartite.centrality.betweenness_centrality.html?highlight=algorithms%20centrality%20betweenness_centrality#networkx.algorithms.bipartite.centrality.betweenness_centrality)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output {
  edge: "1"
  edge: "2"
  edge: "3"
  edge: "4"
  edge: "5"
  edge: "6"
  edge: "7"
  edge: "8"
  output: 0.0714285746216774
  output: 0.5952380895614624
  output: 0.5952380895614624
  output: 0.0714285746216774
  output: 0.0
  output: 0.0
  output: 0.0
  output: 0.0
}

```

#### Find Page Rank [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html#networkx.algorithms.link_analysis.pagerank_alg.pagerank)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output {
  edge: "1"
  edge: "2"
  edge: "3"
  edge: "4"
  edge: "5"
  edge: "6"
  edge: "7"
  edge: "8"
  output: 0.07655997574329376
  output: 0.21930024027824402
  output: 0.264370322227478
  output: 0.10837001353502274
  output: 0.06737788021564484
  output: 0.0786743313074112
  output: 0.09169182181358337
  output: 0.09365541487932205
}
```

#### Find Eigen Vector Centrality [networkx](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.centrality.eigenvector_centrality.html?highlight=algorithms%20centrality%20eigenvector_centrality#networkx.algorithms.centrality.eigenvector_centrality)
An example result obtained after passing the Input
```bash
status: true
message: "success"
output {
  edge: "1"
  edge: "2"
  edge: "3"
  edge: "4"
  edge: "5"
  edge: "6"
  edge: "7"
  edge: "8"
  output: 0.35775017738342285
  output: 0.5298994183540344
  output: 0.5298994183540344
  output: 0.35775017738342285
  output: 0.2135666161775589
  output: 0.2135666161775589
  output: 0.2135666161775589
  output: 0.2135666161775589
}
```

#### Find Hits [networkx](https://networkx.github.io/documentation/stable/reference/algorithms/link_analysis.html)
An example result obtained after passing the Input
```bash
{'hub_matrix': [[25.0, 0.0, 43.0, 0.0, 18.0, 0.0, 27.0, 0.0], [0.0, 151.0, 0.0, 47.0, 0.0, 40.0, 0.0, 50.0], [43.0, 0.0, 238.0, 0.0, 30.0, 0.0, 45.0, 0.0], [0.0, 47.0, 0.0, 65.0, 0.0, 56.0, 0.0, 70.0], [18.0, 0.0, 30.0, 0.0, 36.0, 0.0, 54.0, 0.0], [0.0, 40.0, 0.0, 56.0, 0.0, 64.0, 0.0, 80.0], [27.0, 0.0, 45.0, 0.0, 54.0, 0.0, 81.0, 0.0], [0.0, 50.0, 0.0, 70.0, 0.0, 80.0, 0.0, 100.0]]}
```



