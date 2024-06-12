import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=['a', 'c', 'e', 'f', 'h'], columns= ['column1', 'column2', 'column3'])

df = df.reindex(['a', 'b','c', 'd', 'e', 'f', 'g', 'h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df['column4'] = newColumn


result = df

result = df.drop("column1", axis=1) # Kolon 1'i sildik
result = df.drop(['column1', 'column2'], axis=1)
result = df.drop('a', axis=0) # a satırını sildik
result = df.drop(['a', 'b', 'c'], axis=0)

result = df.isnull() # True ya da False olarak döndürür
result = df.notnull()
result = df.isnull().sum()
result = df['column1'].isnull().sum()
result = df[df['column1'].isnull()] # Kolon 1 de nan olanları getir dedik
result = df[df['column1'].isnull()]['column1']
result = df[df['column1'].notnull()]['column1']
result = df[df['column1'].notnull()]

result = df.dropna() # axis = 0 => Satır (default) # nan'ları silme satır veya sütun
result = df.dropna(axis=1) # axis = 1 => sütun
result = df.dropna(how = 'any') # En az 1 nan olması durumunda silmek istersek
result = df.dropna(how = 'all') # Hepsi nan olursa siler ancak. bütün kolonlarda arar
result = df.dropna(subset= ['column1', 'column2'], how= 'all') # nan silmek istenilen kolonları belirtiriz # 1 ve 2.kolonda herhangi bir nan varsa siler
result = df.dropna(subset= ['column1', 'column2'], how='any')
result = df.dropna(thresh=3) # en az sayıda normal veri
result = df.fillna('no input') # nan'lara doldurma işlemi için
result = df.fillna(1)

result = df.sum()
result = df.sum().sum() # dataframe'deki toplam değeri verir
result = df.size
result = df.isnull().sum().sum() # nan olanların toplam değeri


def ortlama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value= ortlama(df)) # boşlukları hesapladığıız ortalama ile doldurduk




print(result)



personeller = {
    'Çalışan': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
    'Departman': ['İnsan Kaynakları', 'Bilgi İşlem', '', 'İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
    'Maaş': [5000, 3000, 3500, 6500]
}

