import random

# print(dir(random))
# print(help(random))


result = random.random() #0.0 ile 1.0 arasında rastgele bir sayı üretir
result = random.random() * 100

result = random.uniform(1,100) #1 ile 100 arasi float sayilar
result = int(random.uniform(1,100))

result = random.randint(1, 100) # 1 ile 100 arasi int sayilar


greeting = 'Hello There'
names = ['ali', 'deniz', 'cenk', 'veli', 'can']

result = names[random.randint(0, len(names)-1)]
result = random.choice(names) # üsttekinin fonksiyon hali
result = random.choice(greeting) # karakterleri rastgele seçer string listesi

liste = list(range(10)) #10 elemanlı listeye çevirdik

random.shuffle(liste)
result = liste # Rastgele liste elemanları dağıtır


liste = range(100) # 0 dan 100 e sayıların olduğu liste oluşturduk
result = random.sample(liste, 3) # 3 tane rastgele sayı almak için 

result = random.sample(names, 3) # 3 tane rastgele isim almak için

print(result)









