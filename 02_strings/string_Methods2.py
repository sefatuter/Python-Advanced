website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1 ' Hello World ' karakter dizisinin başındaki ve sonundaki boşlukları sil

h = ' Hello World '
h = h.strip()

print(h)

#2 'www.sadikturan.com' içindeki sadıkturan bilgisi dışındakileri sil

result = website.lstrip('htp:/')
print(result)

result = result.strip('w.com')
print(result)

#3 'course' karakter dizisinin tüm karakterlerini küçük harf yapın

result = course.lower()
print(result)

#4 'website' içinde kaç tane a karakteri vardır? (count(a)) 

result = website.count('a')
result = website.count("www",0,10) # 0 ile 10. karakterler arası
print(result)

#5 'website' www ile başlayıp com ile bitiyor mu?

isStart = website.startswith('www')
print(isStart)
isEnd = website.endswith('com')
print(isEnd)

#6 'website' içinde '.com' ifadesi var mı?

result = website.find("com")
result = website.index("com")
print(result)

#7 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result = course.isdigit()
print(result)

#8 'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna + ekleyiniz

result = 'contents'.center(50, "+") # ortalar
#result = 'contents'.ljust(50, "'") # sola yaslar
print(result)


#9 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin

result = course.replace(" ", "-")
print(result)

#10 'Hello World' karakter dizisinin  'World' ifadesini 'There' olarak değiştir

h = 'Hello World'
h = h.replace("World", "There")
print(h)

#11 'course' karakter dizisini boşluk karakterlerinden ayırınız.

result = course.split(" ")

print(result[2])

