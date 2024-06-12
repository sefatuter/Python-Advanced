#4- Aşağıdaki güncelleme sorularını yapınız.
#   a- id'e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet'e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

import mysql.connector
from datetime import datetime
from connection import connection

mycursor = connection.cursor()

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, id, studentNumber, name, surname, birthdate, gender) -> None:
        if id is None:
            self.id=0
        else:
            self.id = id          
            
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
    
    @staticmethod                  
    def getStudentById(id):
        
        sql = "Select * FROM student WHERE id=%s"
        params = (id,)
        
        Student.mycursor.execute(sql, params)
        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        except mysql.connector.Error as err:
            print('Hata: ', err)
        
    @staticmethod    # Sadece Id'ye göre alma işlemi yapacaksan bunu kullanma!         
    def updateStudent(liste): #self        
        sql = "Update student SET studentNumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s WHERE id=%s"
        # values = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender, self.id)
        values = []
        order = [1,2,3,4,5,0]
        
        for item in liste:
            item = [item[i] for i in order] # sıralama yaptık
            values.append(item)
        
        Student.mycursor.executemany(sql, values)
        
        try:
            Student.connection.commit()        
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.error as err:
            print('Hata: ', err)
            
    @staticmethod                  
    def getStudentsGender(gender):
        
        sql = "Select * FROM student WHERE gender=%s"
        value = (gender,)
        
        Student.mycursor.execute(sql, value)
        
        try:
            return Student.mycursor.fetchall()    
        except mysql.connector.Error as err:
            print('Hata: ', err)
        
        
# student = Student.getStudentById(23) #Id buradan

# student.name = 'Ali'
# student.surname = 'can'

# student.updateStudent()

students = Student.getStudentsGender('E')
# print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr. ' + std[2] # isim bilgisi var, güncelledik
    liste.append(std)
    
Student.updateStudent(liste)