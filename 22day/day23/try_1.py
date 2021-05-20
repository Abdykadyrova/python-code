
cars ={
    'toyota':1997,
    'hunday':2006,
    'kia':2008,
    'rng':2017,
    'BMW':2020,
    'porter electro':2019
}
try: 
    
    car_file = open('cars.txt','w')
    for key,value in cars.items():
        print(key,value)
        car_file.writelines(key + ',' + str(value) + '\n')
    # text = 'toyota, 1997',
    # car_file.writelines(text)  
except  FileNotFoundError:
    print('не правельный папка не найдено!!!')        
