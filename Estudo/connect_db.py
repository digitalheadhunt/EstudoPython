import mysql.connector


def connection(query):
	mydb = mysql.connector.connect(host='localhost',user='bizonho',password='YourPassWord',database='estudo')

	print(query)
	
	cursor = mydb.cursor()
	cursor.execute(query)
	mydb.commit()