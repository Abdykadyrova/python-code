
# number = int(input('1 give one number:'))
# number2 = int(input('2 give second number:'))

# g = input('what kind of problem do you make:')

# if g == '+':     
#     print(number + number2)

# if g == '-':
#     print(number - number2)

# elif g == '*':
#     print(number * number2)    

# elif g == '/':
#     print(number / number2)    


# input('do you want try again?')   







# Задание 2:
    # Даны три переменные "A", "B" и "C". 
    # Изменить значения этих переменных так, чтобы в "A" хранилось значение "A"+"B", 
    # в "B" хранилась разность старых значений "C" - "A", 
    # а в "C" хранилось сумма старых значений "A" + "B" + "C". 
    # Например, A=0, B=2, C=5, тогда новые значения A=2, B=5 и C=7.


# a = 7 
# b = 8
# c = 9

# A  = a + b 
# B = c - a
# C = a + b + c
# print(A)
# print(B)
# print(C)




# Задание 3:
    # Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.



# r = int(input('find perimetr: '))
# s = int(input('find sss: '))    
# perimetr = r + r + s + s
# sss = r * s
# print('пer':,per)
# print('аянт':,aint)

# DonQuiXote, [01.05.21 14:22]
# sideA = int(input("сторона а: "))
# sideB = int(input("сторона б: "))

# perim = sideA + sideB + sideA + sideB;
# area = sideA * sideB;

# print("периметр: ", perim)
# print("площ: ", area)






# Залкар Агай, [01.05.21 14:31]
# Задание 4:
    # Вам даны несколько последовательностей чисел:
    # sequence_0 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0]
    # sequence_1 = [14,10,35,45,'60',70,90,0,105,150,'70']
    # sequence_2 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0]
    # sequence_3 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70']
    # Нужно проверить, все ли числа в КАЖДОЙ последовательности уникальны.
    # Если в последовательности были найдены дубликаты ---> Выведите на экран: "Последовательность не уникальна."
    # Если в последовательности дубликатов найдено не было ---> Выведите на экран: "Последовательность уникальна."
    # Если в решении задания не присутствует цикл ---> Задание не защитано.


sequence_0 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0]
sequence_1 = [14,10,35,45,'60',70,90,0,105,150,'70']
sequence_2 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0]
sequence_3 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70']


sequence_0.sort()
sequence_1.sort()