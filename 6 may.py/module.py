# import os
# print(os)

# import lj
# lj.my_function(4,5,8)

# import lj
# lj.fruicts(pain apple,cherry,avocado)





# products = {
#    'утюг': 3500,
#    'телевизов': 24000,
#    'стиральная_машина': 30000,
#    'фен': 5500
# }
# Дан список продуктов products.
# Как раз в магазине проходит скидка в размере 15% на весь товар
# Вычислите сколько денег нужно чтобы купить весь товар ? 
products = {
    'утюг': 3500,
    'телевизор': 24000,
    'стиральная_машина': 30000,
    'фен': 5500
}
print(products['фен']+products['утюг']+products['телевизор']+products['стиральная_машина'])   
print(products)









# Задание 2
# Дано целое число из трёх цифр.
# Напечатайте сумму цифру числа.
# Пример ввода
# 123
# Пример вывода
# 6
n = int(input())
summ = 0
many = 1
while n > 0:
    d = n % 10
    d = summ + d
    many = many * d
    n = n // 10
print('summa:' ,summ)
print('product:' ,many)    


n = input()
summ = 0
moon = 1
for digit in n:
    if digit.isdigit():
        summ +=int(digit)
        moon +=int(digit)
print('сумма: ', summ)
print('product: ', moon)        
# Задание 3
# Дано целое двузначное число.
# Напечатайте число, в котором правая и левая цифры поменяны местами.
# Пример ввода
# 79
# Пример вывода
# 97
a = input('Введите двузначное число: ')
a2 = a[::-1]
print('Пример вывода)', a2)


b = input('двухзначное цифра: ')
b = a[::-1]
print('example)',b)