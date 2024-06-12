#!1
x = 1
y = 2.3
name = "max"
isStudent = True

#type conversion
x = float(x)
print(x)
print(type(x))

y = int(y)
print(y)
print(type(y))

isStudent = int(isStudent)
print(isStudent)
print(type(isStudent))

x, y, name, isStudent = (1, 2.3, "max", True)



customerName = "Ali"
customerSurname = "Veli"

customer = customerName + ' ' + customerSurname

customerGen = True #Erkek
customerTC = "1111111111"
customerYear = 2000
customerAddress = "aasds street adasd"
customerAge = 2024 - customerYear


#------

order1 = 110
order2 = 1100.5
order3  = 356.95

order = order1 + order2 + order3

print("Total : ", order)

"""

Daire alani =   pir^2
daire çevresi = 2pir

* yari çapi verilen bir dairenin alan ve cevresini hesaplayiniz
* (r:  3.14)

"""
pi = 3.14
r = input("Yaricap r'yi giriniz: ")
float(r)

Alan = pi * (float(r) ** 2) # ** işlemi kare almaya yarar
Cevre = 2 * pi * float(r)

print("Alan = ", Alan)
print("Cevre = ", Cevre)