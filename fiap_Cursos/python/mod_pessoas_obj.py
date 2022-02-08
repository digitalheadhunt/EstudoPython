from manager_user import *
pessoas =[]

pergunta = input("Escolha uma das opcoes a seguir \n <I> para inserir um novo paciente \n <P> para pesquisar um usuario \n <L> para listar \n <E> para excluir: ").upper()

while pergunta == "I" or pergunta == "P" or pergunta == "L" or pergunta == "E":
	if pergunta == "I":
		criar_pessoa(pessoas)
		pergunta = input("Escolha uma das opcoes a seguir \n <I> para inserir um novo paciente \n <P> para pesquisar um usuario \n <L> para listar \n <E> para excluir: ").upper()
	elif pergunta == "L":
		listar_pessoa(pessoas)