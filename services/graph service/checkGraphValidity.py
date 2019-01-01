

class Graphs:

    def __init__(self):


        pass

    def isValidMinNodesGraph(self,graph,source_node,target_node):
       # make sure the edges are in a proper format
        if(not(isinstance(graph['edges'],list))):
            return [False, 'the supplied edge is not type array']

        # make sure there is at least more than one node given
        if(len(graph['nodes']) < 1):
            return [False, 'graph should at least contain two nodes']

        # make sure there is at least one edge given
        if(len(graph['edges']) < 1):
            return [False, 'graph should at least contain one edge']
        #check if edges in graph is an array and a proper edge list ------------- to graphs.py check 
        for i in range(len(graph['edges'])):
            if(not(isinstance(graph['edges'][i],list))):
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array'.format(i)]
            if(len(graph['edges'][i]) != 2):
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain two nodes'.format(i)]
            if graph['edges'][i][0] is '' or graph['edges'][i][0] is None or graph['edges'][i][1] is '' or graph['edges'][i][1] is None:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does contain an empty node'.format(i)]
            
            # make sure all nodes specified in the edges exist in the nodes list
            if(not(graph['edges'][i][0] in graph['nodes'])):
                
                return [False, 'node {} doesn’t exist in the graph'.format(graph['edges'][i][0])]
                #graph['nodes'].append(graph['edges'][i][0])
            if(not(graph['edges'][i][1] in graph['nodes'])):
                return [False, 'node {} doesn’t exist in the graph'.format(graph['edges'][i][1])]
                #graph['nodes'].append(graph['edges'][i][1])
        
        return [True]  

    

    def isValidMostImportantGraph(self, graph, source_nodes, target_nodes, T=0, normalized=True, directed=False):
        # make sure the edges are in a proper format
        if(not(isinstance(graph['edges'],list))):
            return [False, 'the supplied edge is not type array']

        if 'weights' in graph:
            if(not(isinstance(graph['weights'],list))):
                return [False, 'the supplied weight is not type array']
            if(len(graph['edges']) != len(graph['weights'])):
                return [False, 'the length of supplied edges and weights does not match']


        # make sure there is at least more than one node given
        if(len(graph['nodes']) < 1):
            return [False, 'graph should at least contain two nodes']

        # make sure there is at least one edge given
        if(len(graph['edges']) < 1):
            return [False, 'graph should at least contain one edge']
       
        for i in range(len(graph['edges'])):
            if(not(isinstance(graph['edges'][i],list))):
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array'.format(i)]
            if(len(graph['edges'][i]) != 2):
                return [False, 'Element of the input array edges at zero-indexed poistion {} does not contain two nodes'.format(i)]
            if graph['edges'][i][0] is '' or graph['edges'][i][0] is None or graph['edges'][i][1] is '' or graph['edges'][i][1] is None:
                return [False, 'Element of the input array edges at zero-indexed poistion {} does contain an empty node'.format(i)]

            # make sure all nodes specified in the edges exist in the nodes list
            if(not(graph['edges'][i][0] in graph['nodes'])):
                
                return [False, 'node {} doesn’t exist in the graph'.format(graph['edges'][i][0])]
                #graph['nodes'].append(graph['edges'][i][0])
            if(not(graph['edges'][i][1] in graph['nodes'])):
                return [False, 'node {} doesn’t exist in the graph'.format(graph['edges'][i][1])]
                #graph['nodes'].append(graph['edges'][i][1])

        # make sure source_nodes and target_nodes are a 1D array
        if(not(isinstance(source_nodes,list))):
            return [False, 'Element of the input source_nodes is not an array']
        if(not(isinstance(target_nodes,list))):
            return [False, 'Element of the input target_nodes is not an array']

       
       # make sure source_node and target_node exist in the graph
        if (not(all(elem in graph['nodes']  for elem in source_nodes))):    
            diff = list(set(source_nodes).difference(graph['nodes']))
            return [False, 'node {} doesn’t exist in the graph'.format(diff[0])]

        if(not(all(elem in graph['nodes']  for elem in target_nodes))):
            diff = list(set(target_nodes).difference(graph['nodes']))
            return [False, 'node {} doesn’t exist in the graph'.format(diff[0])]


        if(T != 0 and T != 1 ):
            return [False, 'Parameter T can only be 0 or 1']

        return [True]    




__end__ = '__end__'