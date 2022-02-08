from multi_listas_buscas import *

lista_de_produtos = []

print("Deseja inserir produtos na lista?")
will_insert = input("Digite s ou n: ").upper()
if will_insert == "S":
	inserir_produtos(lista_de_produtos)

print("Deseja fazer ler os elementos da lista: ")
will_read = input("Digite s ou n: ").upper()
if will_read == "S":
	listar_elementos(lista_de_produtos)




