import networkx as nx
import matplotlib.pyplot as plt
import os

# Criar um objeto de grafo
class Teste:
    def __init__(self,valor):
        self.valor = valor
        def secundaria():

            print("DEntro")
            G = nx.Graph()

            # Adicionar nós
            G.add_node(1)
            G.add_node(2)
            G.add_node(3)

            # Adicionar arestas
            G.add_edge(1, 2)
            G.add_edge(2, 3)
            G.add_edge(3, 1)

            # Plotar o grafo
            pos = nx.spring_layout(G)  # Layout para posicionar os nós
            nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_color='black', font_weight='bold')
            plt.show()
            diretorio_saida = "Imagens"
            plt.savefig(os.path.join(diretorio_saida,f'image.png'))
        if self.valor == 1:
            secundaria()