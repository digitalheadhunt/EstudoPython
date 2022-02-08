from classes import *

def criar_pessoa(obj):
	with open("pessoas.txt","a") as pessoas:	
		nome = input("Digite o nome a pessoa: ")
		sexo = input("Qual o sexo dessa pessoa: ")
		cep = input("Digite o cep: ")
		idade = input("Digite a idade: ")
		cel = input("Digite o telefone: ")

		pessoas.write("\n nome: " + nome)
		pessoas.write(f'\n sexo:{sexo}')
		pessoas.write(f'\n cep:{cep}')
		pessoas.write(f'\n idade:{idade}')
		pessoas.write(f'\n cel:{cel}')
		pessoas.write("\n #######################")
		


def listar_pessoa(obj):
	with open("pessoas.txt","r") as pessoas:
		lines = enumerate(pessoas)
		x = 0
		while x <= lines:
			for index,line in enumerate(pessoas):
				print(f'line{index}: {line}')
				x += 1
			break	
	return print("Finish read")
		

def deletar_pessoa(obj):
		return "True"
