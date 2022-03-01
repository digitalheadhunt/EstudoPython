from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="teste")

rua = input("Digite o nome da rua, numero da casa e UF do estado: ")

location = geolocator.geocode(f'{rua}')
print(location.address)
print((location.latitude,location.longitude))