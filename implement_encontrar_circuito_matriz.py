def tem_circuito(v, grafo, estado, visitados):
    estado[v] = "no_caminho"  
    # marcamos o vértice como "no_caminho".
    visitados[v] = True  
    # marcamos o vértice como visitado.

    for vizinho in grafo[v]:
        # percorrendo os vizinhos de saida.
        if estado[vizinho] == "no_caminho":
            # se estiverem no caminho, entao encontramos um ciclo.
            return True  
            # encontramos um ciclo.

        if estado[vizinho] == "nao_atingido" and tem_circuito(vizinho, grafo, estado):
            # aqui checando se nao foi atingido, e o chamado recursivo retorna verdadeiro.
            return True
            # se sim, tem circuito.

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
            # tem circuito.

    return False
