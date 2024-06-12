# 12. Functions_1

# def greeting(name):
#     print('hello', name)
    

# # print(greeting('ali'))
# # print(greeting)

# sayHello = greeting # bilginin tutulduğu yerdeki dataya atanır

# print(sayHello)
# print(greeting)

# sayHello('ali')

# del sayHello # sayHello'nun tanımlamasını sildik
# print(greeting)


#----> ENCAPSULATION

def outer(num1):
    print('only outer')
    def inner_increment(num1):
        print('inner')
        return num1 + 1

    num2 = inner_increment(num1)    
    print(num1, num2)


outer(10)

def factorial(number):
    if not isinstance(number, int): # gönderilen number'in ilgili class'a ait mi değil mi kontrol eder.
        raise TypeError('Number must be an integer.')
    
    if not number >= 0:
        raise ValueError('Number must be zero or positive')
    
    def inner_factorial(number):
        if number <= 1:
            return 1
    
        return number * inner_factorial(number - 1)

    return inner_factorial(number)

try:
    print(factorial(5))
except Exception as ex:
    print(ex)
    
# factorial(5)
# |-- inner_factorial(5)
# |   |   |-- inner_factorial(4)
# |   |   |   |   |-- inner_factorial(3)
# |   |   |   |   |   |   |-- inner_factorial(2)
# |   |   |   |   |   |   |   |   |-- inner_factorial(1)  # returns 1
# |   |   |   |   |   |   |   |-- return 2 * inner_factorial(1)  # returns 2
# |   |   |   |   |   |-- return 3 * inner_factorial(2)  # returns 6
# |   |   |   |-- return 4 * inner_factorial(3)  # returns 24
# |   |-- return 5 * inner_factorial(4)  # returns 120
