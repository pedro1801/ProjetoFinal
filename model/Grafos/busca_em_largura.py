from collections import deque

class bfs:
    def __init__(self, grafo):
        self.grafo = grafo

    def busca_em_largura(self, vertice_fonte):
        visitados, fila = set(), deque([vertice_fonte])
        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in self.grafo[vertice]:
                    if vizinho not in visitados:
                        fila.extend([vizinho])
        return visitados

# Exemplo de uso
grafo1 = {
    0: [1, 3],    # vizinhos do vértice 0
    1: [4],       # vizinhos do vértice 1
    2: [4, 5],    # vizinhos do vértice 2
    3: [1],       # vizinhos do vértice 3
    4: [3],       # vizinhos do vértice 4
    5: [5]        # vizinhos do vértice 5
}

grafo2 = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [6],
    5: [],
    6: []
}

vertice_origem = 0  # Vértice de origem da busca

grafo1_obj = bfs(grafo1)
vertices_visitados1 = grafo1_obj.busca_em_largura(vertice_origem)

grafo2_obj = bfs(grafo2)
vertices_visitados2 = grafo2_obj.busca_em_largura(vertice_origem)

print("Vértices visitados durante a BFS a partir do vértice", vertice_origem, "no grafo 1 são:", vertices_visitados1)
print("Vértices visitados durante a BFS a partir do vértice", vertice_origem, "no grafo 2 são:", vertices_visitados2)
