import person as ps


def criar_aluno():
	nome = input("Digite o nome do aluno")
	nota1 = input("Digite a nota 1")
	nota2 = input("Digite a nota 2")

	return ps.aluno(nome,nota1,nota2)

	



def calcular_nota(aluno):
	result = (aluno.nota1 + aluno.nota2) / 2 

	if result > 6:
		print("Aluno aprovado")
	else :
		print("Aluno reprovado")


calcular_nota(criar_aluno())