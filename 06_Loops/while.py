# 1-100 e kadar

#i = 0
#while(i <= 100):
#    if i % 2 == 0:
#        print(i, 'çift sayi')
#    else:
#        print(i, 'tek sayi')
#    i += 1


name = '' # false

while not name.strip(): # boşluk karakteri false olur ve istenilen girilene kadar sorar.
    name = input('isminizi giriniz: ') 

print(name, 'merhaba')