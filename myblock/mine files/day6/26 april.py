# #1. Используя while выведи на экран число от 10 до 100:
# d = 10
# while d < 100:
#     print(d)
#     d = d + 1

# # 2. С помощью while у человека имя фамилию и отчество:
# # Проси до тех пор пока человек не вводит свои данные

 
# mnn = " "
# while True:
#     print("пожалуйста напишите свое имя!")
#     print("пожалуйста напишите свое фамилию")
#     print("пожалуйста напишите свое отчество")
#     mnn = input('ваша данные')
#     if mnn == 'aku kubanycaky kadyrohbekovna' :
#         print('thanks your information here') 






# # 3. Дан список гостей, на сегодняшную вечеринку :
# # guests = ['Axe', 'Tom', 'Jax', 'Rik', 'Sam', 'Zot']
# # Создай цикл while чтобы проверить приходящих гостей.
# # Если человек вводит имя которое нет в списке то выводи
# #   Сообщение: Извините, ваше имя нет списке. Sorry.
# # Если человек вводит имя которое есть в списке то выводи
# #   Сообщение: Добро пожаловать гость заходите и наслаждайтесь.
# guests = ['Axe', 'Tom', 'Jax', 'Rik', 'Sam', 'Zot']
# kelgender = 0
# while len (guests) != kelgender:
#     gost = input('your namme')
#     if guests.count(gost) == 1 :
         
#         kelgender = kelgender + 1 
#         print('Добро пожаловать гость заходите и наслаждайтесь.')
#     else :
        
#         print(' Извините, ваше имя нет списке. Sorry')














#      # 4. Создай программу которая проверяет сложность пароля:
# # Если длина пароля:
# #   меньше 4: <<очень легкий>>.
# #   больше 4 и меньше 8: <<простой>>.
# #   больше 8: <<надежный пароль>>.

# # Продолжайте спрашивать <<надежный пароль>> пока клиент не введет сложный пароль  
# # Если клиент вводит очень легкий пароль выводи
# #   Сообщение: Пвв твой пароль даже школьник взломает

# # Если клиент вводит простой пароль выводи
# #   Сообщение: Я взломаю твой пароль за пару секунд зуб даю

# # Если клиент вводит надежный пароль выводи
# #   Сообщение: Хмм твой пароль довольно сложный, Молодец

# while True:
#     password = input('придумайте парлль :')
#     if len (password)<=4:
#         print('очень легкий пароль')
#     elif len(password) >4 and len(password) <8:
#         print('я взломаю твой акаунт')
#     elif len(password) >=8:
#         print('xmm твой пароль довольно сложныйб Мо5лодец')
#         break     
# 
# n = int (input('да сколько нужно посчитать '))
# c = 0
# while c < n :
#     c = c +1 
#     print(c)

# for  i in range(10):
#     print('6','*',i,'='6 * i)
#     print(i)
    


# for i in range(11):
#     for k in range(11):   
#         print(i,'*',k,'=',i * k)



roles = ['Admin','manager','author','users','guest']
users = ['Tom','Jake','Rock','John','Janet','Frank']
# for user in users:
#     print( user,'is', manager[0])
#     print(user,'is'roles[1])
#     print(user,'is'roles[2])
#     print(user,'is'roless[3])
#     print(user,'is' rolers[4])

for user in users:
    
    for role in roles:
     print(user,'is',role)
    print()