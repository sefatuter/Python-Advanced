name = 'Sadik Turan'

for letter in name:
    if(letter == 'a'):
        break # a gördükten sonra döngüyü durdurur ve döngüden çıkılmasını sağlar
    print(letter)
    
for letter in name:
    if(letter == 'i'):
        continue # ise o döngü anını bitirir, döngüden çıkmaz
    print(letter)

print('\n')
x = 0

while x < 5:
    x = x + 1 # burada olmalı
    if(x == 2):
        continue # hep başa döner ve x artmaz
    print(x)
    # x = x +1

# 1- 100'e kadar tek sayıların toplamı.

x = 0
sum = 0
while(x <= 100):
    x += 1
    if x % 2 == 0:
        continue
    sum += x

print(f'Toplam : {sum}')



