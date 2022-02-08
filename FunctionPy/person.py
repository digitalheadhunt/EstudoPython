
class pessoa:
	def _init_(self,nome,age,rg,rua,numero):
		self.nome = nome
		self.idade = age
		self.rg = rg
		self.rua = rua
		self.numero = numero
		


class dados:
	def _init_(self,url,nome,link):
		self.url = url
		self.nome = nome
		self.link = link


class info:
	def _init_(self,cel,nome,infos):
		self.cel = cel
		self.nome = nome
		self.infos = infos


class aluno:
	def _init_(self, nome, nota1, nota2):
		self.nome = nome
		self.nota1 = nota1
		self.nota2 = nota2
