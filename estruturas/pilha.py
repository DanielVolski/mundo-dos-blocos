# Implementação da estrutura de dados do tipo pilha

class NodoPilha:
    """Construtor do nodo da pilha"""
    def __init__(self, dado = 0, proximo_nodo = None):
        self.dado = dado
        self.proximo_nodo = proximo_nodo
    
    """Gera o imprimível de NodoPilha"""
    def __repr__(self) -> str:
        return "%s -> %s" % (self.dado, self.proximo_nodo) 

class Pilha:

    def __init__(self):
        self.topo = None
        self.contador = 0
    
    """Imprime a pilha"""
    def __repr__(self) -> str:
        return "[Topo: " + str(self.topo) + "]"

    def __eq__(self, outro):
        return str(self) == str(outro)
    
    """Empilha um novo dado na estrutura"""
    def push(self, dado):
        novo_nodo = NodoPilha(dado)
        novo_nodo.proximo_nodo = self.topo
        self.topo = novo_nodo
        self.contador = self.contador + 1
    
    """Retira o dado que estiver no topo da pilha e o retorna"""
    def pop(self):
        if (self.topo != None):
            popped = self.topo
            self.topo = self.topo.proximo_nodo
            return popped
        else:
            raise Exception("Pilha vazia!")