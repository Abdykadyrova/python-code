# import module_0

# phone = input('write your phone number: ')
# module_0.check_phone_num



# import module_0

# module_0.translate()

# fio = module_0.getfullname('aiganysh','abdykadyrova')

# print(fio)


# from mylib.calc import calculator
# from mylib.calc import hello
# import mylib.calc
# calculator(10,50,'+')
# hello()


# import mylib.calc as s

# s.calculator(10,50,'+')
# s.hello()

# import os 
# print(os.listdir())


# import math 
# print(math.pow(5,2))




# import random
# # print(random.randint(1,999))

# rstart = int(input('введите начала рандом: '))
# rend = int(input('введите конца рандом: '))
# print(random.randint(rstart,rend))




# import random

# mynum = int(input('загадай число я попробую это число через функцию randint: '))
# choose_num = random.randint(1,mynum + 10)
# while choose_num != mynum:
#     choose_num = random.randint(1,mynum + 10)
#     print('это число твое ? ', choose_num)
# if choose_num == mynum:
#     print('i find your num', choose_num)
 
import random
j = int(input('write number: '))
a = random.randint(1,j+100) 
while a!= j:
    a = random.randin(0,j+100)
    print('is it your num?', j)
if a == j:
    print('i find your num',j)    