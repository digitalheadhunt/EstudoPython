
class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None;
        
    def mostra_lista(self):  
        print(self.valor)
        
class lista:
    def __init__(self,prox):
        self.primeiro = None;
    
    def mostrar_lista(self):
        atual = self.primeiro;
        while atual != None:
            atual.mostra_lista()
            atual = atual.prox
    
    def insere_inicio(self, valor):
        new_valor = No(valor)
        new_valor.prox = self.primeiro
        self.primeiro = new_valor
    
    def excluir_inicio(self):
        self.primeiro = self.primeiro.prox
    
    def buscar_na_lista(self, valor):
        atual = self.primeiro
        while atual != None:
                if valor == atual.valor:
                    print('------')
                    print(atual)
                    return 1
                atual = atual.prox 
        return '0'
    
    def insere_no_final(self,valor):
        new = No(valor)
        atual = self.primeiro
        while atual.prox != None:
            atual = atual.prox
        atual.prox = new
        return 0
        
    def remove_final(self):
        atual = self.primeiro
        while atual.prox != None:
            atual = atual.prox
        temp = atual
        atual = None;
        return temp
         
No1 = No(1)

L = lista(No1)

L.insere_inicio(80)

L.insere_inicio(150)

L.insere_inicio(30)
L.insere_inicio(50)
L.insere_inicio(60)
#L.buscar_na_lista(60)

L.insere_no_final(25)

L.mostrar_lista()
L.remove_final()
L.mostrar_lista()





