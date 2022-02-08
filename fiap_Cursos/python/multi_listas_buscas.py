
def inserir_produtos(l):
	lists = [] 
	resposta = "S"

	while resposta == "S":
		produtos = input("Digite o nome do produto: ")
		serial = input("Digite o numero serial do produto: ")
		setor = input("Digite o setor que o produto vai: ")
		lists.append(produtos)
		lists.append(serial)
		lists.append(setor)
		l.append(lists)
		resposta = input("Digite \"S\" para continuar: ").upper()
		lists = []	
	

def listar_elementos(l):
	for x in range(0,len(l)):
		print("Produto......:"+l[x][0])
		print("Serial.......:"+l[x][1])
		print("Setor........:"+l[x][2])
		print("#_______________#")


