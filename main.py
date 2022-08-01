# Implementação principal
# Para a busca em largura foram utilizados como referência:
# O livro Algoritmos de Thomas Cormen
# O site https://favtutor.com/blogs/breadth-first-search-python

from estruturas.lista import ListaEncadeada
from estruturas.pilha import Pilha
import random
import copy
import time

def cria_estado_aleatorio(pilhas):
    blocos = ["A", "B", "C"]
    while blocos:
        pilhas[random.randint(0, 2)].push(blocos.pop())

def cria_estado_obj(pilhas):
    blocos = ["A", "B", "C"]
    while blocos:
        pilhas[1].push(blocos.pop())

def expande(pilhas):
    vertices = []
    for i in range(0, 3):
        if pilhas[i].contador == 0:
            continue
        else:
            temp1 = copy.deepcopy(pilhas)
            bloco = temp1[i].pop()
            for j in range(0, 3):
                temp2 = copy.deepcopy(temp1)
                if i != j:
                    temp2[j].push(bloco)
                    vertices.append(temp2)
    return vertices

def busca_largura(raiz, objetivo):
    vertices = []
    visitados = []
    nivel = 0
    vertices.append(raiz)
    visitados.append(raiz)

    #inicio = time.time()
    while vertices:
        vertice = vertices.pop()
        vizinhos = expande(vertice)
        nivel = nivel + 1
        for vizinho in vizinhos:
            if vizinho == objetivo:
                print("Resultado encontrado no nível " + str(nivel) + " da árvore!")
                return vizinho
            elif vizinho not in visitados:
                visitados.append(vizinho)
                vertices.append(vizinho)

if __name__ == "__main__":
    estado_ini = [Pilha(), Pilha(), Pilha()]
    estado_obj = [Pilha(), Pilha(), Pilha()]
    estado_teste = [Pilha(), Pilha(), Pilha()]

    cria_estado_aleatorio(estado_ini)
    cria_estado_aleatorio(estado_obj)

    print("Estado inicial: " + str(estado_ini))
    print("Estado objetivo:" + str(estado_obj))
    
    inicio = time.time()
    resultado = busca_largura(estado_ini, estado_obj)
    fim = time.time()
    print("Resultado: " + str(resultado))
    print("Tempo total: " + str(fim - inicio))