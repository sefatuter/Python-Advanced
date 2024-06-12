# class

class Person:
    #pass  keywordü ile yer tutucu olarak kullandık
    # class attributes
    address = 'no information'

    #constructor (yapıcı metod)
    def __init__(self, name, year): # self -> classtan türetmiş olduğumuz p1 ya da p2 objesini temsil eder.
        # object attributes
        self.name = name
        self.year = year
        print('init metodu calisti.')
    # methods


# object, instance

p1 = Person(name = 'ali',year = 1990) # p1 objesi tanımladık
p2 = Person('veli', 2000) # name = .. şeklinde gösterilede bilir gösterilmeye de bilir

# updating
p1.name = 'ahmet' # class'a tanimlanan ismi değiştirdik
p1.address = 'istanbul'


# accessing object attributes
print(f'name: {p1.name}, year: {p1.year}, address {p1.address}')
print(f'name: {p2.name}, year: {p2.year}, address {p2.address}')


# print(p1, p2)
# print(type(p1), type(p2)) # tipleri Person tipinde

# print(p1 == p2) # farklı objeler