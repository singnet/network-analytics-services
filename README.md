# Network Analysis Service

Network analysis service for SingularityNET. Below is a list of currently available services
under different categories. Also detailed services input/output specifications.

## List of Services

### Bipartite Graphs

Bipartite Graph: Create a bipartite graph from two given nodes and a set of edges

Projected Graph: Returns the projection of a bipartite graph on a given set of nodes.

## Input/Output Service Specification

### Service:Bipartite Graph

**Description**: Create a bipartite graph from two given nodes
and a set of edges.

**Service endpoint**: bipartite_graph

**input_0**: Bipartition nodes

input name: nodes

sample input:

```
{
 “bipartite_0”:[bipartite_0_node_0,bipartite_0_node_1,...],
 “bipartite_1”:[bipartite_1_node_0,bipartite_1_node_1,...]
}
```
**input_1**: A two dimensional array

input name: edges

sample input:

```
[[bipartite_0_node_0,bipartite_1_node_1],[],[]]]
```

**output**: If no error is raised, a concatenation of input_0 with input_1 is returned along with a boolean true and a ‘success’ text message. If an error is raised a false boolean value is returned along with a specific error message and an empty graph {}.

sample output 1 for error free invocation:

```
{
“status”: ture,
“message”: success,
“output”:{ “bipartite_0”:[bipartite_0_node_0,bipartite_0_node_1,...],
           “bipartite_1”:[bipartite_1_node_0,bipartite_1_node_1,...],
“edges”:[[bipartite_0_node_0,bipartite_1_node_1],[],[]]]
}
}
```
sample output 2 for error invocation:

```
{
"status": false,
"message": "Edge element at zero-indexed position 0 is not contained in either of the bipartitions",
"output": {} }
```

**Error handling**:
1. All specified input arguments must be present as named above. And arrays should be used strictly as indicated in some of the inputs.
2. Making sure both input bipartitions contain at least one node
3. Making sure that an element exists only in a single bipartition, that is input bipartition graph is a valid one.
4. Make sure that edges is a two-d array and has at least one element
5. With respect to the validity of edges provided, given an edge [bipartite_0_node_x,bipartite_1_node_y], if either of the elements doesn’t belong to the respective bipartition_0 or bipartition_1, then an error occurs.
6. If no edge is formed in either steps 3, 4 or 5, then a bipartite would not be returned. Instead, an error message would be returned.


### Service:Projected Graph

**Description**: Returns the projection of a bipartite graph on a given set of nodes.

**Service endpoint**: projected_graph

**input_0**: Input bipartite graph as given below

input name: bipartite_graph

sample input:

```
{ “bipartite_0”:[bipartite_0_node_0,bipartite_0_node_1,...],
  “bipartite_1”:[bipartite_1_node_0,bipartite_1_node_1,...],
  “edges”:[[bipartite_0_node_0,bipartite_1_node_1],[],[]]]
}
```
**input_1**: Nodes to project onto

input name: nodes

sample input: An array of nodes to project onto

**input_2**: Edge weight logic.

input name: weight

List of possible values: inputs are case-sensitive

***none***: No weight is used. The corresponding networkx method called is “projected_graph” with multigraph=False.

***multigraph***: a multigraph where the multiple edges
represent multiple shared neighbors. The edge key in the
multigraph is assigned to the label of the neighbor. The corresponding networkx method called is “projected_graph” with multigraph=True.

***degree***: number of shared neighbors. The corresponding networkx method called is “weighted_projected_graph” with ration=False.

***degree_ratio***: ration between actual shared neighbors and
possible shared neighbors. The corresponding networkx method called is “weighted_projected_graph” with ration=True.

***Newman***: The collaboration weighted projection is the
projection of the bipartite network B onto the specified
nodes with weights assigned using Newman’s collaboration
Model. The corresponding networkx method called is “collaboration_weighted_projected_graph”.

***Jaccard***: Jaccard index between the neighborhoods of
the two nodes in the original bipartite graph. The corresponding networkx method called is “overlap_weighted_projected_graph” with jaccard=True.

***Jaccard_modified***: the fraction of common neighbors by
minimum of both nodes degree in the original bipartite
Graph. The corresponding networkx method called is “overlap_weighted_projected_graph” with jaccard=True.

***generic***: user defined generic function. Not implemented yet.

***output***: projected graph

sample output 1 for error free invocation:

```
{
“status”: ture,
“message”: “success”,
“output”:{
“nodes”:[node_0,node_1,...], “edges”:[[node_0,node_2],[node_10,node_1],...],
“weights”:[weight_for_first_edge,weight_for_second_edge,...]
}
}
```

sample output 2 for error invocation:

```
{
“status”: false,
“message”: “error message”,
“output”:{}
}
```
**Error handling**:
1. All specified input arguments must be present as named above. And arrays should be used strictly as indicated in some of the inputs.
2. Input bipartite graph must be a valid one. Error handling steps from 1 to 5 are executed from the “Bipartite Graph” service above.
3. Nodes to project onto has at least one element is an array
4. If nodes contain more than one element, then all elements should come from one bipartition
5. If an unknown weighting technique is specified then an error is returned

