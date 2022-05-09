# -*- coding: utf-8 -*-

class node:
    def __init__(self,chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)
    
    def inserir(self, vlr):
        atual = self
        if vlr > atual.chave and atual.chave == None:
            atual.chave = vlr
        elif vlr > atual.chave and atual.direita == None:
            atual.direita = node(vlr)
        elif vlr < atual.chave and atual.esquerda == None:
            atual.esquerda = node(vlr)
        else:
            return 'O valor não foi inserido na árvore'
                           


raiz = node(5)
raiz.inserir(2)
raiz.inserir(4)
raiz.inserir(3)
raiz.inserir(6)
raiz.inserir(7)            
print("Árvore: ", raiz.__repr__())
print(raiz.__repr__())
print(raiz.esquerda)
    