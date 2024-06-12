import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Lesson import Lesson
from Class import Class


class DbManager:
    def __init__(self) -> None:
        self.connection = connection
        self.cursor = self.connection.cursor()
        
    def getStudentById(self, id):
        sql = "Select * FROM student WHERE id = %s"
        value = (id, )
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            # print(obj)
            # return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)
        
    def getStudentsByClassId(self, classid):
        sql = "Select * FROM student WHERE classid = %s"
        value = (classid, )
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            # print(obj)
            # return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6]) # Alternatif olarak aşağıdakini kullandık Student.py bak
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)
    
    def deleteStudent(self, studentid):
        sql = "DELETE FROM student WHERE id=%s"    
        value = (studentid, )
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as err:
            print('Error: ', err)
    
    
    def getClasses(self):
        sql = "Select * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)
    
    
    def addorEditStudent(self, student: Student):
        pass
    
    def addStudent(self, student: Student):
        sql = "INSERT INTO student(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES (%s,%s,%s,%s,%s,%s)"    
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Error: ', err)
    
    def editStudent(self, student: Student):
        sql = "Update student SET studentNumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid=%s WHERE id=%s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, value)
        
        self.cursor.execute(sql, value)
        
        try:
            self.connection.commit()        
            print(f'{self.cursor.rowcount + 1} tane kayıt güncellendi.')
        except mysql.connector.error as err:
            print('Hata: ', err)
    
    def addTeacher(self, student: Teacher):
        pass
    
    def editTeacher(self, student: Teacher):
        pass
    
    def __del__(self): # pip install --upgrade mysql-connector-python
        self.connection.close()
        print('db silindi.')
    
    
db = DbManager()

# CreateStudent'siz
# student = db.getStudentById(2)
# print(student.name)
# print(student.surname)

# CreateStudent'li
# student = db.getStudentById(2)
# print(student[0].name)
# print(student[0].surname)

# students = db.getStudentsByClassId(1)
# print(students[0].name)
# print(students[0].surname)
# print(students[1].name)
# print(students[1].surname)

# std = Student(None, 109, "Yaman",) # Şeklinde doldurulabilir
student = db.getStudentById(6)
student[0].name = "Kerim"
student[0].surname = "Turan"
student[0].studentNumber = "965"
student[0].gender = 'E'

db.editStudent(student[0])