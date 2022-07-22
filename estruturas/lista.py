#
# Baseado na implementação disponível em:
# https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/listas-encadeadas/
#

"""Representa um único nodo de uma lista encadeada"""
class NodoLista:
    """Construtor da classe NodoLista"""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    """Gera o imprimível de um objeto NodoLista"""
    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo)

"""Representa uma lista encadeada"""
class ListaEncadeada:
    """Construtor da classe"""
    def __init__(self):
        self.cabeca = None

    """Torna o objeto imprímivel"""
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    """Insere um novo dado ao final da lista"""
    def inserir(self, dado):
        novo = NodoLista(dado)
        novo.proximo = self.cabeca
        self.cabeca = novo