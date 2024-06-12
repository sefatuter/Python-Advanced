import mysql.connector

def insertProduct(name, price, imageURL, description):
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    sql = "INSERT INTO Products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = (name, price, imageURL, description)
    
    cursor.execute(sql, values)
    
    try: # Hata olma ihtimalinden dolayı exceptiona aldık
        connection.commit() # Sorguyu çalıştır.
        print(f'{cursor.rowcount} tane kayıt eklendi.') # kaç kayıt eklendiğini söyler.
        print(f'Son eklenen kaydın Id numarası: {cursor.lastrowid}')
    except mysql.connector.error as err:
        print('Hata: ', err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı.')
        
def insertProducts(list):
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    sql = "INSERT INTO Products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"    
    cursor.executemany(sql, list) # Çoğul ekleme işlemi için executemany kullandık
    
    try: # Hata olma ihtimalinden dolayı exceptiona aldık
        connection.commit() # Sorguyu çalıştır.
        print(f'{cursor.rowcount} tane kayıt eklendi.') # kaç kayıt eklendiğini söyler.
        print(f'Son eklenen kaydın Id numarası: {cursor.lastrowid}')
    except mysql.connector.error as err:
        print('Hata: ', err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı.')
        
def getProducts():
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    # cursor.execute('Select * FROM products') # Bütün kayıtları getirir
    cursor.execute('Select name,price FROM products') # Sadece name, price kayıtlarını getirir
    # result = cursor.fetchall() # birden fazla kayıt almak için kullanılan metod
    
    result = cursor.fetchone() # Tek bir kayıt getirmesi için
    print(f'Name: {result[0]}, Price: {result[1]}')
    
    #for product in result:
    #    print(f'Name: {product[1]}, Price: {product[2]}')
    #    print(f'Name: {product[0]}, Price: {product[1]}') # ihtiyacımız olan kolonları database'den getirdik dolayısıyla indeks numarası değişti
    
    
getProducts()