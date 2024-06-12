name = "cinar"
surname = "turan"

# print('My name is {} {}'.format(name, surname))

print('My name is {0} {1}'. format(name, surname)) #aynı şekilde yazar ama 1 0 yaparsan tersi

print('My name is {s} {n}'. format(n = name, s = surname))

print('My name is {} {} and im {} years old.'. format(name, surname, '30'))

result = 200/700

print("Result = {r:1.3}".format(r = result)) #sağdan kaç basamak alınacağını seçer (3) r:1.3 (1) soldan kaç bosluk

print(f'My name is {name} {surname} and im {32} years old.')
