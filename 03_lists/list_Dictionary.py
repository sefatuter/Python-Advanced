#key - value
#41 -> kocaeli
#34 -> istanbul

#dictionary olmadan liste ile kullanımı
sehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])

# istenilen print(plakalar['kocaeli']) -> 41 şeklinde yapmak

# var  = {key : value, ....}
plakalar = {'Kocaeli' : 41, 'istanbul' : 34}

print(plakalar['Kocaeli'])
print(plakalar['istanbul'])

plakalar['Ankara'] = 6 # ankara bilgisi key olarak eklendi.
plakalar['Kocaeli'] = 'new value' # yeni atama yapıldı.

print(plakalar)

users = { 
    'sadikturan': {
        'age': 36,
        'email': "sadk@gmail.com",
        'address': "kocaeli",
        'phone': "123123123"
    },
    'cinarturan': {
        'age': 6,
        'roles': ['admin', 'user'],
        'email': "cnrk@gmail.com",
        'address': "kocaeli",
        'phone': "3231233"
    }
}

print(users['sadikturan']['age'])
print(users['sadikturan']['address'])
print(users['sadikturan']['phone'])

print(users['cinarturan']['roles'][0])


    

