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
        
list = []
while True:

    name = input('Ürün adı: ')
    price = float(input('Ürün Fiyatı: '))
    imageURL = input('Ürün Fotoğraf Linki: ')
    description = input('Açıklama: ')

    list.append((name, price, imageURL, description))
    
    result = input('Ürün eklemeye devam etmek istiyor musunuz? (y/N)')
    if result == 'n' or result == 'N':
        print('Kayıtlar veritabanına aktarılıyor...')
        # Kayıt
        print(list)
        insertProducts(list)
        break

# insertProduct(name, price, imageURL, description)