import mod # Olusturduğumuz modülü ekledik
# Aynı dizin içinde olmalı eğer kendi modülümüzü ekleyecek isek
# terminalde sırasiyla:
# python
# import sys
# sys.path
# yazıp sonu lib ile biten path içine python dosyamızı atarsak direkt import edilebilir.


# print(help(mod))
# print(dir(mod))

# print(help(mod.func))

mod.func(101)
print(mod.number)
print(mod.numbers)


p = mod.Person()
p.speak()