# Identity Operator: 'is'

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y)
print(x == z)
#listelere atılan değerlerin karşılaştırması yapılır

print(x is y)
print(x is z) # x ile z farklı referansta, objelerin aynı mı değil mi?


x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()

print(x == y)
print(x is not y) # x, y objesi değil midir?

# Membership Operator: 'in'

x = ["apple", "banana"]
print('banana' in x)

name = 'Çınar'
print('a' in name) # a harfi name içinde mi?
print('a' not in name) # a harfi name içinde yok mu