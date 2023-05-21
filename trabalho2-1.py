import sys

class Aresta:
    def __init__(self, u, v, peso): #aqui criamos um componente aresta
        #com peso e os seus vertices.
        self.u = u
        self.v = v
        self.peso = peso 

def encontrar_comp(vertice, comps):
    #percorre recursivamente em busca se o vertice for igual ao seu representante
    #pois, sendo igual significa que ele é a raiz do conjunto.
    if comps[vertice] == vertice:
        return vertice
    return encontrar_comp(comps[vertice], comps)

def concatenar_conjuntos(raiz1, raiz2, comps, tam): 
    #recebendo as raizes dos conjuntos, o array comps representa a relaçao
    # dos representantes dos vertices.
    #função responsavel por unir os conjuntos disjuntos, vendo qual é maior
    #e quem apontará para quem.
    if tam[raiz1] > tam[raiz2]:
        comps[raiz2] = raiz1
    elif tam[raiz1] < tam[raiz2]:
        comps[raiz1] = raiz2
    else:
        comps[raiz2] = raiz1
        tam[raiz1] += 1

def calcular_peso_agm(arestas, num_vertices): #recebe as arestas do grafo e o total de vertices
    #a função começa ordenando de forma crescente utilizando o sort.
    arestas.sort(key=lambda aresta: aresta.peso)
    comps = [i for i in range(num_vertices + 1)] #aqui onde cada vertice seria um representante
    tam = [0] * (num_vertices + 1)
    peso_total = 0 

    #percorre as arestas em ordem, e confere se os vertices pertencem a conjuntos disjuntos.
    for aresta in arestas:
        raiz_u = encontrar_comp(aresta.u, comps)
        raiz_v = encontrar_comp(aresta.v, comps)
        #se nao pertencerem ao mesmo conjunto, a aresta é adicionada.
        if raiz_u != raiz_v:
            #adicionamos o peso da aresta para calcular.
            peso_total += aresta.peso
            #depois unimos os conjuntos.
            concatenar_conjuntos(raiz_u, raiz_v, comps, tam)

    return peso_total

#a função que faz o parse das entradas, assim criando a lista de arestas.
def parse_entrada(linhas_entrada):
    arestas = []
    inicio_dados = False

    #percorre as linhas de entrada para procurar a que indica o inicio.
    for linha in linhas_entrada:
        linha = linha.strip()

        #no caso, a que começa com "data".
        if linha.startswith("data:"):
            inicio_dados = True
            continue
    
        if inicio_dados and linha:
            #aqui divide em três valores, e convertendo eles conforme ir precisando.
            u, v, peso = map(float, linha.split())
            #em seguida, a aresta com os vertices e seus pesos.
            aresta = Aresta(int(u), int(v), peso)
            arestas.append(aresta)

    return arestas

def main():
    #chamado das funções referentes ao codigo.
    linhas_entrada = sys.stdin.readlines()
    arestas = parse_entrada(linhas_entrada)
    num_vertices = max(max(aresta.u, aresta.v) for aresta in arestas)
    peso_agm = calcular_peso_agm(arestas, num_vertices)
    print(f"{peso_agm:.3f}") #saindo em 3 casas decimais

#o bloco seguinte garante que o codigo dentro dele so sera executado se o script for executado diretamente
# nao importado como um modulo.
if __name__ == "__main__":
    main()
