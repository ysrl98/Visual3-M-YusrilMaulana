import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password=""
    
    )

if db.is_connected():
    print("Berhasil Terhubung ke Database")