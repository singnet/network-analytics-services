# Tested on python3.6

class Graphs:

    def __init__(self):

        pass

    def is_valid_graph(self, graph):
        # make sure there are at least two nodes
        if not (isinstance(graph['nodes'], list)):
            return [False, 'the supplied nodes is not type array']

            # make sure the edges are in a proper format
        if not (isinstance(graph['edges'], list)):
            return [False, 'the supplied edge is not type array']

            # make sure there is at least more than one node given
        if len(graph['nodes']) < 1:
            return [False, 'graph should at least contain two nodes']

        # make sure there is at least one edge given
        if len(graph['edges']) < 1:
            return [False, 'graph should at least contain one edge']

        # make sure the edges supplied are in proper format       
        for i in range(len(graph['edges'])):
            if not (isinstance(graph['edges'][i], list)):
                return [False, 'Element of the input array edges at zero-indexed poistion {} is not an array'.format(i)]
            if len(graph['edges'][i]) != 2:
                return [False,
                        'Element of the input array edges at zero-indexed poistion {} does not contain two nodes'.format(
                            i)]
            if graph['edges'][i][0] is '' or graph['edges'][i][0] is None or graph['edges'][i][1] is '' or \
                    graph['edges'][i][1] is None:
                return [False,
                        'Element of the input array edges at zero-indexed poistion {} does contain an empty node'.format(
                            i)]

            # make sure all nodes specified in the edges exist in the nodes list
            if(not(graph['edges'][i][0] in graph['nodes'])):
                return [False, "edge value at ["+ str(i) + "][0] is not a node"]
                #return [False, 'node {} doesn’t exist in the graph'.format(graph['edges'][i][0])]
                #graph['nodes'].append(graph['edges'][i][0])
            if(not(graph['edges'][i][1] in graph['nodes'])):
              return [False, "edge value at ["+ str(i) + "][1] is not a node"]
                #return [False, 'node {} doesn’t exist in the graph'.format(graph['edges'][i][1])]


                

        # Weight related test
        try:
            if len(graph['weights']) != 0 and len(graph['weights']) != len(graph['edges']):
                return [False, 'the length of supplied edges and weights does not match']
        except Exception as e:
            # weight is empty
            pass

        return [True]

    def is_valid_min_nodes_graph(self, graph, source_node, target_node):

        isValid = self.is_valid_graph(graph)
        print(isValid[0])

        if isValid[0]:
            # check source node and target node
            if not (source_node in graph['nodes']):
                return [False, 'The source node does not exist in graph']
            if not (target_node in graph['nodes']):
                return [False, "The target node does not exist in graph"]

            return [True]

        else:
            return isValid

    def is_valid_most_important_graph(self, graph, source_nodes, target_nodes, T=0):

        # make sure graph is correct

        isValid = self.is_valid_graph(graph)
        print(isValid[0])

        if isValid[0]:
            if not (isinstance(graph['edges'], list)):
                return [False, 'the supplied edge is not type array']

            if 'weights' in graph:
                if not (isinstance(graph['weights'], list)):
                    return [False, 'the supplied weight is not type array']
                if len(graph['edges']) != len(graph['weights']):
                    return [False, 'the length of supplied edges and weights does not match']
                #the edge weights must be greater than zero     
                if(0 in graph['weights']):
                    return [False, 'all edge weights must be greater than zero']   


                # the edge weights must be greater than zero
                if not all(i > 0 for i in graph['weights']):
                    return [False, 'all edge weights must be greater than zero']


                    # make sure source_nodes and target_nodes are a 1D array
            if not (isinstance(source_nodes, list)):
                return [False, 'Element of the input source_nodes is not an array']
            if not (isinstance(target_nodes, list)):
                return [False, 'Element of the input target_nodes is not an array']

            # make sure source_node and target_node exist in the graph
            for i in range(len(source_nodes)):
                if not (source_nodes[i] in graph['nodes']):
                    return [False, "source_nodes [" + str(i) + "] does not exist in graph"]

            # make sure source_node and target_node exist in the graph
            for i in range(len(target_nodes)):
                if not (target_nodes[i] in graph['nodes']):
                    return [False, "target_nodes [" + str(i) + "] does not exist in graph"]

            if T != 0 and T != 1:
                return [False, 'Parameter T can only be 0 or 1']

            return [True]


        else:
            return isValid


    def is_valid_pagerank(self, graph,personalization,dangling,nstart):

        # Personalization check

        if personalization is not None:
            c = 0
            for v in personalization:
                if v not in graph['nodes']:
                    return False,'personalization parameter contains a node at zero-indexed position {} that does not exist in the graph'.format(c),{}
                c = c + 1

            if not any(i != 0 for i in list(personalization.values())):
                return False, 'one personalization value should at lease be non-zero'

        # nstart check

        if nstart is not None:
            c = 0
            for v in nstart:
                if v not in graph['nodes']:
                    return False,'nstart parameter contains a node at zero-indexed position {} that does not exist in the graph'.format(c),{}
                c = c + 1

        # dangling check

        if dangling is not None:
            c = 0
            for v in dangling:
                if v not in graph['nodes']:
                    return False,'dangling parameter contains a node at zero-indexed position {} that does not exist in the graph'.format(c),{}
                c = c + 1

        return [True]


    def is_valid_eigenvector_centrality(self, graph,nstart):


        # nstart check

        if nstart is not None:
            c = 0
            for v in nstart:
                if v not in graph['nodes']:
                    return False,'nstart parameter contains a node at zero-indexed position {} that does not exist in the graph'.format(c),{}
                c = c + 1

            if not any(i != 0 for i in list(nstart.values())):
                return False, 'one nstart value should at lease be non-zero'


        return [True]


    def is_valid_hits(self, graph,nstart):


        # nstart check

        if nstart is not None:
            c = 0
            for v in nstart:
                if v not in graph['nodes']:
                    return False,'nstart parameter contains a node at zero-indexed position {} that does not exist in the graph'.format(c),{}
                c = c + 1



        return [True]



__end__ = '__end__'

