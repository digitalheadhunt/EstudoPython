import socket

resp = "S"

while resp == "S":
	url = input("digite uma url aqui: ")
	ip = socket.gethostbyname(url)
	print(socket.getservbyname("domain"))
	print(socket.getservbyname("http"))
	print(socket.getservbyname("ftp"))
	print("O ip referente a url e : ", ip)
	resp = input("Digite <S> para continuar: ").upper()


