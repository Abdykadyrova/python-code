##    'aku',
  #    'bek',
#     'nur',
#     'timu',
#     'aku',
#     'nur',
#     'timu',
# }
# print(n)

# Emails = [
#     'aku@gmail.com',
#     'bek@gmail.com',
#     'nur@gmail.com',
#     'aku@gmail.com',
#     'bek@gmail.com',
#     'nur@gmail.com',
# ]
# Emails = set(Emails)
# for Email in Emails:
#     print('на почту', Email, 'отправлен сообщение')




# frends = {
#     'diana',
#     'asel',
#     'arapa',
#     'madina',
#     'dior',
#     'diana',
#     'asel',
#     'arapa',
#     'madina',
#     'dior',
    
# }    
# print(frends)

# products = {
#     'shugar',
# }
# print(products)


# products.add('tea')
# products.add('salt')

# print(products)


# colors = {
#     'red',
#     'black',
#     'green',

# }
# print(colors)

# colors.add('blue')
# colors.add('yellow')
# print(colors)


# j


computers = set()
for t in range(6):
    computers.add(input('laptops').lower())
print(computers)   


# products = {
#     'shugar',
#     'salt',
#     'water',
#     'tea',
# }
# print(products)
# products.remove('water')
# print('after',products)


# fruits = {
#     'watermelon',
#     'apple',
#     'cherry',
# }
# print(products)
# products.update(fruits)
# print('after',products)

# comp1 = {'lg','google','honda'}
# comp2 = {'honda','lg','toyota','google'}
# comp3 = {'bmw','jkl',}
# # differnce_comp = comp2.difference(comp1)
# # print(diffe
# comp1.intersection_update(comp2)
# comp1.intersection_update(comp3)
# print(comp1)

k = {
    'jek',
    'rock',
    'job',
    'tom',
    'rik',
    'john',
    'tom',
}
lot = int(input('введите количество призовых мест'))

# mest_1 = print('1 место:',k.pop())
# mest_1 = print('2 место:',k.pop())
# mest_1 = print('3 место:',k.pop())
for i in range(lot):
    print( i + 1 ,'место:' , k.pop())
    


