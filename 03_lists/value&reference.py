# value type -> string, numbers
x = 5
y = 25

x = y

y = 10

print(x,y)

# reference type -> lists

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b # bir adres eşitlemesi yapılır

b[0] = "grape" # b üzerinde yapılan değişiklik a'yı etkiledi

print(a, b)