import mysql.connector

mydb = mysql.connector.connect( # ilgili adresdeki servera bağlantı sağladık.
    host = "localhost", # 192.23.45.56 (internetten satın alındığında bu yazılır)
    user = "root",
    password = "mysql1234",
    auth_plugin='mysql_native_password',
    database = "mydatabase"
)


mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES") # Tüm databaseleri gösterir.
# for x in mycursor:
#     print(x)

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") # customers isminde bir tablo oluştur