import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
    'Departman': ['İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
    'Maaş': [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}

df = pd.DataFrame(personeller)
result = df

result = df['Maaş'].sum() # Maaş bilgisinin toplamını yazdırır.
result = df.groupby('Departman').groups # Gruplama yapar, hangilerinin gruplandığını gösterir.
result = df.groupby(['Departman', 'Semt']).groups # iki tanesi aynı olanları gruplar


for name, group in df.groupby('Semt'): # Semtler grubunda dönerek semti aynı olanları gruplar ve printler
    print(name)
    print(group)

for name, group in df.groupby('Departman'):
    print(name)
    print(group)

print("--------------")
result = df.groupby('Semt').get_group('Kadıköy') # Kadıköyde oturan kişileri gruba göre almış olduk
result = df.groupby('Departman').get_group('Muhasebe') # Departmanı Muhasebe olan kişileri aldık

result = df.groupby('Departman').sum('Yaş')
result = df.groupby('Departman').mean('Yaş')
result = df.groupby('Semt')['Maaş'].mean()
result = df.groupby('Semt')["Yaş"].mean()
result = df.groupby('Semt')["Çalışan"].count()
result = df.groupby('Departman')["Yaş"].max()
result = df.groupby('Departman')["Maaş"].min()["Muhasebe"] # Muhasebede minimum maaş
result = df.groupby('Departman')['Maaş'].agg([np.sum])
result = df.groupby('Departman')['Maaş'].agg([np.sum, np.mean, np.max, np.min])




print(result)