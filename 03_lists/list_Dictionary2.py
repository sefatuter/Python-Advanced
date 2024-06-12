'''
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    }
}

        1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
        dictionary içinde saklayınız.

        2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
    
'''
"""
no = input("Ögrenci no giriniz: ")

ad = input("Öğrenci adı: ")
soyad = input("Öğrenci soyadı: ")
telefon = input("Telefon numarası: ")

no2 = input("Ögrenci no giriniz: ")

ad2 = input("Öğrenci adı: ")
soyad2 = input("Öğrenci soyadı: ")
telefon2 = input("Telefon numarası: ")

no3 = input("Ögrenci no giriniz: ")

ad3 = input("Öğrenci adı: ")
soyad3 = input("Öğrenci soyadı: ")
telefon3 = input("Telefon numarası: ")

ogrenciler = {
    no: {
        'ad': ad,
        'soyad': soyad,
        'telefon': telefon
    },
    no2: {
        'ad': ad2,
        'soyad': soyad2,
        'telefon': telefon2
    },
    no3: {
        'ad': ad3,
        'soyad': soyad3,
        'telefon': telefon3
    }
}

ogrNo = input("Bilgi görmek icin ogrenci no gir : ")

print(ogrenciler[ogrNo]['ad'] + "\n" + ogrenciler[ogrNo]['soyad'] + "\n" + ogrenciler[ogrNo]['telefon'])

"""

ogrenciler = {}

number = input("öğrenci no: ")

name = input("öğrenci ismi: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }
ogrenciler.update({ # birden fazla veriyi aynı liste üzerine ekleme şansı sağlar
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone,   
    }
})

number = input("öğrenci no: ")

name = input("öğrenci ismi: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({ # birden fazla veriyi aynı liste üzerine ekleme şansı sağlar
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone,   
    }
})

number = input("öğrenci no: ")

name = input("öğrenci ismi: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({ # birden fazla veriyi aynı liste üzerine ekleme şansı sağlar
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone,   
    }
})

print('*'*50)

ogrNo = input('öğrenci no: ')

ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefon: {ogrenci['telefon']}.")
