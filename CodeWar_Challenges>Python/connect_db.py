import mysql.connector

def connection():
	mydb = mysql.connector.connect(host='localhost',user='bizonho',password='30912650',database='estudo')

	cursor = mydb.cursor()

	return cursor