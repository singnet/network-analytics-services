[![SingnetLogo](../../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')](https://singularitynet.io/)

# Bipartite Graph Services


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
snet client call 341  0.00000001 service_ip:port  BipartiteGraph query.json
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
{"status": true
 "message": "success"
 "output":{
    "nodes":
    {
           "bipartite_0": ["8", "7"],
           "bipartite_1": ["3", "4"]
           },

    "edges":[{"edge": ["3","8"]},{ "edge": ["4","7"] }]}
}
```

## ProjectedGraph

Returns the projection of a bipartite graph on a given set of nodes.


### Inputs

* A bipartite graph (required)
* A set of node nodes (required)
* Weight logic (requried): the ist of possible values are below (inputs are case-sensitive)

    - **none**: No weight is used. The corresponding networkx method called is “projected_graph” with multigraph=False.

    - **multigraph**: a multigraph where the multiple edges represent multiple shared neighbors. The edge key in the multigraph is assigned to the label of the neighbor. The corresponding networkx method called is “projected_graph” with multigraph=True.

    - **degree**: number of shared neighbors. The corresponding networkx method called is “weighted_projected_graph” with ration=False.

    - **degree_ratio**: ration between actual shared neighbors and possible shared neighbors. The corresponding networkx method called is “weighted_projected_graph” with ration=True.

    - **Newman**: The collaboration weighted projection is the projection of the bipartite network B onto the specified nodes with weights assigned using Newman’s collaboration Model. The corresponding networkx method called is “collaboration_weighted_projected_graph”.

    - **Jaccard**: Jaccard index between the neighborhoods of the two nodes in the original bipartite graph. The corresponding networkx method called is “overlap_weighted_projected_graph” with jaccard=True.

    - **Jaccard_modified**: the fraction of common neighbors by minimum of both nodes degree in the original bipartite Graph. The corresponding networkx method called is “overlap_weighted_projected_graph” with jaccard=True.

    - **generic**: user defined generic function. Not implemented yet.


#### Sample input

Sample inputs using the dApp are as below. For each input, you can use either a text input field or a file input field with the following format.

```
Bipartite Graph
First bipartite node:Pam,Goeff,Philip,Sam,Fred,Jane,Sue,Charlie
Second bipartite node:American Diner,Sushi,Italian,Indian,Chinese,Tapas,Thai,French,Hungarian,Lebanese,Greek
Edges:Pam,French;Pam,Hungarian;Pam,Sushi;Goeff,American Diner;Goeff,Indian;Goeff,Chinese;Philip,Lebanese;Philip,Italian;Philip,Tapas;Sam,American Diner;Sam,Sushi;Sam,Italian;Fred,Italian;Fred,Tapas;Fred,Thai;Jane,French;Jane,Hungarian;Jane,Sushi;Sue,Greek;Sue,Tapas;Sue,hai;Charlie,American Diner;Charlie,Indian;
Charlie,Chinese
Nodes:Pam,Charlie,Goeff,Fred,Sam,Sue,Philip,Jane
weight:Newman
```

Sample call while using the SingularityNET CLI terminal application

```
snet client call 360  0.00000001 service_ip:port  ProjectedGraph query_projected.json
```

where the content of the file `query_projected.json` is

```
{

    "graph":
           {
            "bipartite_0": ["Pam", "Goeff", "Philip", "Sam", "Fred", "Jane", "Sue", "Charlie"],
            "bipartite_1": ["American Diner", "Sushi", "Italian", "Indian", "Chinese", "Tapas", "Thai","French", "Hungarian", "Lebanese", "Greek"],
            "edges": [{"edge": ["Pam", "French"]}, {"edge": ["Pam", "Hungarian"]}, {"edge": ["Pam", "Sushi"]}, {"edge": ["Goeff", "American Diner"]},
                               {"edge": ["Goeff", "Indian"]}, {"edge": ["Goeff", "Chinese"]}, {"edge": ["Philip", "Lebanese"]}, {"edge": ["Philip", "Italian"]},
                               {"edge": ["Philip", "Tapas"]}, {"edge": ["Sam", "American Diner"]}, {"edge": ["Sam", "Sushi"]}, {"edge": ["Sam", "Italian"]},
                               {"edge": ["Fred", "Italian"]}, {"edge": ["Fred", "Tapas"]}, {"edge": ["Fred", "Thai"]}, {"edge": ["Jane", "French"]},
                               {"edge": ["Jane", "Hungarian"]}, {"edge": ["Jane", "Sushi"]}, {"edge": ["Sue", "Greek"]}, {"edge": ["Sue", "Tapas"]},
                               {"edge": ["Sue", "Thai"]}, {"edge": ["Charlie", "American Diner"]}, {"edge": ["Charlie", "Indian"]},
                               {"edge": ["Charlie", "Chinese"]}]
           },
     "nodes": ["Pam", "Charlie", "Goeff", "Fred", "Sam", "Sue", "Philip", "Jane"],
     "weight":"Newman"
}
```

#### Sample output

```
{"status":true,
"message":"success",
"output":{
  "nodes":["Pam","Charlie","Goeff","Fred","Sam","Sue","Philip","Jane"],
  "edges":[{"edge":["Pam","Jane"]},{"edge":["Pam","Sam"]},{"edge":["Charlie","Goeff"]},{"edge":["Charlie","Sam"]},{"edge":["Goeff","Sam"]},
          {"edge":["Fred","Sue"]},{"edge":["Fred","Philip"]},{"edge":["Fred","Sam"]},{"edge":["Sam","Jane"]},{"edge":["Sam","Philip"]},{"edge":["Sue","Philip"]}],
          "weights":[2.5,0.5,2.5,0.5,0.5,1.5,1,0.5,0.5,0.5,0.5]}
}
```





