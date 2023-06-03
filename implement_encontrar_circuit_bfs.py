from collections import deque
# utilizamos o deque, para podermos retirarmos e adicionarmos de ambos os extremos da fila.

def encontrar_circuito(grafo):
    n = len(grafo)
    estado = ["nao_atingido"] * n
    # marcamos todos como nao atingidos, inicialmente.

    def tem_circuito(v):
        fila = deque()
        # o deque, seria double-ended-queue.
        fila.append(v)
        estado[v] = "no_caminho"  
        # marcamos o vértice como "no_caminho", apos enfileiramos ele.

        while fila:
            u = fila.popleft()
            # retiramos o prmeiro elemento.

            for vizinho in grafo[u]:
                # e para os vizinhos de saida dele, conferimos os estados.
                if estado[vizinho] == "no_caminho":
                    return True  
                  # encontramos um ciclo se pertencer ao caminho.

                if estado[vizinho] == "nao_atingido":
                    # se nao estiver, adicionamos esse.
                    fila.append(vizinho)
                    estado[vizinho] = "no_caminho"  
                    # e marcamos o vértice como "no_caminho".

            estado[u] = "finalizado"  
            # marcamos o vértice como "finalizado".

        return False

    # executamos a busca em largura para cada vértice do grafo.
    for v in range(n):
        if estado[v] == "nao_atingido" and tem_circuito(v):
            return True

    return False
