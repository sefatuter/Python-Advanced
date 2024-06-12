website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1 - 'course' karakter dizisinden kaç tane bulunmaktadır?

result = len(course)
length = len(website)
print(result)

#2 - 'website' içinden www karakterlerini alın.

result = website[7:10]
print(result)

#3 - 'website' içinden com karakterlerini alın.

result = website[22:25]
result = website[length-3: length]
print(result)

#4 - 'course' içinden ilk 15 ve son 15 karakteri al.

result = course[0:15]
result = course[:15]
print(result)

result = course[-15:]
print(result)

#5 - 'course' ifadesindeki karakterleri tersten yazdırın.

result = course[::-1]
print(result) 

s = '12345' * 5

print(s[::5]) # s'nin bütün hepsini al ama her 5. indexteki karakterde bir yazdır

name, surname, age, job = 'Bora', 'Yilmaz', 32, 'mühendis'
#6 - Yukarıda verilen değişkenler ile aşağıdaki ifadeyi yazdır.
#      'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

introduce = 'Benim adim ' + name + " " +  surname + ',' + ' Yasim ' + str(age) + ' ve meslegim ' + job + "."
introduce2 = f"Benim adım {name} {surname}, Yaşım {age}  ve mesleğim {job}."
introduce3 = "Benim adım {1} {0}, Yaşım {2}  ve mesleğim {3}.".format(name, surname, age, job) #name 0 surname 1 age 2 job 3

print(introduce2)
print(introduce3)
#7 'Hello world' ifadesindeki w harfini 'W' harfi ile değiştirin.

h = "Hello world"
h = h[0:6] + 'W' + h[-4:] # parçalayarak bölümledik

h.replace('w', 'W')
print(h)

#8  'abc' ifadesini yan yana 3 defa yazdırın.

a = "abc"

print(a*3)
