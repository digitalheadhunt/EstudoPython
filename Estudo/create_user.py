from connect_db import *
"""
	CREATE TABLE users(
	 id INT AUTO_INCREMENT  PRIMARY KEY,
	 name VARCHAR(50) DEFAULT NULL,
	 login VARCHAR(20) DEFAULT NULL,
	 senha VARCHAR(30) DEFAULT NULL,
	 client_status VARCHAR(20) DEFAULT 'ativo'
	)

"""

def criar_user():
	nome = input("Digite o nome do usuario: ")
	login = input("Digite o login: ")
	senha = input("Digite a senha: ")
	
	query = f'INSERT INTO users(name, login, senha) VALUES("{nome}", "{login}", "{senha}")'
	connection(query)

	return


def update_user():
	nome = input("Digite o nome do usuario que quer atualizar: ")
	status = input("Digite o status ATIVO ou INATIVO para o usuario: ").upper()
	query = f'UPDATE users SET client_status ="{status}" WHERE name ="{nome}"'
	connection(query)
