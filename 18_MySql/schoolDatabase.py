#1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Id, StudentNumber, Name, Surname, Birthdate, Gender


#2- Database bağlantısını oluşturunuz.


import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    auth_plugin='mysql_native_password',
    database = "schooldb"
)

mycursor = connection.cursor()

