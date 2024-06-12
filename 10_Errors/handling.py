# Error => hata

# Error

# print(a)          => NameError
# int('1a2')        => ValueError
# print(10/0)       => ZeroDivisionError
# print('denem'e)   => SyntaxError

# Error handling => hata yönetimi

while True: # Doğru bilgi girilene kadar devam ettirmeye yarar

    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    # except (ZeroDivisionError, ValueError) as e:
    #     print('Cannot enter this!')
    #     print(e) # hangi objeden gelen bir hata onu gösterir
        
    # except ValueError:
    #     print('Cannot divide by string')

    except Exception as ex:
        print(ex)

    else:
        # print('Everything fine!')
        break
    finally: #finally bloğu her zaman çalışır farketmeksizin.
        print('Try except ended.')

