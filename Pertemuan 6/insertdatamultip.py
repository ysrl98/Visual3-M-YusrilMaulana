import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "", 
    database = "db_penjualan")

mycursor = mydb.cursor()
sql = "INSERT INTO Kategori (id, name) VALUES (%s, %s)"
val = [("3", "Sagu"), ("4", "Tepung")]
mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "Data Berhasil Ditambahkan.")