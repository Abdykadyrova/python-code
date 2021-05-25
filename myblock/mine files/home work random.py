
mesto = {
    'Дархан',
    'Манас-Ата',
    'Палван-Ата',
    'Караван',
    'Баарына кошулам',
    'Офис',
    'Фаиза'
}
meats = {
    'Аш',
    'Пицца',
    'Пирожок',
    'Ачуу-Эт',
    'Лагман',
    'Мясной рулет',
    'Ташкентский Аш',
    'Шашлык',
    'Стейк',
    'Тиббон'
}
p = int(input('напишите место'))
for i in range(p):
    print(1 ,'place:' ,mesto.pop())

t = int(input('choose the meals'))
for v in range(t):
    print(4,' meal:',meats.pop())   

place = {
    'vilage',
    'city',
    'osh',
    'jalal abad',
    'japalak',
    'bishkek'
} 
l = int(input('place where nuriz will get marridge'))
for i in range(l):
    print(2,'place:', place.pop())
    
man = {
    'ruslan',
    'elaman',
    'kairat',
    'askar',
    'nurlan'
}
k = int(input('boy that will be molmols boyfriend'))
for m in range(k):
    print(1,'boy:',man.pop())


man = {
    'zukur',
    'aibek',
    '555',
    'beytaanysh',
    'almanbet',
    'kara suu',
    'argen',
    'limon'
}    
d = int(input('boys that will be veneras boyfriend'))
for u in range(d):
    print(1,'man:', man.pop())

place = {
    'nookat',
    'kadam jai',
    'kurshab',
    'osh',
    'alai',
    'karavan',
    'j abad',
    'kok jar'
}    
h = int(input('place where venera get marridge'))
for n in range(h):
    print(1,'place:', place.pop())

    