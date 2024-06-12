from dbmanager import DbManager
from Student import Student
import datetime

class App:
    def __init__(self) -> None:
        self.db = DbManager() # App'e özel bir Db oluşturuldu
        
    def initApp(self):
        msg = "------------\n1-Student List\n2-Add Student\n3-Update Student\n4-Delete Student\n5-Add Teacher\n6-Class to lesson\n7-Exit(y/N)"
        while True:
            print(msg)
            islem = input('Choice: ')
            if islem == '1':
                self.displayStudents()    
            
            elif islem == '2':
                self.addStudent()
                
            elif islem == '3':
                self.editStudent()
            
            elif islem == '4':
                self.deleteStudent()
                
            elif islem == 'y' or islem == 'Y':
                break
            else:
                print('Wrong Choice')
    
    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Student id: '))
        
        self.db.deleteStudent(studentid)
    
    
    
    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Student id: '))
        
        student = self.db.getStudentById(studentid) # student objesi
        # print(student[0].name) # Öğrencinin ismini almış olduk sadece
        
        student[0].name = input('Name: ') or student[0].name # Kullanıcı bir şey girmezse eski ismin aynısını yaz
        student[0].surname = input('Surname: ') or student[0].surname
        student[0].gender = input('Gender(E/K): ') or student[0].gender
        student[0].classid = input('Class: ') or student[0].classid
        
        # Int yapılmalı aksi takdirde çalışmaz veya boş geçerek dene.
        year  = input('Year: ') or student[0].birthdate.year
        month  = input('Month: ') or student[0].birthdate.month
        day  = input('Day: ') or student[0].birthdate.day
 
        student[0].birthdate = datetime.date(year,month,day)
        
        self.db.editStudent(student[0])
    
    def addStudent(self):
        self.displayClasses()
        
        classid = int(input('Which class: '))
        number = input('Number: ')
        name = input('Name: ')
        surname = input('Surname: ')
        year = int(input('Year: '))
        month = int(input('Month: '))
        day = int(input('Day: '))
        gender = input('Gender(E/K): ')
        
        birthdate = datetime.date(year, month, day)
        
        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)
    
    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')
        
    def displayStudents(self):        
        self.displayClasses()
        classid = int(input('Which class: '))
        students = self.db.getStudentsByClassId(classid)
        print('Student List')
        for std in students:
            print(f'{std.id} - {std.name}, {std.surname}')
        
        return classid
        
app = App()
app.initApp()