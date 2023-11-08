import networkx as nx
import matplotlib.pyplot as plt
import os

class dfs:
    def __init__(self):
        self.G = nx.Graph()
        self.visited = set()
        self.currently_visiting = None
        self.NumeroImg = 0
    def busca_em_profundidade(self, grafo, vertice):
        self.NumeroImg = self.NumeroImg + 1
        diretorio_saida = 'Imagens'
        if not os.path.exists(diretorio_saida):
            os.makedirs(diretorio_saida)
        if vertice not in self.visited:
            self.visited.add(vertice)
            self.currently_visiting = vertice
            #print(f'Visitando vértice: {vertice}')
            vizinhos = grafo[vertice]
            #print(f'Os vizinhos do vértice {vertice} são: {vizinhos}')
            for vizinho in vizinhos:
                self.G.add_edge(vertice, vizinho)
                plt.clf()
                node_colors = self.color_nodes()
                nx.draw(self.G, with_labels=True, node_color=node_colors)
                plt.savefig(os.path.join(diretorio_saida,f'image{self.NumeroImg}.png'))
                self.busca_em_profundidade(grafo, vizinho)

    def color_nodes(self):
        node_colors = []
        for node in self.G.nodes:
            if node == self.currently_visiting:
                node_colors.append('black')  # Atualmente visitado (verde)
            elif node in self.visited:
                node_colors.append('gray')  # Visitado anteriormente (azul)
            else:
                node_colors.append('white')  # Não visitado
        return node_colors
    def Inicialização():
        grafo = {
            0: [1, 3],
            1: [4],
            2: [],
            3: [1],
            4: [],
        }
        
        dfs_instancia = dfs()
        dfs_instancia.busca_em_profundidade(grafo, 0)