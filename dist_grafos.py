#testes com matrizes de adjacencias

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_arestas(self,u,v,peso):
        #grafos nao direcionados
        self.grafo[u-1][v-1] = peso #caso seja multiplo, trocar o = por +=

    def mostrar_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])

#numero de vertices
v = int(input('Numero de vertices: '))
g = Grafo(v)

#numero de arestas
a = int(input("Numero de arestas: "))
for i in range(a):
    u = int(input("QUal vertice começa: "))
    v = int(input("Qual vertice termina: "))
    p = int(input("Valor: "))
    g.add_arestas(u, v, p)

g.mostrar_matriz()
