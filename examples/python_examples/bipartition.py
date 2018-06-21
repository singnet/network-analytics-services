import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import random




class graphx:

    def __init__(self):

        # self.file = "book_readers"
        self.file = "food_pref"

    # helper function to plot graphs
    def plot_graph(self, G, title, weight_name=None):
        '''
        G: a networkx G
        weight_name: name of the attribute for plotting edge weights (if G is weighted)
        '''
        # % matplotlib notebook

        plt.figure()
        plt.title(title)
        pos = nx.spring_layout(G)
        edges = G.edges()
        weights = None

        if weight_name:
            weights = [int(G[u][v][weight_name]) for u, v in edges]
            labels = nx.get_edge_attributes(G, weight_name)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            nx.draw_networkx(G, pos, edges=edges, width=weights)
        else:
            nx.draw_networkx(G, pos, edges=edges)

        plt.show()

    def create_bipartite_graph(self):

        self.read_file = "data/bipartite_data/"+self.file+".csv"
        self.file_df = pd.read_csv(self.read_file, encoding='ISO-8859-1')

        # This is the set of family members
        first_column = set(self.file_df.iloc[:,0])
        print(type(first_column))
        # This is the set of food types
        second_column = set(self.file_df.iloc[0,:])
        print(first_column)
        print(second_column)

        self.B = nx.Graph()
        self.B.add_nodes_from(first_column, bipartite=0)
        self.B.add_nodes_from(second_column, bipartite=1)
        self.B.add_edges_from(self.file_df.values.tolist())
        print((self.file_df.values))
        print((self.file_df.values.tolist()))

        self.plot_graph(self.B,self.file)

    def projected_graph(self):
        E = bipartite.sets(self.B)[0]
        P = bipartite.projected_graph(self.B, E,multigraph=True)
        self.plot_graph(P,'projected_gragh')

    def weighted_projected_graph(self):

        # set node types for family or food
        # print('faaaaaa')
        # for n in bipartite.sets(self.B)[0]:
        #     print(n)
        #     self.B.add_node(n, type='family')
        # print('foooooo')
        # for n in bipartite.sets(self.B)[1]:
        #     print(n)
        #     self.B.add_node(n, type='food')

        # print(bipartite.sets(B)[1])

        # create a projection on the 'family' nodes
        E = bipartite.sets(self.B)[0]
        P = bipartite.weighted_projected_graph(self.B,E,ratio=True)

        self.plot_graph(P,'weighted_projected')

    def collaboration_weighted_projected_graph(self):
        E = bipartite.sets(self.B)[0]
        P = bipartite.collaboration_weighted_projected_graph(self.B, E)
        self.plot_graph(P,'collaboration_weighted_projected')

    def overlap_weighted_projected_graph(self):
        E = bipartite.sets(self.B)[0]
        P = bipartite.overlap_weighted_projected_graph(self.B, E,jaccard=False)
        self.plot_graph(P,'overlap_weighted_projected_graph')



def sample_data_generation(file_name):

    persons = []
    books = []

    persons_count = 10
    books_count = 7
    books_per_person_count = 7

    for i in range(persons_count):
        persons.append('person_'+str(i))

    for i in range(books_count):
        books.append('book_'+str(i))

    print(persons)
    print(books)

    books_readers_bipartition = []

    for i in persons:
        indices_to_keep = random.sample(books,books_per_person_count)

        for j in indices_to_keep:
            books_readers_bipartition.append([i,j])

    print(books_readers_bipartition)

    print(len(books_readers_bipartition))

    pd.DataFrame(books_readers_bipartition,columns=['person','book']).to_csv('data/bipartite_data/'+file_name,index=False)






def run_sample_bipartite():
    bi = graphx()
    bi.create_bipartite_graph()

def run_projected_graph():
    bi = graphx()
    bi.create_bipartite_graph()
    bi.projected_graph()

def run_weighted_projected_graph():
    bi = graphx()
    bi.create_bipartite_graph()
    bi.weighted_projected_graph()

def run_collaboration_weighted_projected_graph():
    bi = graphx()
    bi.create_bipartite_graph()
    bi.collaboration_weighted_projected_graph()

def run_overlap_weighted_projected_graph():
    bi = graphx()
    bi.create_bipartite_graph()
    bi.overlap_weighted_projected_graph()



if __name__ == '__main__':

    sample_data_generation('book_readers.csv')

    # run_overlap_weighted_projected_graph()
    # run_collaboration_weighted_projected_graph()
    run_weighted_projected_graph()
    # run_projected_graph()
    # run_sample_bipartite()
    #
