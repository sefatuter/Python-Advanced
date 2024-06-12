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

    # cursor.execute("Select * FROM Products ORDER BY name") # İsme göre sıralama için ORDER BY kullandık
    # cursor.execute("Select * FROM Products ORDER BY price") # Fiyata göre sıraladık- artan
    # cursor.execute("Select * FROM Products ORDER BY id DESC") # id'ye göre azalan (DESCending) sıraladık
    cursor.execute("Select * FROM Products ORDER BY name, price") # önce name'e göre sıralar, sonra name'lerin içinde priceları sıralar (default = artan)
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(f'Id: {product[0]}, Name: {product[1]}, Price: {product[2]}') 
            
    except mysql.connector.error as err:
        print('Hata: ', err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı.')
      
def getProductById(id):
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    sql = "Select * FROM Products WHERE id=%s"
    params = (id,)
    
    cursor.execute(sql, params)
    result = cursor.fetchone()
    
    print(f'Id: {result[0]}, Name: {result[1]}, Price: {result[2]}')
 
def getProductInfo():
    connection = mysql.connector.connect(host= "localhost", user="root", password="mysql1234", auth_plugin='mysql_native_password', database="node-app")
    cursor = connection.cursor()
    
    # sql = "Select COUNT(*) FROM Products" # Satır sayısını sayar, WHERE price > 2000 yazılabilir 
    # sql = "Select AVG(price) FROM Products" # fiyat alanının ortalamasını getirir, WHERE ile filtreleme eklenebilir
    # sql = "Select SUM(price) FROM Products" # Toplamı alır
    # sql = "Select MIN(price) FROM Products"
    # sql = "Select MAX(price) FROM Products"
    sql = "Select name FROM Products WHERE price = (Select MAX(price) FROM Products)" # En pahalı ürünün ismini getir
    
    
    
    cursor.execute(sql)
    result = cursor.fetchone()
    
    print(f'Result: {result[0]}')
 

getProductInfo()