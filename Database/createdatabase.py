import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password=""
    
    )

mycursor = db.cursor()
mycursor.execute('CREATE DATABASE db_penjualan')
print("Database Dibuat")