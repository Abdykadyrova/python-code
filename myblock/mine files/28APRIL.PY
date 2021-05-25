dictationary
dict
audio = {
    'name':'audi',
    'vol':'4.0',
    'color':'black',
    'price':2600,
    12:55
}
print('model',audio['name'])
print('obem',audio['vol'])
print('color',audio['color'])
print('speed',audio['price'])
print('speed',audio[12])


panda = {
    'name':'тибетская панда',
    'ves':'400 kg',
    'color':'black and white',
    'type':'sut emuuchu',
    'eat':'chop jeit'

}
print(panda['name'] ,panda ['eat'])

hours = {
    'name':'chagylgan',
    'ves':'800kg',
    'color':'blue',
    'eat':'bede'


}
print(hours['name'],hours['ves'],hours['color'],hours['eat'])



autosalon

car1 = {
    'model':'honda fit',
    'year':'2008',
    'vol':'1.4',
    'price':'5000$'

}

car2 = {
    'model':'bmw',
    'year':'2010',
    'vol':'2.0',
    'price':'10000$'

}


car3 = {
    'model':'lexus',
    'year':'2015',
    'vol':'4.0',
    'price':'15000$'

}

car4 = {
    'model':'djaz',
    'year':'2020',
    'vol':'3.0',
    'price':'59000$'
}    

print('welcome to auto salon.')
print('1:',car1['model'])
print('2:',car2['model'])
print('3:',car3['model'])
print('4:',car4['model'])

select_car = int (input('which car do you choose'))
if select_car == 1:
    print('model',car1['model'])
    print('year',car1['year'])
    print('vol',car1['vol'])
    print('price',car1['price'])


elif select_car == 2:
    print('model',car2['model'])
    print('year',car2['year'])
    print('vol',car2['vol'])
    print('price',car2['price'])

elif select_car == 3:
    print('model',car3['model'])
    print('year',car3['year'])
    print('vol',car3['vol'])
    print('price',car3['price'])

elif select_car == 4:
    print('model',car4['model'])
    print('year',car4['year'])
    print('vol',car4['vol'])
    print('price',car4['price'])

else:
    print('we dont have this car')    



car1 = {
    'model':'honda fit',
    'year':'2008',
    'vol':'1.4',
    'price':'5000$'

    }

print('welcom to auto bootcamp.')
print('машина в наличии:')
print('1:',car1['model'])
print('2:',car2['model'])
print('3:',car3['model'])

s = int(input('which car?:'))

if s == 1:
    carKey = input('which character. do you want:')
    if car1.get(carKey) != None:
        print(carKey, car1[carKey])
    else:
        print('we dont have this car')   



