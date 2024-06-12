#-- 1. Yöntem --
# import math
import math as islem # modüle özel isim de verilebilir

# print(dir(math)) # math modülü içindeki bütün fonksiyonlar
# print(help(math)) # hangisinin ne işe yaradığını gösterir

# print(math.factorial) # factorial fonksiyonunun ne işe yaradığı


# value = math.factorial(5)

# value = islem.ceil(5.9)

#-- 2. Yöntem --

# from math import * # math'dan hepsini import et ve artık fonksiyonun adlarını sadece kullanabilirsin
from math import factorial, sqrt # özel olarak belirli fonksiyonu import etmek

def sqrt(x):
    print('x: '+ str(x))
# fonksiyon import altına alınırsa, fonksiyon baz alınır
# en son ne tanımlanırsa o referans alır.

value = sqrt(6)

print(value)
