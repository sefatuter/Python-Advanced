#1- Workbench IDE ile schooldb isminde bir database oluşturup student tablosunu ekleyiniz.
# Id, StudentNumber, Name, Surname, Birthdate, Gender

#2- Database bağlantısını oluşturunuz.

#3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.
#
#   ("101", "Ahmet", "Yılmaz", datetime.datetime(2005, 5, 17), "E"),
#   ("102", "Ali", "Can", datetime.datetime(2005, 6, 17), "E"),
#   ("103", "Canan", "Tan", datetime.datetime(2005, 7, 7), "K"),
#   ("104", "Ayşe", "Tane", datetime.datetime(2005, 9, 27), "K"),
#   ("105", "Bahadır", "Toksöz", datetime.datetime(2004, 7, 27), "E"),
#   ("106", "Ali", "Cenk", datetime.datetime(2003, 8, 25), "E"),

#-------------------------------------------------------

# students = []
# def insertStudent(students):
#     connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="schooldb")
#     cursor = connection.cursor()
    
#     sql = "INSERT INTO student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)"    
#     cursor.executemany(sql, students) # Çoğul ekleme işlemi için executemany kullandık
    
#     try: # Hata olma ihtimalinden dolayı exceptiona aldık
#         connection.commit() # Sorguyu çalıştır.
#         print(f'{cursor.rowcount} tane kayıt eklendi.') # kaç kayıt eklendiğini söyler.
#         print(f'Son eklenen kaydın Id numarası: {cursor.lastrowid}')
#     except mysql.connector.error as err:
#         print('Hata: ', err)
#     finally:
#         connection.close()
#         print('Database Bağlantısı Kapandı.')
        
# students = []
# while True:

#     no = input('Öğrenci numarası: ')
#     name = input('Öğrenci Adı: ')
#     surname = input('Öğrenci soyadı: ')
#     birthday = input('Doğum tarihi (YYYY/AA/GG): ')
#     gender = input('Cinsiyet: ')

#     students.append((no, name, surname, birthday, gender))
    
#     result = input('Öğrenci kaydına devam etmek istiyor musunuz? (y/N)')
#     if result == 'n' or result == 'N':
#         print('Kayıtlar veritabanına aktarılıyor...')
#         # Kayıt
#         print(students)
#         insertStudent(students)
#         break
    
    
#---> OR

# import mysql.connector
# from datetime import datetime

# connection = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "mysql1234",
#     auth_plugin='mysql_native_password',
#     database = "schooldb"
# )

# mycursor = connection.cursor()

# sql = "INSERT INTO student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)"    

# ogrenciler = [
#     ("103", "Canan", "Tan", datetime(2005, 7, 7), "K"),
#     ("104", "Ayşe", "Tane", datetime(2005, 9, 27), "K"),
#     ("105", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
#     ("106", "Ali", "Cenk", datetime(2003, 8, 25), "E"),
# ]

# mycursor.executemany(sql, ogrenciler)

# try:
#     connection.commit()
#     print(f'{mycursor.rowcount} tane kayıt eklendi.')
# except mysql.connector.Error as err:
#     print('Hata: ', err)
# finally:
#     connection.close()
    

# Nesne Tabanlı Yaklaşım ile uygulamak

import mysql.connector
from datetime import datetime
from connection import connection

mycursor = connection.cursor()

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber, name, surname, birthdate, gender) -> None:
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        
    def saveStudent(self):
        sql = "INSERT INTO student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)"    
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata: ', err)
        finally:
            Student.connection.close()
    
    @staticmethod
    def saveStudents(students): # Dışarıdan liste alır, kendine özel bir özelliği olacak
        sql = "INSERT INTO student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)"    
        values = (students)
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata: ', err)
        finally:
            Student.connection.close()
        
        
# ahmet = Student("202", "Ahmet", "Yılmaz", datetime(2005, 5, 16), "E")
# ahmet.saveStudent()

ogrenciler = [
    ("303", "Canan", "Tan", datetime(2005, 7, 7), "K"),
    ("304", "Ayşe", "Tane", datetime(2005, 9, 27), "K"),
    ("305", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
    ("306", "Ali", "Cenk", datetime(2003, 8, 25), "E"),
]

Student.saveStudents(ogrenciler)