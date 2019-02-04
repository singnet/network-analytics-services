[![SingnetLogo](../../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')](https://singularitynet.io/)

# Robustness Services


## Methods

* [MinNodesToRemove](#minnodestoremove)
* [MostImportantNodesEdgesSubset](#mostimportantnodesedgessubset)

## MinNodesToRemove

Identify the minimum set of nodes or edges that need to be removed to block messages between two nodes in the network

### Inputs

* A graph (required)
* source_node  (required)
* target_node (required)

#### Sample input

Sample inputs using the dApp are as below. For each input, you can use either a text input field or a file input field with the following format.

```
Graph
Nodes:1,2,3,4,5,6
Edges:1,2;1,4;2,3;2,5;3,4;3,6;4,6
Source node:1
Target node:6
```

Sample call while using the SingularityNET CLI terminal application

```
snet client call 942  0.00000001 service_ip:port  MinNodesToRemove  query_minnodes.json
```

where the content of the file `query_minnodes.json` is

```
{
 "graph": {
        "nodes": ["1","2","3","4","5","6"],
        "edges": [{"edge": ["1","2"]},{"edge": ["1","4"]},{"edge": ["2","3"]},{"edge": ["2","5"]},{"edge": ["3","4"]},{"edge": ["3","6"]},{"edge": ["4","6"]}]
        },
        "source_node" : "1",
        "target_node" : "6"
}

```

#### Sample output

```
{"status": true
 "message": "success"
 "nodes_output" : ["3","4"]
 "edges_output" : [{"edge":["4", "6"]}, {"edge":["3","6"]}]
}
```

## MostImportantNodesEdgesSubset

Identify the most important nodes/edges between groups of nodes.

### Inputs

* A graph (required). Weight parameter in the graph is optional
* Source nodes  (required)
* Target nodes (required)
* Type (optional): Can assume either a value of 0 or 1. Defalut is 0 which would be used to calculate node betweeness; 1 for edge betweeeness.
* normalized (optional): Default is False. If True the betweenness values are normalized by `2/((n−1)(n−2))` for graphs, and `1/((n−1)(n−2))` for directed graphs where n is the number of nodes in G.
* directed (optional): Default is False, that is input graph is assumed undirected graph

#### Sample input

Sample inputs using the dApp are as below. For each input, you can use either a text input field or a file input field with the following format.

```
Graph
Nodes:1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Edges:1,2;1,4;2,3;2,5;3,4;3,6;2,7;3,8;7,9;5,9;9,10;10,6
Source nodes:5,7
Target nodes:6
Type:
normalized:
directed:true
```

Sample call while using the SingularityNET CLI terminal application

```
snet client call 942  0.00000001 service_ip:port  MostImportantNodesEdgesSubset query_bet.json
```

where the content of the file `query_bet.json` is

```
{
      "graph":
       {
            "nodes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            "edges": [{"edge": ["1", "2"]}, {"edge": ["1", "4"]}, {"edge": ["2", "3"]}, {"edge": ["2", "5"]}, {"edge": ["3", "4"]}, {"edge": ["3", "6"]}, {"edge": ["2", "7"]}, {"edge": ["3", "8"]}, {"edge": ["7", "9"]}, {"edge": ["5", "9"]},{"edge": ["9", "10"]}, {"edge": ["10", "6"]}]

        },

        "source_nodes" : ["5","7"],
        "target_nodes" : ["6"],
        "directed":true
}
```

#### Sample output

```
{"status":true,
"message":"success",
"node_betweenness_centrality": {
  node: ["9","10"],
  node_centrality_value: 2.0
}

```





