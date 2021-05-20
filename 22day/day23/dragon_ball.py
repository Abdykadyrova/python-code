
# magics = {}
# enemy = {
#     'dragon':50
# }

# magic_file = open('magic.txt','r')
# magic_array = magic_file.readlines()
# for cur_magic in magic_array:
#     magic_striped = cur_magic.strip()
#     magic_splitted = magic_striped.split(',')
#     # print(magic_splitted[0],magic_splitted[1])
#     magics[magic_splitted[0]] = float (magic_splitted[1]) 
# print('ваш противник',enemy)
# while enemy ['dragon'] > 0:
#     udar = input('выберите удар: ')
#     u = magics[udar]
#     enemy['dragon'] = enemy['dragon']-u
#     print('ХР врага: ',enemy['dragon'])
# print('вы победили жизнь врага: ',enemy['dragon'])    



















 #Задача 1.
# создайте файл friends.txt
# напишите туда имена своих друзей и их возраст с помощью open('friends.txt', 'w')
# Например содержимое файла должен быть:
    # Руслан,26
    # Кадыр,23
    # Ерлан,22

friends_file = open('friends.txt','w')
friendsss = friends_file.writelines()


# Задание 2
# Создайте функцию splitFio(fio) которое разделяет имя и фамилию
# Например:
    # Ввод: splitFio('Асан уулу Рулсан')
    # Вывод: Имя: Руслан Фамилия: Асан уулу
    
    # Ввод: splitFio('Тургунбаева Айсулуу')
    # Вывод: Имя: Айсулуу Фамилия: Тургунбаева



# Задание 3
# создайте файл tasks.txt и напишите туда разные уравнения
# создайте функцию run_task() которое открывает файл tasks.txt и выполняет уравнения
# Например содержимое файла tasks.txt:
# 20+99
# 199/3
# 200**5
# 500+1976
# При запуске функции run_task()
# Вывод:
#   20+99=119
#   199/3=106
#   200**5=320000000000
#   500+1976=2476