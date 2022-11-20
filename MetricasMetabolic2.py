import networkx as nx
import numpy as np

Grafo = nx.DiGraph()

with open("C:\\Users\\vifer\\OneDrive\\Documents\\BSI\\7(5)Periodo\\ICR\\networks\\metabolic.edgelist.txt") as file:
    for linha in file:
        Grafo.add_edge(int(str(linha).split("	")[0]), int(str(linha).split("	")[1]))

    graus = []
    for no in Grafo.nodes():
        graus.append(nx.degree(Grafo, no)/2)


print(f"Nº de nós: {Grafo.number_of_nodes()}")
print(f"Nº de Arestas: {Grafo.number_of_edges()}")
print(f"Grau médio: {np.mean(graus)}")
print(f"Densidade: {nx.density(Grafo)}")
print(f"Cluster global: {nx.transitivity(Grafo)}")
print(f"Cluster médio: {nx.average_clustering(Grafo)}")
