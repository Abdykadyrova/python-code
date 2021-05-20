
try:
    a = int(input('введите число 1: '))
    b = int(input('введите разделитель числа: ')) 
    z = a / b * jok
    print(z)
except NameError:
    print('неправельный переменный')    
except ValueError:
    print('write num not word!!!!')    
except ZeroDivisionError:
    print('')
except:
    print('ой ошибка!!!')    