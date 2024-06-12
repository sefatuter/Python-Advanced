# global scope
x = 'global x'

def function():
    # local scope
    # x = 'local x' # yorum satırına alındığında global x yazdırılır
    # çünkü fonksiyon kapsamında x 'e tanımlanmış bir şey yok
    # bu durumda bir üst kapsama ( en yakın ) bakılır o da en yakın global'dir
    # bu nedenle x = 'global x' olarak referans alınır ve bu yazdırılır 
    # ama bir x tanımlanırsa local x kullanılır.
    print(x)
    # burada tanımlananlar dışarıyı etkilemez


function() # fonksiyon kapsamında tanımlandığı için dışarıda global geçerli olur
# fonksiyonlar yeni bir tanımlama alanı oluşturur
print(x)


# global name
name = 'Veli'

def changeName(new_name):
    # local name
    name = new_name # global name eklenirse değişir.
    print(name)

changeName('Ada')
print(name)


name = 'Global string'

def greeting():
    name = 'Melih'

    def hello():
        # name = 'Çınar' # eğer 'Çınar' eklenirse bu referans alınır.
        print('hello ' + name )
        # bir üstteki name'i ifade eder globali değil
        # çünkü bizim hello fonksiyonumuz için global scope greeting()'dir.
    hello()

greeting()

x = 50

def test(x):
    print(f'x = {x}')

    x = 100
    print(f'changed x to {x}')

test(x) # fonksiyon içinde x güncellenmesine rağmen
print(x)# 50 olarak yazdırıldı

# dışarıda tanımlanan x bilgisini fonksiyon içinde değiştirmek için
# global keywordünü kullanmamız gerek

print('------------------')
x = 50

def test():
    global x # bundan sonra fonksiyon içinde x'e yaptığımız işlemler global x'e uygulanır.
    print(f'x = {x}')

    x = 100
    print(f'changed x to {x}')

test() # fonksiyon içinde x güncellenmesine rağmen
print(x)# 50 olarak yazdırıldı


