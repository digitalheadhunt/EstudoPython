# -*- coding: utf-8 -*-

class No:
    def __init__(self, valor = None, esq = None, direita = None):
        self.valor = valor
        self.esq = esq
        self.direita = direita
        
    def mostra_no(self):
        return self.valor

class arvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []
        
    def inserir(self, valor):
        novo = No(valor)
        
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                #esquerda
                if valor < atual.valor:
                    atual = atual.esq
                    if atual == None:
                        pai.esq = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                #direita
                else:
                    atual = pai.direita
                    if atual == None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return

    def pesquisar(self,valor):
        atual = self.raiz
        while atual.valor != valor:
            
            if valor == atual.valor:
                return atual
            elif valor < atual.valor:
                atual = atual.esq
            else:
                atual = atual.direita
            if atual == None:
                return None        
        return atual     

    


three = arvoreBinariaBusca()

three.inserir(55)
three.inserir(35)
three.inserir(79)
three.inserir(29)
three.inserir(36)
three.inserir(69)
three.inserir(14)
three.inserir(81)
three.inserir(75)
three.inserir(15)
three.inserir(26)
three.inserir(65)
three.inserir(30)
three.inserir(98)
three.inserir(1)
print(three.ligacoes)
print(three.pesquisar(98))