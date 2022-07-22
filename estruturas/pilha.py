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
    
    """Imprime o topo da lista"""
    def __repr__(self) -> str:
        return "[Topo: " + str(self.topo) + "]"
    
    """Empilha um novo dado na estrutura"""
    def push(self, dado):
        novo_nodo = NodoPilha(dado)
        novo_nodo.proximo_nodo = self.topo
        self.topo = novo_nodo
