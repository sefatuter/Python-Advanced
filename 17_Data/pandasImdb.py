import pandas as pd
import numpy as np

#1- Dosyada hakkındaki bilgiler.

imdbDf = pd.read_csv("C:/Users/SefaPc/Desktop/btkPythonL/17_Data/IMDB Top 250 Movies.csv")
print(imdbDf)

imdbDf = pd.DataFrame(imdbDf)
print(imdbDf)
print(imdbDf.info)

#2- ilk 5 kaydı göster.

result = imdbDf.head()
print(result)

#3- ilk 10 kaydı göster.

result = imdbDf.head(10)
print(result)

#4- son 5 kaydı göster.

result = imdbDf.tail(5)
print(result)

#5- son 10 kaydı göster.

result = imdbDf.tail(10)
print(result)


#6- Sadece Title kolonunu göster.

result = imdbDf["name"]
print(result)


#7- Title kolonunu içeren ilk 5 kaydı al

result = imdbDf["name"].head()
print(result)

#8- Title ve Rating kolonlarını içeren ilk 5 kaydı al

result = imdbDf[["name", "rating"]].head()
print(result)


#9- Title ve Rating kolonlarını içeren son 7 kaydı al

result = imdbDf[["name", "rating"]].tail(7)
print(result)

#10- Title ve Rating kolonunu içeren ikinci 5 kaydı al

result = imdbDf[6:][["name", "rating"]].head()
print(result)


#11- Title ve Rating kolonunu içeren ve imdb puanı 9.0 ve üstünde olan kayıtlardan ilk 50 tanesini al.

result = imdbDf[imdbDf["rating"] >= 9.0][["name", "rating"]]
print(result)

#12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getir.

result = imdbDf[(imdbDf["year"] >= 2014) & (imdbDf["year"] <= 2015)]["name"]
print(result)
