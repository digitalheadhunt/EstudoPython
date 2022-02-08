from geopy.geocoders import Nominatim

def criar_clientes():
	geolocator = Nominatim(user_agent="Thalis")

	with open("rel_clientes.txt","a") as clients:
		nome = input("Digite o nome: ")
		endereco = input("Digite o endereco: ")
		telefone = input("Digite o telefone: ")
		tipo_de_aparelho = input("Qual aparelho: ")
		email = input("Email de contato: ")

		location = geolocator.geocode(f'{endereco}')
		clients.write(f'\n Nome.......: {nome}')
		clients.write(f'\n endereco...: {location.address}')
		clients.write(f'\n coordenades: {location.longitude},{location.latitude}')
		clients.write(f'\n contatos...: {telefone}, email: {email}')
		clients.write(f'\n Aparelho...: {tipo_de_aparelho}')
		clients.write(f'\n - - - - - - - - - - - - - - - - - - - - - - ')

criar_clientes()





