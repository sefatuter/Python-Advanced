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
    
    # sql = "Select * FROM Products"
    # sql = "Select * FROM categories"
    # sql = "Select * FROM products INNER JOIN categories ON categories.id = products.categoryid" # birbirine bağladık.
    # sql = "Select products.name, products.price, categories.name FROM products INNER JOIN categories ON categories.id = products.categoryid" # Özellikle istediğimiz kolonları aldık
    # sql = "Select products.name, products.price, categories.name FROM products INNER JOIN categories ON categories.id = products.categoryid WHERE categories.name = 'Telefon'" # Categories tablosunun sadece telefon olanları getirir.
    # sql = "Select products.name, products.price, categories.name FROM products INNER JOIN categories ON categories.id = products.categoryid WHERE products.name LIKE '%Iphone%'" # içinde Iphone geçen kayıtları getirir.
    sql = "Select p.name, p.price, c.name FROM products AS p INNER JOIN categories AS c ON c.id = p.categoryid WHERE p.name LIKE '%Iphone%'" #  "FROM products AS p", "INNER JOIN categories AS c" ile atadık işimiz kolaylaşır.
    
    
    cursor.execute(sql)
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.error as err:
        print('Hata: ', err)
    finally:
        connection.close()
        print('Database Bağlantısı Kapandı.')
      
        
getProducts()