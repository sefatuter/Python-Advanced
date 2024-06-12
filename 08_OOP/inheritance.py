# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Person ortak bir özellik aşağıdaki kişilerin de sahip olabileceği
# Student(Person), Teacher(Person)


# Animal => Dog(Animal), Cat(Animal) # Dog ve cat animal'dan miras alıyor


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created.')

    def whoami(self):
        print('I am a person')

    def eat(self):
        print('I am eating.')


class Student(Person): # Student'in persondan türetildiğini belirttik Student persondaki bütün özelliklere sahip
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname) # ezmeyi engellemek için bu veya def __init__(self) -> Person: oldu
        self.studentNumber = number
        print('Student Created') # burada student init'i personu ezer.

    # override
    def whoami(self):
        print('I am a student') #whoami metodunu burada da tanımlayarak person'dakini ezdik ( Override )

    def sayHello(self):
        print('Hello I am a student')


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) # ikinci yolu persondan miras almasi icin
        self.branch = branch
    
    def whoami(self):
        print(f'I am a {self.branch} teacher')



p1 = Person('Ali', 'Yılmaz')
s1 = Student('Çınar', 'Turen', 1234)
t1 = Teacher('Veli', 'Yılmaz', 'Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.whoami()
s1.whoami() # student üzerinden de whoami'a ulaşılabilir.

p1.eat()
s1.eat()

s1.sayHello() # Sadece student üzerinden çağırılır.

t1.whoami()












