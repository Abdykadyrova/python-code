#Задача 1.
# создайте файл friends.txt
# напишите туда имена своих друзей и их возраст с помощью open('friends.txt', 'w')
# Например содержимое файла должен быть:
    # Руслан,26
    # Кадыр,23
    # Ерлан,22



# frend = {
#     'diana':'20',
#     'arapa':'19',
#     'aijamal':'21',
#     'alia':'22',
#     'anara':'18'
# }

# friends_file = open('friends.txt','w')
# for key,value in frend.items():
#     print(key,value)
#     friends_file.writelines(key + ',' + str(value) + '\n')    







#Задание 2
# Создайте функцию splitFio(fio) которое разделяет имя и фамилию
# Например:
    # Ввод: splitFio('Асан уулу Рулсан')
    # Вывод: Имя: Руслан Фамилия: Асан уулу
    
    # Ввод: splitFio('Тургунбаева Айсулуу')
    # Вывод: Имя: Айсулуу Фамилия: Тургунбаева

def splitFio(fio):
    print("\nname:"  + fio + " familian name:" + fio)
splitFio('aiganysh abdykadyrova')







#Задание 3
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

task_file = open('tasks.txt' ,'r')
task_lists = task_file.readlines()


for task in task_lists:
    try:

        t = task.strip()
        print(t,'=',eval(t))
    except ZeroDivisionError:
        print('на ноль делить нелзя')
    except:
    except FileNotFoundError:
        print()    
        print('problem iss frong!!!')




