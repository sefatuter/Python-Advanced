from datetime import datetime
from datetime import timedelta

simdi = datetime.now()
simdi = datetime.today()

result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi) # daha acıklayici bir bilgi verir

result = datetime.strftime(simdi,'%Y') # sadece yıl bilgisi örnegin.
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %d') # yıl ay gün.

# gun, ay, yil = t.split(' ')
# print(gun)
# print(ay)
# print(yil)

# print(result)

t = '21 April 2019 hour 10:12:30'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S') # kendi olusturdugumuz stringi ayirdik

# dt = dt.year # gibi özel olarak alınabilir

print(dt)

birthday = datetime(1983,5,9)
print(birthday)


dt = datetime.timestamp(birthday) # tarihi saniyeye çevirir
print(dt) # saniye cinsinden yazdırılır.

dt = datetime.fromtimestamp(dt) # saniyeyi tarih bilgisine çevirir
print(dt) 

dt = datetime.fromtimestamp(0)
print(dt) # bilgisayarlar için kullanılan milat bilgisi

dt = simdi - birthday # aradaki farki alır

# dt = dt.days # toplam gün bilgisi getirilir
# dt = dt.seconds
# dt = dt.microseconds

dt = simdi + timedelta(days=11) # şimdiki günün üzerine 11 gün ekler.
 
dt = simdi - timedelta(days=10) # şimdiki günden 10 gün çıkarır.
 
print(dt)

