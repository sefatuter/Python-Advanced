message = "Hello There. My name is Sadık Turan"

# message = message.upper() # bütün karakterleri büyük harfe çevirir
# message = message.lower() # bütün karakterleri küçük harfe çevirir
# message = message.title() # her kelimenin baş harfi büyük olur
# message = message.capitalize() # sadece başlangıç büyük harf gerisi küçük

# message = message.strip() #başlangıç ve sondaki boşluk karakterini siler
# message = message.split() # her kelimeyi boşluklardan böler her kelimeye ayrı ayrı ulaşabiliriz diziye dönüşür 
# print(message[0])
# message = message.split(".") # noktalardan ayırır
# print(message[1])

# message = message.split()
# message = ' '.join(message) # ayrılmış elemanı birleştircek birleştirirken araya boşluk ekleyecek

#index = message.find('Sadık') # 24. indexten itibaren cümle içerisinde var
#print(index)

# isFound = message.startswith('H') # mesaj içerisinde H ile başlayıp başlamadığına bakar
# print(isFound)

# isFound = message.endswith('n') # mesaj içerisinde n ile bitip bitmediğine bakar
# print(isFound)

# message = message.replace('Sadık', 'Çınar') #1. parametreyi bul yerine 2. parametreyi yaz
# message = message.replace('a','b').replace('d', 'y')

# message = message.center(100) # 100 karakterlik bir boşluğun içine alığ ortalar
# message = message.center(100, '-') # 100 karakterlik - işaretinin içine alır ve ortalar
# ! https://www.w3schools.com/python/python_ref_string.asp

print(message)