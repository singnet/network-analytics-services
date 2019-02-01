[![SingnetLogo](../../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')](https://singularitynet.io/)

# Bipartite Graph Services

## Service endpoints

* Kovan: 159.69.56.49:2222
* Ropsten: 159.69.56.49:2232

## Methods

* [BipartiteGraph](#bipartitegraph)
* [ProjectedGraph](#projectedgraph)

## BipartiteGraph

Create a bipartite graph from two given nodes and a set of edges. Also making sure that the supplied graph is bipartite graph.
It will give specific error messages when the supplied graph can not be converted into a bipartite graph.

### Inputs

* Bipartition nodes (required): first set of nodes representing the bipartition
* Bipartition nodes (required): second set of nodes representing the bipartiion
* Edges (requried): A list of edges connection the first set of nodes with the second

#### Sample input

Sample inputs using the dApp are as below. For each input, you can use either a text input field or a file input field with the following format.

```
First node:8,7
Second node:3,4
Edges:3,8;4,7
```

Sample call while using the SingularityNET CLI terminal application

```
snet client call 341  0.00000001 159.69.56.49:2222  BipartiteGraph query.json
```

where the content of the file `query.json` is

```
{
    "nodes":
           {
           "bipartite_0": ["8", "7"],
           "bipartite_1": ["3", "4"]
           },

    "edges":[{"edge": ["3","8"]},{ "edge": ["4","7"] }]
}
```

#### Sample output

```
{
    "nodes":
           {
           "bipartite_0": ["8", "7"],
           "bipartite_1": ["3", "4"]
           },

    "edges":[{"edge": ["3","8"]},{ "edge": ["4","7"] }]
}
```



## ProjectedGraph

Returns the projection of a bipartite graph on a given set of nodes.



