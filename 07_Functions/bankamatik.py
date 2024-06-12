# Bankamatik Uygulaması

JohnAcc = {
    'name': 'John',
    'accountNo': '123412',
    'balance': 3000,
    'additionalAcc': 1000,
}

MaxAcc = {
    'name': 'Max',
    'accountNo': '123112',
    'balance': 9000,
    'additionalAcc': 3000,
}

def withrawMoney(hesap, miktar):
    print(f"Merhaba {hesap['name']}")

    if hesap['balance'] >= miktar:
        print('Paranızı alabilirsiniz.')
        hesap['balance'] -= miktar
    else:
        toplam = hesap['balance'] + hesap['additionalAcc']
        if (toplam >= miktar):
            hesap['balance'] -= miktar # bakiyenin güncellenmesi
            addAcc = input('Ek hesap kullanılsın mı? (y/N): ')
            if addAcc == 'y':
                ekHesapMiktar = miktar - hesap['balance']
                hesap['additionalAcc'] -= ekHesapMiktar
                hesap['balance'] = 0
                print('Paranızı alabilirsiniz.')
                print(f"{hesap['accountNo']} nolu hesabınızda {hesap['balance']} miktarda para bulunmaktadır. Ek hesap {hesap['additionalAcc']} ")
            else:
                print(f"{hesap['accountNo']} nolu hesabınızda {hesap['balance']} miktarda para bulunmaktadır ")
        else:
            print('Bakiyeniz yetersiz')

x = int(input('Cekmek istediginiz miktari giriniz: '))

withrawMoney(JohnAcc, x)

x = int(input('Cekmek istediginiz miktari giriniz: '))

withrawMoney(JohnAcc, x)

def bakiyeSorgu(hesap):
    print('******************************')
    print(f"{hesap['accountNo']} nolu hesabınızda {hesap['balance']}, tl bulunmaktadır, ek hesap {hesap['additionalAcc']}")

bakiyeSorgu(JohnAcc)