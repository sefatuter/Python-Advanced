import pandas as pd

customers = {
    'CustomerId': [1,2,3,4],
    'FirstName': ['Ahmet', 'Ali', 'Hasan', 'Canan'],
    'LastName': ['Yılmaz', 'Korkmaz', 'Çelik', 'Toprak']
}

orders = {
    'OrderId': [10,11,12,13],
    'CustomerId': [1,2,5,7],
    'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}

df_customers = pd.DataFrame(customers, columns= ['CustomerId', 'FirstName', 'LastName'])
df_orders = pd.DataFrame(orders, columns= ['OrderId', 'CustomerId', 'OrderDate'])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers, df_orders, how="inner") # Siparişi olan müşterileri getirdik yani CustomerId tutuyorsa getirildi.
# result = pd.merge(df_customers, df_orders, how="left") # bütün müşteriler gelsin ancak siparişi olmayan müşteriler de gelsin.
# result = pd.merge(df_customers, df_orders, how="right")
# result = pd.merge(df_customers, df_orders, how="outer")

customerA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ['Ahmet', 'Ali', 'Hasan', 'Canan'],
    'LastName': ['Yılmaz', 'Korkmaz', 'Çelik', 'Toprak']
}

customerB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ['Yağmur', 'Çınar', 'Cengiz', 'Can'],
    'LastName': ['Bilge', 'Turan', 'Yılmaz', 'Turan']
}

df_customerA = pd.DataFrame(customerA, columns= ['CustomerId', 'FirstName', 'LastName'])
df_customerB = pd.DataFrame(customerB, columns= ['CustomerId', 'FirstName', 'LastName'])

result = pd.concat([df_customerA,df_customerB],axis=0) # iki dataframe'i birleştirdik concat ile.
result = pd.concat([df_customerA,df_customerB],axis=1) # axis = 1 durumunda yan yana getirilir.

print(result)
