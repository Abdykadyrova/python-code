
#curs = {
#    "EUR": 101.65,
#     "USD": Курс валют
#   84.80,
#     "RUS": 1.23,
#     "KZT": 0.200
# }
# Мен сом турундо акчаны берсем валюта боюнча
# конвертация кылып бер.
# Мисалы: 60 000 сомду доллар кылып бер
# 78 685 сомду Евро кылып бер
# 50 000 сомду Тенге кылып бер
# 45 000 сомду Рубль кылып бер
# def convert(money, valuta):
#     if curs.get(valuta) != None:
#         result = money / curs[valuta]
#         print(valuta, ':', result)
#     else:
#         print('Андай валюта жок')
# valuta = input('Кайсы валютага которосуз: ')
# money = float(
#     input('Сумманы айтыныз сом турундо: ')
# )
# convert(money, valuta)
# molmol altyn berse any akcha kylyp berish kerek
#70 000 somduk altyn
#50000 somduk kumush
#20000 somduk bjutera


sena {
    'altyn': 900.99,
    'kumush': 501.8,
    'bjutera': 200.65
}

def convert(metal,som):
    if sena.get(som) != None:
        prosess = metal / sena[som]
        print(som,':',prossess)
    else:
        print('we dont have such kind of thing')
som = input('which kind of thing do you want exchange: )            
metal = float(
    input('write GR sent: ')

)
convert(metal/som)





