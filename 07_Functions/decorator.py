# 12. Functions_4

# bir fonksiyona bir özellik eklemek istediğimiz zaman kullanılır.


def my_decorator(func):
    def wrapper(name):
        print('fonksiyondan önceki islemler')
        func(name)
        print('fonksiyondan sonraki islemler')
    return wrapper

@my_decorator
def sayHello(name):
    print('Hello ', name)    

# def sayGreeting():
#     print('Greeting')
    
sayHello('ali')

# sayHello = my_decorator(sayHello) # decorative içine bir fonksiyon gönderip belirli bir yerde çağırıp kullanıyoruz. 
# şimdi bunun yerine @ işareti kullanılabilir. @my_decorator
# sayHello()

# sayGreeting = my_decorator(sayGreeting)
# sayGreeting()

import math
import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1) # 1 saniye uygulamayı uyuttuk

        finish = time.time()
        print("fonksiyon " + func.__name__ + " " + str(finish-start) + " saniye sürdü.")
        
    return wrapper

@calculate_time
def usalma(a,b):
    # start = time.time()
    # time.sleep(1) # 1 saniye uygulamayı uyuttuk
     
    print(math.pow(a,b))
    
    # finish = time.time()
    # print("fonksiyon " + str(finish-start) + " saniye sürdü.")
    
@calculate_time
def factorial(num):
    # start = time.time()
    # time.sleep(1)
    
    print(math.factorial(num))
    
    # finish = time.time()
    # print("fonksiyon " + str(finish-start) + " saniye sürdü.")

@calculate_time
def toplama(a,b):
    print(a+b)


usalma(2,3)
factorial(5)
toplama(5)