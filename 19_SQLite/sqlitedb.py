import sqlite3


connection = sqlite3.connect('C:/Users/SefaPc/Desktop/btkPythonL/SQLite/chinook.db') # yok ise klasörü oluşturur 
cursor = connection.cursor()

cursor.execute("Select * FROM customers")
result = cursor.fetchall()

for i in result:
    print(i)


connection.close()
