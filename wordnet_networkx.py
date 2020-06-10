# -*- coding: utf-8 -*-

from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib


def traverse(graph, start, node):
    graph.depth[node.name()] = node.shortest_path_distance(start)
    for child in node.hyponyms():
        graph.add_edge(node.name(), child.name())
        traverse(graph, start, child)


def hyponym_graph(start):
    G = nx.Graph()
    G.depth = {}
    traverse(G, start, start)
    return G


def draw_graph(graph):
    nx.draw(graph, 
                     node_size = [16 * graph.degree(n) for n in graph],
                     node_color = [graph.depth[n] for n in graph],
                     #with_labels = False,
                     with_labels = True,
                    )
    matplotlib.pyplot.show()


if __name__ == '__main__':
    car = wn.synset('car.n.01')
    car = wn.synset('dog.n.01')
    car = wn.synset('computer.n.01')
    graph=hyponym_graph(car)
    draw_graph(graph)


