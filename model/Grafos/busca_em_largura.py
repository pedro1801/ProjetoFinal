from collections import deque
import os
import networkx as nx
import matplotlib.pyplot as plt

class bfs:
    def __init__(self, grafo):
        self.grafo = grafo
        self.NumeroImg = 0

    def busca_em_largura(self, vertice_fonte):
        diretorio_saida = 'Imagens'
        if not os.path.exists(diretorio_saida):
            os.makedirs(diretorio_saida)
        visitados, fila = set(), deque([vertice_fonte])

        # Crie um grafo para representar o grafo original
        G = nx.Graph(self.grafo)
        node_colors = ['b' if node != vertice_fonte else 'g' for node in G.nodes()]

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                self.NumeroImg+=1
                # Atualize as cores dos nós
                node_colors = ['gray' if node == vertice else 'black' if node in visitados else 'white' for node in G.nodes()]

                # Atualize a imagem do grafo com as cores dos nós
                plt.clf()
                pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800)
                plt.savefig(os.path.join(diretorio_saida,f'image{self.NumeroImg}.png'))

                for vizinho in self.grafo[vertice]:
                    if vizinho not in visitados:
                        fila.extend([vizinho])

        return visitados
    def Inicialização():
        # Exemplo de uso
        grafo1 = {
            0: [1, 3],
            1: [4],
            2: [4, 5],
            3: [1],
            4: [3],
            5: [5]
        }


        vertice_origem = 0

        grafo1_obj = bfs(grafo1)
        vertices_visitados1 = grafo1_obj.busca_em_largura(vertice_origem)

