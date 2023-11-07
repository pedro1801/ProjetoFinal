import networkx as nx
import matplotlib.pyplot as plt

class dfs:
    def __init__(self):
        self.G = nx.Graph()
        self.visited = set()
        self.currently_visiting = None

    def busca_em_profundidade(self, grafo, vertice):
        if vertice not in self.visited:
            self.visited.add(vertice)
            self.currently_visiting = vertice
            print(f'Visitando vértice: {vertice}')
            vizinhos = grafo[vertice]
            print(f'Os vizinhos do vértice {vertice} são: {vizinhos}')
            for vizinho in vizinhos:
                self.G.add_edge(vertice, vizinho)
                plt.clf()
                node_colors = self.color_nodes()
                nx.draw(self.G, with_labels=True, node_color=node_colors)
                plt.pause(1)
                self.busca_em_profundidade(grafo, vizinho)

    def color_nodes(self):
        node_colors = []
        for node in self.G.nodes:
            if node == self.currently_visiting:
                node_colors.append('green')  # Atualmente visitado (verde)
            elif node in self.visited:
                node_colors.append('blue')  # Visitado anteriormente (azul)
            else:
                node_colors.append('red')  # Não visitado
        return node_colors

grafo = {
    0: [1, 3],
    1: [4],
    2: [],
    3: [1],
    4: [],
}

dfs_instancia = dfs()
dfs_instancia.busca_em_profundidade(grafo, 0)
plt.show()  # Mantém a última imagem aberta
