#4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 Doğumlu öğrenci bilgilerini alınız
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız
#   f- Ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
#   g- Kaç erkek öğrenci vardır?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

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
    
    @staticmethod      
    def getStudents():
        
        sql = "Select * FROM student"                                           #a-
        sql = "Select StudentNumber, Name, Surname FROM student"                #b-
        sql = "Select Name, Surname FROM student WHERE Gender='K'"              #c-
        sql = "Select * FROM student WHERE YEAR(Birthday) = 2003"               #d-
        sql = "Select * FROM student WHERE Name = 'Ali' AND YEAR(Birthday)=2005"#e-
        sql = "Select * FROM student WHERE Name LIKE '%an%'"                    #f-
        sql = "Select COUNT(*) FROM student WHERE Gender = 'E'"                 #g-
        sql = "Select * FROM student WHERE Gender = 'K' ORDER BY Name,Surname"  #h-

        # sql = "Select * FROM student LIMIT 5" # istenen sayıda kayıt alma. 
        Student.mycursor.execute(sql)

        try:
#a-,d-,e-,f-# result = Student.mycursor.fetchall()
            # for student in result:
            #     print(f'Result: {student[0]}, {student[1]}, {student[2]}, {student[3]}, {student[4]}, {student[5]}')
            
#b-         # result = Student.mycursor.fetchall()
            # for student in result:
            #     print(f'Result: {student[0]}, {student[1]}, {student[2]}')
   
#c-         # result = Student.mycursor.fetchall()
            # for student in result:
            #     print(f'Result: {student[0]}, {student[1]}')           
            
#g-         # result = Student.mycursor.fetchone()   
            # print(f'Total male student: {result[0]}')
            
            result = Student.mycursor.fetchall() #h-
            for student in result:
                print(f'Result: {student[0]}, {student[1]}, {student[2]}, {student[3]}, {student[4]}, {student[5]}')

        except mysql.connector.Error as err:
            print('Hata: ', err)
        finally:
            Student.connection.close()
        
        
        
Student.getStudents()        


# ogrenciler = [
#     ("303", "Canan", "Tan", datetime(2005, 7, 7), "K"),
#     ("304", "Ayşe", "Tane", datetime(2005, 9, 27), "K"),
#     ("305", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
#     ("306", "Ali", "Cenk", datetime(2003, 8, 25), "E"),
# ]

# Student.saveStudents(ogrenciler)

