from create_user import *
from read_user import *

response = "S"
option = ""
while response == "S":
	option = input("C para criar um usuario, D para deletar um usuario, L para listar todos, E para editar e X para sair: ").upper()
	if option == "C":
		criar_user()
	elif option == "E":
		update_user()
	elif option == "L":
		read_users()
	else:
		response = input('Deseja continuar S para continuar: ')

