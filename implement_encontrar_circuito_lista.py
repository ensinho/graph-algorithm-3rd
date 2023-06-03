def tem_circuito(v, grafo, estado, visitados):
    estado[v] = "no_caminho"  
    # marcamos o vértice como "no_caminho".
    visitados[v] = True  
    # marcamos o vértice como visitado.

    for vizinho in grafo[v]:
        # percorrendo os vizinhos de saida do vertice.
        if estado[vizinho] == "no_caminho":
            return True  
          # se estiver no caminho, encontramos um ciclo.

        if estado[vizinho] == "nao_atingido" and tem_circuito(vizinho, grafo, estado, visitados):
            # se nao estiver visitado, mas chamarmos recursivamente e tiver circuito.
            return True
            # temos um circuito.

    estado[v] = "finalizado"  
    # marcamos o vértice como "finalizado".
    return False

def encontrar_circuito(grafo):
    n = len(grafo)
    estado = ["nao_atingido"] * n  
    # inicializamos todos os vértices como "nao_atingido".
    visitados = [False] * n  
    # inicializamos todos os vértices como não visitados.

    for v in range(n):
        if estado[v] == "nao_atingido" and tem_circuito(v, grafo, estado, visitados):
            return True

    return False
