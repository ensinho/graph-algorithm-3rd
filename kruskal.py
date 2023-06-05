class No:
  # Definimos um nó.
    def __init__(self, elemento, proximo=None):
        self.elemento = elemento
        self.proximo = proximo

def kruskal(grafo):
    L = sorted(grafo, key=lambda x: x[2])  
    # Ordenar arestas por peso.
    A = set()
    represent = list(range(len(grafo)))  
    # Inicializar representantes.
    comp = [None] * len(grafo)

    for u in range(len(grafo)):
        comp[u] = No(u)  
        # Cria um nó para cada vértice e define como primeiro e último do conjunto.

    while len(A) != len(grafo) - 1:
        u, v, peso = L.pop(0) 
        # Remove a primeira aresta com menor peso.
        if represent[u] != represent[v]:  
          # Verifica se os vértices pertencem a conjuntos diferentes.
            A.add((u, v))  
            # Adiciona a aresta ao conjunto A.
            x = represent[u]
            y = represent[v]
            if comp[x].tamanho < comp[y].tamanho:  
              # Verifica o tamanho dos conjuntos.
                x, y = y, x  
                # Troca os representantes para manter o menor como representante.
            z = comp[y].primeiro  
            # Percorre os nós do conjunto menor.
            comp[x].ultimo.proximo = z  
            # Atualiza o último nó do conjunto maior.
            comp[x].ultimo = comp[y].ultimo  
            # Atualiza o último nó do conjunto maior.
            comp[x].tamanho += comp[y].tamanho  
            # Atualiza o tamanho do conjunto maior.
            while z is not None:
                represent[z.elemento] = x  
                # Atualiza os representantes dos vértices do conjunto menor.
                z = z.proximo

    return A
