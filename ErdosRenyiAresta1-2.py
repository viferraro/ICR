import random
import time
import networkx as nx
import numpy as np

def CriaGrafo(vertice):  #metodo para criar o grafo
    Grafo = nx.Graph()
    for no in range(vertice):  #cria os vértices
        Grafo.add_node(no)
    for x in range(vertice - 1):    #vertice
        for y in range(x + 1, vertice - 1):  #possibilidade de arestas com os demais vertices do grafo
            z = random.random()      # sorteio
            if z <= (10/vertice) and x != y:     #alinha o número sorteado com a probabilidade (10/n)   #não permite autolink
                if not Grafo.has_edge(y, x):   #não permite arestas duplicadas
                    Grafo.add_edge(x, y)    # adiciona as arestas
    return Grafo
n=4
tempo = 0
while(n<19):    #laço para gerar grafos com 2^4, 2^6, 2^8, 2^10, 2^12, 2^14, 2^16 e 2^18 vértices
    i = 0
    arestas = []
    densidades = []
    GrausMedios = []
    tempos = []
    while (i < 10):  # gera 10 grafos de cada (para calcular as médias)
        tempo1 = time.time_ns()   #tempo de referência (em nanosegundos)
        Grafo = CriaGrafo(2**n)   # gera o grafo segundo o numero de vertices
        tempo2 = time.time_ns()
        tempo = (tempo2 - tempo1)
        grau = []
        arestas.append(Grafo.number_of_edges())
        for no in Grafo.nodes():
            grau.append(nx.degree(Grafo, no))
        GrausMedios.append(np.mean(grau))
        densidades.append(nx.density(Grafo))
        tempos.append(tempo)
        i = i+1

    print(f"Nº de nós: {Grafo.number_of_nodes()}")
    print(f"Nº médio de Arestas: {np.mean(arestas)}")
    print(f"Média de Graus médios: {np.mean(GrausMedios)}")
    print(f"Média de Densidades: {np.mean(densidades)}")
    print(f"Média do tempo de processamento: {np.mean(tempos)}\n")
    n = n+2