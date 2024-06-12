def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ort = (not1+not2+not3) / 3    
    
    if ort >= 90 and ort <= 100:
        harf = 'AA'
    elif ort >= 85 and ort <= 89:
        harf = 'BA'
    elif ort >= 80 and ort <= 84:
        harf = 'BB'
    elif ort >= 75 and ort <=79:
        harf = 'CB'
    elif ort >= 70 and ort <=74:
        harf = 'CC'
    elif ort >= 65 and ort <=69:
        harf = 'DC'
    elif ort >= 60 and ort <=64:
        harf = 'DD'
    elif ort >= 50 and ort <=59:
        harf = 'FD'
    else:
        harf = 'FF'
    
    return ogrenciAdi + ": " + harf + '\n'
    
def ortalamaOku():
    with open("exam_notes.txt", "r", encoding='utf-8') as file:
        for satir in file:
            print(not_hesapla(satir))
        
        
def notGir():
    ad = input('Öğrenci adı:')
    soyad = input('Öğrenci soyadı: ')
    not1 = input('Not 1: ')
    not2 = input('Not 2: ')
    not3 = input('Not 3: ')   
    
    with open("exam_notes.txt", "a", encoding='utf-8') as file:
        file.write(ad + ' ' + soyad + ': ' + not1+ ',' + not2 + ',' + not3 + '\n')

def notKayit():
    with open("exam_notes.txt", "r", encoding='utf-8') as file:
        liste = []
        
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt", "w", encoding='utf-8') as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input('1- Notları oku\n2- Not gir\n3- Notları kaydet\n4- Çıkış\n -> ')
    
    if islem == '1':
        ortalamaOku()
    elif islem == '2':
        notGir()
    elif islem == '3':
        notKayit()
    else:
        print('Çıkış Yapıldı.')
        break