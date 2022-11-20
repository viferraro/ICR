import networkx as nx
import numpy as np

Grafo = nx.Graph()

with open("C:\\Users\\vifer\\OneDrive\\Documents\\BSI\\7(5)Periodo\\ICR\\networks\\powergrid.edgelist.txt") as file:
    for linha in file:
        Grafo.add_edge(int(str(linha).split("	")[0]), int(str(linha).split("	")[1]))

    graus = []

    for no in Grafo.nodes():
        graus.append(nx.degree(Grafo, no))

print(f"Nº de vértices: {Grafo.number_of_nodes()}")
print(f"Nº de Arestas: {Grafo.number_of_edges()}")
print(f"Grau médio: {np.mean(graus)}")
print(f"Densidade: {nx.density(Grafo)}")
print(f"Media Menor Caminho: {nx.average_shortest_path_length(Grafo)}")
print(f"Clusterização global: {nx.transitivity(Grafo)}")
print(f"Clusterização local média: {nx.average_clustering(Grafo)}")

