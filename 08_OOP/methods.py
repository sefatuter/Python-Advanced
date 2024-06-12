# Class
class Person:
    # Class Attributes
    address = 'No information'
    
    # Constructor (Yapıcı metod)
    def __init__(self, name, year):
        
        # Object attributes
        self.name = name
        self.year = year


    # instance Methods
    def intro(self): # tanımlanan objenin bir referansı buraya verilmeli
        print('Hello There. I am ' + self.name)

    def calculateAge(self):
        return 2024 - self.year


# Objects (Instance)

p1 = Person(name = 'ali',year = 1990)
p2 = Person('veli', 2000)

p1.intro() #p1 objesine hizmet eden bir method
p2.intro() #p2 objesine hizmet eden bir method

print(f"Age: {p1.calculateAge()}")
print(f"Age: {p2.calculateAge()}")


class Circle:
    # Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1): # Eğer yarıçap bilgisi belirtilmezse buna 1 değerini ata
        self.radius = radius
    
    # Methods

    def cf_calc(self):
        return 2 * self.pi * self.radius

    def r_calc(self):
        return self.pi * (self.radius ** 2)


c1 = Circle() # yaricap 1'e eşitlenmiş olur
c2 = Circle(5)


print(f"c1: region = {c1.r_calc()}, circumference = {c1.cf_calc()}")
print(f"c2: region = {c2.r_calc()}, circumference = {c2.cf_calc()}")





