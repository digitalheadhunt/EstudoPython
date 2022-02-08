# Here I`ve imported all functions in registro_rede.py to call them here
from registro_rede import *

#now Im just start a new variable the catch the users answer to choose one function to call
pergunta = input("Escolha uma das opcoes a seguir \n <I> para inserir um novo dispositivo \n <P> para pesquisar um dispositivo \n <L> para listar \n <E> para excluir: ").upper()

while pergunta == "I" or pergunta == "P" or pergunta == "L" or pergunta == "E":
	if pergunta == "I":
		inserir_dispositivos()
		pergunta = input("Escolha uma das opcoes a seguir \n <I> para inserir um novo dispositivo \n <P> para pesquisar um dispositivo \n <L> para listar \n <E> para excluir: ").upper()
	elif pergunta == "L":
		ler_dispositivos()
		pergunta = input("Escolha uma das opcoes a seguir \n <I> para inserir um novo dispositivo \n <P> para pesquisar um dispositivo \n <L> para listar \n <E> para excluir: ").upper()
