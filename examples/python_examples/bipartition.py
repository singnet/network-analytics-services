import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import random
import plotly as py
import plotly.graph_objs as go
import time
import math




class graphx:

    def __init__(self):

        # self.file = "book_readers"
        self.file = "food_pref"
        self.num_nodes = 0

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

        # Adding random locations for the nodes
        # Put towards center nodes that have the most connections perhaps?

        # Get descending list of nodes
        print('Degrees')
        print(self.B.degree())
        sorted_by_second = sorted(list(self.B.degree()), key=lambda tup: tup[1], reverse=True)
        sorted_nodes_list = []
        for s in sorted_by_second:
            sorted_nodes_list.append(s[0])
        print(sorted_nodes_list)
        print(sorted_nodes_list.__len__())

        interval = 0.5/float(len(self.B))
        print("interval =",interval)

        i = 0

        for node in self.B.nodes(data=True):

            # node[1]['pos'] = [random.uniform(0,1),random.uniform(0,1)]

            # theta = primes[i] * 2 * math.pi / 8
            theta = random.uniform(0.01,2 * math.pi-0.01)
            r = i * interval

            x = r * math.cos(theta) + 0.5
            y = r * math.sin(theta) + 0.5

            print(x,y)

            node[1]['pos'] = [x,y]

            i = i + 1


        # self.plot_graph(self.B,self.file)
        self.plot_graph_2(self.B,'Initial bipartite graph')

    def projected_graph(self):
        E = bipartite.sets(self.B)[0]
        P = bipartite.projected_graph(self.B, E,multigraph=False)
        # self.plot_graph(P,'projected_gragh')
        self.plot_graph_2(P,'projected_gragh')
        print('projected_graph:number of edges:',P.number_of_edges())
        print(P.edges())
        print(list(P.edges(data=True)))

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

        # self.plot_graph(P,'weighted_projected')
        self.plot_graph_2(P,'weighted_projected')
        print('weighted_projected:number of edges:', P.number_of_edges())
        print(P.edges())
        print(list(P.edges(data=True)))

    def collaboration_weighted_projected_graph(self):
        E = bipartite.sets(self.B)[0]
        P = bipartite.collaboration_weighted_projected_graph(self.B, E)
        self.plot_graph_2(P,'collaboration_weighted_projected')
        print('collaboration_weighted_projected:number of edges:', P.number_of_edges())
        print(P.edges())
        print(list(P.edges(data=True)))

    def overlap_weighted_projected_graph(self):
        E = bipartite.sets(self.B)[0]
        P = bipartite.overlap_weighted_projected_graph(self.B, E,jaccard=False)
        self.plot_graph_2(P,'overlap_weighted_projected_graph')
        print('overlap_weighted_projected_graph:number of edges:', P.number_of_edges())
        print(P.edges())
        print(list(P.edges(data=True)))

    # ===============================================================
    # Assorted utilities and accessor functions
    # ===============================================================


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

    def plot_graph_2(self, G,graph_label):


        edge_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        edge_weight_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode='markers+text',
            textposition='top center',
            marker=go.Marker(
                opacity=0
            )
        )


        for edge in G.edges(data=True):
            x0, y0 = G.node[edge[0]]['pos']
            x1, y1 = G.node[edge[1]]['pos']
            edge_trace['x'] += [x0, x1, None]
            edge_trace['y'] += [y0, y1, None]

            edge_weight_trace['x'].append((x0+x1)/2)
            edge_weight_trace['y'].append((y0+y1)/2)
            try:
                print('||||||||||||||||||||||||||||||')
                print(edge)
                edge_weight_trace['text'].append(round(edge[2]['weight'],3))
            except:
                print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                edge_weight_trace['text'].append('')

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode='markers+text',
            textposition='bottom center'
            )

        for node in G.nodes():
            x, y = G.node[node]['pos']
            node_trace['x'].append(x)
            node_trace['y'].append(y)
            node_trace['text'].append(node)


        layout = go.Layout(
            title='<br>'+graph_label,
            titlefont=dict(size=16),
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            annotations=[dict(
                text='Network graph made for SNet',
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002)],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

        fig = go.Figure(data=[edge_trace, node_trace, edge_weight_trace],layout=layout)


        py.offline.plot(fig, filename=graph_label+'.html')


    def plot_graph_3(self):

        G = nx.random_geometric_graph(self.num_nodes, 1)
        pos = nx.get_node_attributes(G, 'pos')

        dmin = 1
        ncenter = 0
        for n in pos:
            x, y = pos[n]
            d = (x - 0.5) ** 2 + (y - 0.5) ** 2
            if d < dmin:
                ncenter = n
                dmin = d

        p = nx.single_source_shortest_path_length(G, ncenter)

        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        for edge in G.edges():
            x0, y0 = G.node[edge[0]]['pos']
            x1, y1 = G.node[edge[1]]['pos']
            edge_trace['x'] += [x0, x1, None]
            edge_trace['y'] += [y0, y1, None]

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                # colorscale options
                # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
                # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
                colorscale='YIGnBu',
                reversescale=True,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=2)))

        for node in G.nodes():
            x, y = G.node[node]['pos']
            node_trace['x'].append(x)
            node_trace['y'].append(y)

        fig = go.Figure(data=[edge_trace, node_trace],
                     layout=go.Layout(
                         title='<br>Network graph made with Python',
                         titlefont=dict(size=16),
                         showlegend=False,
                         hovermode='closest',
                         margin=dict(b=20, l=5, r=5, t=40),
                         annotations=[dict(
                             text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                             showarrow=False,
                             xref="paper", yref="paper",
                             x=0.005, y=-0.002)],
                         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

        py.offline.plot(fig, filename='networkx.html')

    def prime(self,i, primes):
        for prime in primes:
            if not (i == prime or i % prime):
                return False
        primes.append(i)
        return i

    def return_primes(self,n):
        primes = []
        i, p = 2, 0
        while True:
            if self.prime(i, primes):
                p += 1
                if p == n:
                    return primes
            i += 1



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





def run_create_bipartite_graph():
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

def run_combined_graphs():
    bi = graphx()
    bi.create_bipartite_graph()
    bi.projected_graph()
    bi.weighted_projected_graph()
    bi.collaboration_weighted_projected_graph()
    bi.overlap_weighted_projected_graph()

if __name__ == '__main__':

    sample_data_generation('book_readers.csv')

    run_combined_graphs()
    # run_overlap_weighted_projected_graph()
    # run_collaboration_weighted_projected_graph()
    # run_weighted_projected_graph()
    # run_projected_graph()
    # run_create_bipartite_graph()
    #
