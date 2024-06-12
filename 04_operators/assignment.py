# x = 5
# y = 10
# z = 20

x, y, z = 5, 16, 20

# x, y = y, x
x = x + 5
x += 5       # x = x + 5
x -= 5       # x = x - 5
x *= 5       # x = x * 5
x /= 5       # x = x / 5
x %= 5       # x = x % 5 (bölümünden kalan)
y //= 5      # x = x // 5 (tam bölme küsüratı siler)
y **= z      # y = y ** 5 ( üs alma y üzeri z)

print(x, y, z)



values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values # values'in içindeki değerler x y ve z'ye aktarılır. (liste içerisinden çıkarmak)
      # kalan bütün elemanlar z'nin içine girer
print(x, y, z)
print(x, y, z[1])














