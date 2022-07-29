from estruturas.lista import ListaEncadeada
from estruturas.pilha import Pilha

if __name__ == "__main__":
    lista = ListaEncadeada()

    lista.inserir(1)
    lista.inserir(2)

    print(lista)

    lista.remove(2)

    print(lista)