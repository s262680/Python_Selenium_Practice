import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", password="123456")

print("connected")

db.close()