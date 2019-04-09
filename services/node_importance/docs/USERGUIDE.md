[![SingnetLogo](../../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')](https://singularitynet.io/)

# Node Importance Services


## Methods

The corresponding methods from the networkx library are wrapped and put as a service. Some of the parameter descriptions
are credited to NetworkX Developers.

* [CentralNodes](#centralnodes)
* [Periphery](#periphery)
* [DegreeCentrality](#degreecentrality)
* [ClosenessCentrality](#closenesscentrality)
* [BetweennessCentrality](#betweennesscentrality)
* [eigenvector centrality](#eigenvectorcentrality)
* [pagerank](#pagerank)
* [hits](#hits)


## CentralNodes

Identify the central nodes from the given input graph

### Inputs

* A graph (required)
* usebounds (optional,default value is False): When this option is used, the [extrema_bounding](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.extrema_bounding.html#networkx.algorithms.distance_measures.extrema_bounding) method is used for calculating central nodes.

#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeImportance CentralNodes centralnodes.json -y
```

where the content of the file `centralnodes.json` is

```
{
 "graph": {
        "nodes": ["1","2","3","4","5","6"],
        "edges": [{"edge": ["1","2"]},{"edge": ["1","4"]},{"edge": ["2","3"]},{"edge": ["2","5"]},{"edge": ["3","4"]},{"edge": ["3","6"]},{"edge": ["4","6"]}]
}
```

#### Sample output

```
status: true
message: "success"
output: "2"
output: "3"
```

## Periphery

Identify the peripheral/remote nodes from the given input graph

### Inputs

* A graph (required)
* usebounds (optional,default value is False): When this option is used, the [extrema_bounding](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.extrema_bounding.html#networkx.algorithms.distance_measures.extrema_bounding) method is used for calculating peripheral nodes.

#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeImportance Periphery periphery.json -y
```

where the content of the file `periphery.json` is

```
{
 "graph": {
        "nodes": ["1","2","3","4","5","6"],
        "edges": [{"edge": ["1","2"]},{"edge": ["1","4"]},{"edge": ["2","3"]},{"edge": ["2","5"]},{"edge": ["3","4"]},{"edge": ["3","6"]},{"edge": ["4","6"]}]
}
```

#### Sample output

```
status: true
message: "success"
output: "1"
output: "4"
output: "5"
output: "6"
output: "7"
output: "8"
```

## DegreeCentrality

Find the degree centrality of nodes.

### Inputs

* A graph (required)

#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeImportance DegreeCentrality degreecentrality.json -y
```

where the content of the file `degreecentrality.json` is

```
{
 "graph": {
        "nodes": ["1","2","3","4","5","6"],
        "edges": [{"edge": ["1","2"]},{"edge": ["1","4"]},{"edge": ["2","3"]},{"edge": ["2","5"]},{"edge": ["3","4"]},{"edge": ["3","6"]},{"edge": ["4","6"]}]
}
```

#### Sample output

```
status: true
message: "success"
output {
  node: "1"
  output: 0.2857142857142857
}
output {
  node: "2"
  output: 0.5714285714285714
}
output {
  node: "3"
  output: 0.5714285714285714
}
output {
  node: "4"
  output: 0.2857142857142857
}
output {
  node: "5"
  output: 0.14285714285714285
}
output {
  node: "6"
  output: 0.14285714285714285
}
output {
  node: "7"
  output: 0.14285714285714285
}
output {
  node: "8"
  output: 0.14285714285714285
}
```

## ClosenessCentrality

Compute closeness centrality for nodes.

### Inputs

* A graph (required)
* distance (Optional. Default is False): If True, then the weights in the given graph are used in shortest path calculations
* wf_improved (optional. Default value is 'wf_improved'. Any other value other than the default value including the null string will result in not using the [improved Wasserman and Faust formula](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html#networkx.algorithms.centrality.closeness_centrality).
* reverse (Optional. Default is False): If True and input graph G is a directed graph, reverse the edges of G, using successors instead of predecessors.
* directed (Optional. Default is False). If True the graph is treated as a directed graph where the first specified node in an edge is the source node.

#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeImportance ClosenessCentrality closenesscentrality.json -y
```

where the content of the file `betweennesscentrality.json` is

```
{
    "graph":
           {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}]
        },
    "type":"node"

}
```

#### Sample output

```
status: true
message: "success"
output {
  node: "1"
  output: 0.5
}
output {
  node: "2"
  output: 0.7
}
output {
  node: "3"
  output: 0.7
}
output {
  node: "4"
  output: 0.5
}
output {
  node: "5"
  output: 0.4375
}
output {
  node: "6"
  output: 0.4375
}
output {
  node: "7"
  output: 0.4375
}
output {
  node: "8"
  output: 0.4375
}
de: "8"
}
```



## BetweennessCentrality

Find the BetweennessCentrality of nodes.

### Inputs

* A graph (required)
* type (Optional. Possible values are 'node'(default) and 'edge'): Indicates to calculate node or edge betweeness centrality
* k (optional. Default value is zero meaning that the parameter is not used)
* normalized (Optional. Default is True): If k is not zero use k node samples to estimate betweenness. The value of k <= n where n is the number of nodes in the graph. Higher values give better approximation.
* weight (Optional. Default is False): If True, then the weights in the given graph are used
* endpoints (Optional. Default is False): If True include the endpoints in the shortest path counts.
* seed (Optional. Default is zero meaning that the parameter is not used): – Indicator of random number generation state. This is only used if k is not None.
* directed (Optional. Default is False). If True the graph is treated as a directed graph where the first specified node in an edge is the source node.


#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeImportance BetweennessCentrality betweennesscentrality.json -y
```

where the content of the file `betweennesscentrality.json` is

```
{
    "graph":
           {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}]
        },
    "type":"node"

}
```

#### Sample output

```
status: true
message: "success"
output {
  node: "1"
  output: 0.07142857142857142
}
output {
  node: "2"
  output: 0.5952380952380952
}
output {
  node: "3"
  output: 0.5952380952380952
}
output {
  node: "4"
  output: 0.07142857142857142
}
output {
  node: "5"
}
output {
  node: "6"
}
output {
  node: "7"
}
output {
  node: "8"
}
```


