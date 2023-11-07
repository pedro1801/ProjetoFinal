import networkx as nx
import matplotlib.pyplot as plt

class dfs:
    def __init__(self, grafo):
        self.grafo = grafo
        self.G = nx.Graph()

    def busca_em_profundidade(self, vertice_inicial):
        def busca_recursiva(vertice):
            visitados.add(vertice)
            print(f'Visitando vértice: {vertice}')
            vizinhos = self.grafo[vertice]
            print(f'Os vizinhos do vértice {vertice} são: {vizinhos}')
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    busca_recursiva(vizinho)

        visitados = set()
        busca_recursiva(vertice_inicial)
    
    def desenhar_grafo(self,grafo):
        for vertice, vizinhos in enumerate(self.grafo):
            self.G.add_node(vertice)
            for vizinho in vizinhos:
                self.G.add_edge(vertice, vizinho)

        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
        plt.axis('off')
        plt.savefig("grafo.png", format="PNG")
        plt.show()

grafo = [
    [1, 3],    # vizinhos do vertice 0
    [4],       # vizinhos do vertice 1
    [4, 5],    # vizinhos do vertice 2
    [1],       # vizinhos do vertice 3
    [3],       # vizinhos do vertice 4
    [5]        # vizinhos do vertice 5
]

x = dfs(grafo)
x.busca_em_profundidade(0)
x.desenhar_grafo(grafo)