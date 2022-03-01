import mysql.connector


def read_users():

	my_db =  mysql.connector.connect(host='localhost',user='bizonho',password='YourPassWord',database='estudo')
	cursor = my_db.cursor()

	query =f'SELECT * FROM users WHERE client_status != "INATIVO"'

	cursor.execute(query)
	result = cursor.fetchall()

	for x in result:
		print(x)

