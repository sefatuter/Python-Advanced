import pandas as pd

data = pd.read_csv("C:/Users/SefaPc/Desktop/btkPythonL/17_Data/datasets/nba.csv")

data.dropna(inplace=True) # NaN olan satırları sildik


print(data.columns)

data["name"] = data["name"].str.upper() # name kolonunun hepsini büyük harfe çevirir
data["name"] = data["name"].str.lower()
data["index"] = data["name"].str.find('a') # içinde a harfi kaçıncı indekste geçiyorsa bunu indeks kolonuna atar
data = data[data.name.str.contains('Tom')] # Tom geçen kayıtları bulur
data = data.college.str.replace(' ', '-').str.replace(',', ' ')
data[['FirstName', 'LastName']] = data['name'].loc[data['name'].str.split().str.len() == 2].str.split(expand=True) # Ad ve soyad kolonlarını ayırdık


print(data.head(10))
