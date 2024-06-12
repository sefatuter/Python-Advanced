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

    cursor.execute("Select * FROM Products")
    
    result = cursor.fetchall()    
    
    for product in result:
        print(f'Id: {product[0]}, Name: {product[1]}, Price: {product[2]}')    

def getProductById(id):
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    sql = "Select * FROM Products WHERE id=%s"
    params = (id,)
    
    cursor.execute(sql, params)
    result = cursor.fetchone()
    
    print(f'Id: {result[0]}, Name: {result[1]}, Price: {result[2]}')
 
def updateProduct(id, name, price):
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    # sql = "Update products SET name='Iphone 12'" # Products tablosunu günceller ve bütün name alanlarını Iphone 12 yapar.    
    # sql = "Update products SET name='Iphone 12', price = 12000, description = 'apple phone' WHERE id=5" #id'si 5 olan kaydı "Iphone 12" yapar
    
    # if name != '': # Kontrol edilebilir
    # if price:
    
    sql = "Update products SET name=%s, price=%s WHERE id=%s"
    values = (name,price,id)
    cursor.execute(sql, values)
    
    try:
        connection.commit()        
        print(f'{cursor.rowcount} tane kayıt güncellendi.')
    except mysql.connector.error as err:
        print('Hata: ', err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı.')
        
def deleteProduct(id):
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    sql = "Delete FROM products WHERE id=%s" # id kaydı
    values = (id,)
    cursor.execute(sql, values)
    
    try:
        connection.commit()        
        print(f'{cursor.rowcount} tane kayıt silindi.')
    except mysql.connector.error as err:
        print('Hata: ', err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı.')
    

deleteProduct(3)
getProducts()
    