import pandas as pd

list = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]
dict = {'Name': ["Ahmet", "Ali", "Yağmur", "Çınar"], "Grade": [50,60,70,80]}
dict_list = [
                {"Name": "Ahmet", "Grade": 50},
                {"Name": "Ali", "Grade": 60},
                {"Name": "Yağmur", "Grade": 70},
                {"Name": "Çınar", "Grade": 80}    
            ]

#df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
df = pd.DataFrame(list, columns=["Name", "Grade"], index= [1,2,3,4]) # Dataframe oluşturma
df = pd.DataFrame(dict)
df = pd.DataFrame(dict, index=["212","233","545","123"]) # Öğrenci numaraları
df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index=["212","233","545","123"]) # Farklı yöntem ile oluşturduk

print(df)


# s1 = pd.Series([3,2,1,0])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)



