# Из Dictionary No1:
# Добавьте в меню
# 'besh_barmak' который
# стоит 130 сом.

# Оказалось лагман
# слишком дешевый.
# Обновите цену на 135

# Ваш повар отвратительно
# готовит борщ, поэтому
# хотите удалить это

# блюдо.
# Удалить borsh

# menu = {
#     'beshbarmak':'130som',
#     'borsh':'100',

# }
# print(menu)

# menu ['beshbarmak']=135
# print(menu)


# del menu ['borsh']
# print(menu)



# Из Dictionary No1:
# Добавьте в меню
# напитки как ключ "drinks",

# А список всех доступных
# напитков: ['Coca-Cola',
# 'Sprite', 'Fanta'] как его

# значение.

# mylist = {

# }

# for b in range(4):
#     name = input(' запишите ваш имя ')
#     passw = int(input(' запишите пароль '))
#     mylist[name] = passw


# print(mylist)






# peopls = {
#     'jake':'teacher',
#     'nurbek':'lower',
#     'kuba':'sowtwear inganier',
#     'aibike':'doctor',
#     'damir':'dentist',
# }
# for b in peopls:
#     # print('b,здравствуйте мне зовут jake, мне 23')
#     # print('b,здравствуйте мне зовут nurbek, мне 32')
#     # print('b,здравствуйте мне зовут kuba, мне 24')
#     # print('b,здравствуйте мне зовут damir, мне 34')
#     print('hello my name is [' peoplse'], i/am 23')



#     Создайте цикл который
# справшивает у

# пользователя 10 чисел и
# добавьте их в SET.
# Сделайте так чтобы эти
# данные уже никто не смог

# поменять позже.








#курс валют

cours = {
    'EURO':101.65,
    'USD':84.80,
    'RUS':1.23,
    'KZT':0.200
}
#мен сом турундо акчаны берсем авалюта боюнча конвертация кылып берю
#МИСАЛЫ   60000 сомду доллар кылып бер 
#78 685 сомду Евро кылып бер
#50 000 сомду тенге кылып бер
#45 000 сомду рубль кылып бер 

def convert (money,valuta):
    if cours.get(valuta)!= None:
        result = money/cours[valuta]
        print(valuta,':',result)
    else:
        print('андай валюта жок')
valuta = input('кайсы авлютага которосуз: ')
money = float(
    input('сумманы айтыныз сом турундо:')
)            
convert(money,valuta)

cours = {
    'EURO':101.65,
    'USD':84.80,
    'RUS':1.23,
    'KZT':0.200
}
def convert (money,valuta):
    if cours.get(valuta)!= None:
        result = money/cours[valuta]
        print(valuta,':',result)
    else:
        print('андай валюта жок')
valuta = input('кайсы валютага которосуз: ')
money = float(
    input('сумманы айтын сом турундо: ')
)            
convert (money,valuta)



