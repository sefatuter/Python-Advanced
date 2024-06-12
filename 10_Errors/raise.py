x = 10

# if x > 5:
#     raise Exception("X 5'den buyuk olamaz.")

def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 8 karakterli olmali.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[@_$]", psw):
        raise Exception("Parola alfanümerik karakter içermelidir.(@_$)")
    elif re.search("\s", psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print('Gecerli Parola. fonksiyondan')
    
password = "12345678aA@"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print('Gecerli parola: else kısmından')
finally:
    print('Validation tamamlandı.')


class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter iceriyor.")
        else:
            self.name = name
        
p = Person("Aliiiiiiiiiii", 1099)