#here I started a function to open or create a new txt, and write in this txt, put the informations about the dispositivos
def inserir_dispositivos():
	with open("dispositivos.txt","a") as disp:
		nome = input("Insira o nome do dispositivo de rede: ")
		id_de_rede = input("Insira o id de rede do dispositivo: ")
		ip_de_rede = input("Insira o ip da rede do dispositivo: ")
		porta = input("Qual porta esse dispositivo esta connectado")
		#Well I choose to use 2 write functions because the write() using fString doesn`t accept text when begins with \n
		disp.write("\n nome do dispositivo: " + nome + " ...:")
		disp.write(f'id: {id_de_rede} ip: {ip_de_rede}, porta: {porta}')


def ler_dispositivos():
	#Now on the read function I choose the argument r to just read the lines on the txt arquive
	with open("dispositivos.txt","r") as disp:
		line = 0
		for x in disp:
			print(line,x)
			line += 1