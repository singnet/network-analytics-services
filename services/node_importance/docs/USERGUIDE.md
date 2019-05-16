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
* [EigenvectorCentrality](#eigenvectorcentrality)
* [PageRank](#pagerank)
* [Hits](#hits)


## CentralNodes

Identify the central nodes from the given input graph

### Inputs

* A graph (required)
* usebounds (optional,default value is False): When this option is used, the [extrema_bounding](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.extrema_bounding.html#networkx.algorithms.distance_measures.extrema_bounding) method is used for calculating central nodes.

#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeimportance CentralNodes centralnodes.json -y
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
snet client call snet network-analytics-nodeimportance Periphery periphery.json -y
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
snet client call snet network-analytics-nodeimportance DegreeCentrality degreecentrality.json -y
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
snet client call snet network-analytics-nodeimportance ClosenessCentrality closenesscentrality.json -y
```

where the content of the file `betweennesscentrality.json` is

```
{
    "graph":
           {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}]
        }

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
snet client call snet network-analytics-nodeimportance BetweennessCentrality betweennesscentrality.json -y
```

where the content of the file `betweennesscentrality.json` is

```
{
    "graph":
           {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}]
        }
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

## EigenvectorCentrality

Find the EigenvectorCentrality of nodes.

### Inputs

* A graph (required)
* max_iter (Optional. Integer. Default is 100): Maximum number of iterations in power method.
* tol (Optional. Float. Default is 1e-06): Error tolerance used to check convergence in power method iteration.
* nstart (Optional. If you skip setting this field, you will get the default behavior): It is a dictionary of starting values of eigenvector iteration for each node. I.e., each node would have a corresponding value.
* weight (Optional. Default is False): If True, then the weights in the given graph are used. If no weights are given, all edge weights are considered equal.
* directed (Optional. Default is False). If True the graph is treated as a directed graph where the first specified node in an edge is the source node.
* in_out (Optinal. String value. Default is the empty string '' or the string 'in'). This is used when the graph is a directed graph. Supply the string 'in' or leave setting the parameter (that is it will have value of the null string '') if you want to calculate 'left' eigenvector centrality which corresponds to the in-edges in the graph. Use the string 'out' or anyother string to calculate the out-edges eigenvector centrality.



#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeimportance EigenvectorCentrality eigenvectorcentrality.json -y
```

where the content of the file `eigenvectorcentrality.json` is

```
{
    "graph":
           {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}]
        }
}
```

#### Sample output

```
status: true
message: "success"
output {
  node: "1"
  output: 0.35775018836999806
}
output {
  node: "2"
  output: 0.5298994260311778
}
output {
  node: "3"
  output: 0.5298994260311778
}
output {
  node: "4"
  output: 0.35775018836999806
}
output {
  node: "5"
  output: 0.2135666184274351
}
output {
  node: "6"
  output: 0.2135666184274351
}
output {
  node: "7"
  output: 0.2135666184274351
}
output {
  node: "8"
  output: 0.2135666184274351
}
```

## PageRank

Find the PageRank of nodes.

### Inputs

* A graph (required)
* alpha (Optional. Float. Default is 0.85): Damping parameter.
* personalization (Optional. Dictionary. If you skip setting this field, you will get the default behavior). A dictionary with a key for some subset of graph nodes and personalization value each of those. At least one personalization value must be non-zero. If not specfiied, a nodes personalization value will be zero. By default, a uniform distribution is used.
* max_iter (Optional. Integer. Default is 100): Maximum number of iterations in power method eigenvalue solver.
* tol (Optional. Float. Default is 1e-06): Maximum number of iterations in power method eigenvalue solver.
* nstart (Optional. Dictionary. If you skip setting this field, you will get the default behavior): It is a dictionary of starting values of eigenvector iteration for each node. I.e., each node would have a corresponding value.
* weight (Optional. Default is False): If True, then the weights in the given graph are used. If no weights are given, all edge weights are set to one.
* dangling (Optional. Dictionary. If you skip setting this field, you will get the default behavior): The outedges to be assigned to  nodes without any outedges. The dict key is the node the outedge points to and the dict value is the weight of that outedge. By default, dangling nodes are given outedges according to the personalization vector (uniform if not specified). This must be selected to result in an irreducible transition matrix. It may be common to have the dangling dict to be the same as the personalization dict.
* directed (Optional. Default is False). If True the graph is treated as a directed graph where the first specified node in an edge is the source node.

#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeimportance PageRank pagerank.json -y
```

where the content of the file `pagerank.json` is

```
{
    "graph":
           {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}]
        }
}
```

#### Sample output

```
status: true
message: "success"
output {
  node: "1"
  output: 0.12113884655309373
}
output {
  node: "2"
  output: 0.23955113566709454
}
output {
  node: "3"
  output: 0.23955113566709454
}
output {
  node: "4"
  output: 0.12113884655309375
}
output {
  node: "5"
  output: 0.06965500888990583
}
output {
  node: "6"
  output: 0.06965500888990583
}
output {
  node: "7"
  output: 0.06965500888990583
}
output {
  node: "8"
  output: 0.06965500888990583
}
```

## Hits

Find the HITS hubs and authorities values for nodes.

### Inputs

* A graph (required)
* max_iter (Optional. Integer. Default is 100): Maximum number of iterations in power method.
* tol (Optional. Float. Default is 1e-08): Maximum number of iterations in power method eigenvalue solver.
* nstart (Optional. Dictionary. If you skip setting this field, you will get the default behavior): It is a dictionary of starting values of eigenvector iteration for each node. I.e., each node would have a corresponding value.
* normalized (Optinal. String value. Default is the empty string '' or the string 'n'). This is used to normalize results by the sum of all of the values. Any string value except 'n' and '' would not use normalization.
* directed (Optional. Default is False). If True the graph is treated as a directed graph where the first specified node in an edge is the source node.

#### Sample call

Sample call while using the SingularityNET CLI terminal application

```
snet client call snet network-analytics-nodeimportance Hits hits.json -y
```

where the content of the file `hits.json` is

```
{
    "graph":
           {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}]
        }
}
```

#### Sample output

```
status: true
message: "success"
hubs {
  node: "1"
  output: 0.13604957690850644
}
hubs {
  node: "2"
  output: 0.2015158583139189
}
hubs {
  node: "3"
  output: 0.2015158583139189
}
hubs {
  node: "4"
  output: 0.13604957690850644
}
hubs {
  node: "5"
  output: 0.08121728238878734
}
hubs {
  node: "6"
  output: 0.08121728238878734
}
hubs {
  node: "7"
  output: 0.08121728238878734
}
hubs {
  node: "8"
  output: 0.08121728238878734
}
authorities {
  node: "1"
  output: 0.13604957688814256
}
authorities {
  node: "2"
  output: 0.2015158585243154
}
authorities {
  node: "3"
  output: 0.2015158585243154
}
authorities {
  node: "4"
  output: 0.13604957688814256
}
authorities {
  node: "5"
  output: 0.08121728229377104
}
authorities {
  node: "6"
  output: 0.08121728229377104
}
authorities {
  node: "7"
  output: 0.08121728229377104
}
authorities {
  node: "8"
  output: 0.08121728229377104
}

```