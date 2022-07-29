from estruturas.lista import ListaEncadeada
from estruturas.pilha import Pilha
#from grafos import bfs
import random

def cria_estado_aleatorio(pilhas):
    blocos = ["A", "B", "C"]
    while blocos:
        pilhas[random.randint(0, 2)].push(blocos.pop())

def cria_estado_obj(pilhas):
    pilhas[1].push("C")
    pilhas[1].push("B")
    pilhas[1].push("A")

if __name__ == "__main__":
    estado_ini = [Pilha(), Pilha(), Pilha()]
    estado_obj = [Pilha(), Pilha(), Pilha()]

    cria_estado_aleatorio(estado_ini)
    cria_estado_obj(estado_obj)

    print(estado_obj[1].contador)