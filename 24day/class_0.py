# class Tiger:
#     name = 'sherhan'
#     weight = 400
#     age = 5
#     color ='orange woght and black'
#     speed = 50
#     power = 99

# tigr = Tiger()
# print(Tiger.name)    
# print(Tiger.weight)
# tigr2 = Tiger()
# tigr2.name = 'mursik'
# tigr2.weight = 500
# print(tigr2.name)
# print(tigr2.weight)


# class Human:
#     name = ''
#     color = ''
#     rassa = ''
#     gender = ''
#     weight = ''
#     age = ''
    
# zalkar = Human()
# zalkar.name ='zalkar' 
# zalkar.color ='black'
# zalkar.gender ='male'
# zalkar.weight ='65'
# zalkar.age ='18' 
# print(zalkar.name)
# print(zalkar.color) 
# print(zalkar.gender)  
# print(zalkar.weight)  
# print(zalkar.age)  



# #Залкар Агай, [10.05.21 15:31]
# class Human:
#     name = ''
#     color = ''
#     rassa = ''
#     gender = ''
#     weight = ''
#     age = ''
#     hair = ''
#     hair_color = ''
#     def to_walk(self):
#         print(self.name, 'Баса алат')
    
#     def to_speak(self, word, word2):
#         print(self.name, 'govorit', word, word2)


# belek = Human()
# belek.name = 'Белек'
# belek.color = 'Будай цветтуу'
# belek.rassa = 'Кыргыз'

# belek.to_walk()
# belek.to_speak('Салам кандай ?', 'Жакшы озун')





# Обьекты (Классы)
# class Tiger:
#     name = 'Шерхан'
#     weight = 400
#     age = 5
#     color = 'ОранжевоЧерныйБелый'
#     speed = 50
#     power = 99

# tigr = Tiger()
# tigr2 = Tiger()
# tigr2.name = 'Мурсик'
# tigr2.weight = 300

# print(tigr.name)
# print(tigr2.name)
# print(tigr2.weight)


# class Human:
#     name = ''
#     color = ''
#     rassa = ''
#     gender = ''
#     weight = ''
#     age = ''
#     hair = ''
#     hair_color = ''
#     def to_walk(self):
#         print(self.name, 'Баса алат')
    
#     def to_speak(self, word, word2):
#         print(self.name, 'govorit', word, word2)


# belek = Human()
# belek.name = 'Белек'
# belek.color = 'Будай цветтуу'
# belek.rassa = 'Кыргыз'

# belek.to_walk()
# belek.to_speak('Салам кандай ?', 'Жакшы озун')




ai_92 = 49.50
ai_95 = 51.50

class Car:
    rasxod_100 = 12
    def __init__(self, name, year, color, volume):
        self.name = name
        self.year = year
        self.color = color
        self.volume = volume
    
    
    def get_volume(self):
        print('Мой обьем:', self.volume)
    
    
    def get_rashodprice(self,km):    
        r = self.get_rasxod(km)
        print('92 na ',km,'km',r * ai_92,'som')
        print('95 na ',km,'km',r * ai_95,'som')
    

    def get_rasxod(self, km):
        r = (km / 100) * self.rasxod_100
        # print('Расход на', km, r)
        return r

    # def get_rasxod_price(self, km):
    #     r = (km / 100) * self.rasxod_100 
    #     print('Расход на', km, d)
    #     print('Расход на', km, s)

mycar = Car(
    name = 'Matiz 1', 
    year = 2000,
    color = 'Белый',
    volume = 3.5,
)

mycar.get_volume()
mycar.get_rasxod(140)
mycar.get_rashodprice(140)










#Создай Class Teacher
# свойство:
# name - имя учителя
# age - возраст учителя 
# predmet - имя предмет (по какому предмету препод-т)
# создайте функции:
# to_teach(self): - должна показывать по какому предмету обучает
    
# На основое Class Teacher создай обьекты учителей по:
# Физике  
# Биологии
# Математики

class Teacher:
    name = ''
    age = ''
    predmet = ''
    def to_teach(self):
        print(self.name,'to teaches us',self.predmet)
aku = Teacher()
aku.name = 'aku'
aku.age = '28'
aku.predmet = 'math'
print(aku.name)
print(aku.age)
print(aku.predmet)
aku.to_teach()
#
aika = Teacher()
aika.name = 'aika'
aika.age = '22'
aika.predmet = 'phiziks'
print(aika.name)
print(aika.age)
print(aika.predmet)
aika.to_teach()
# 
bema = Teacher()
bema.name = 'bema'
bema.age = '26'
bema.predmet = 'chemistry'
print(bema.name)
print(bema.age)
print(bema.predmet)
bema.to_teach()
# 2.
# Создай Обьект Plane реализуй его свойство и умение летать
class Plane:
    def __init__(self,name,year,color,volume,length):
        self.name = name
        self.year = year
        self.color = color
        self.volume = volume
        self.length = length
    def get_volume(self):
        print('Мой обьем:', self.volume)
    def technik_fling(self):
        print(self.name, 'can fly')

plane = Plane('a97','2020','white','volume','length')
print(plane.name)
plane.technik_fling()
# 3.
# Создай Обьект Hacker реализуй все его свойство и умение 
# Характеристики:
# уровень - уровень хакера
# навыки - какими навыками он обладает
# возраст - возраст хакера
# пол

# Что он может делать ?
# Например: взломать почту, взлом сайта, взлом сети
class Hacker:
    level = ''
    attainments = ''
    age = ''
    gender = ''
    def what_he_can(self):
        print(self.level, 'can hack the site')

    def what_he_can_do(self):
        print(self.level,' can hack the E-mail')   

    def he_can(self):
        print(self.level, 'can networking hacking')  
hackerr =  Hacker()
hackerr.level = 'junior'
hackerr.attainments = 'JAVA'
hackerr. age = 25
hackerr.gender = 'female'
print(hackerr.level)
print(hackerr.attainments)
print(hackerr.age)
print(hackerr.gender)
hackerr.what_he_can()
hackerr.what_he_can_do()
hackerr.he_can()    




class House:
    name =''
    volume = ''
    length = ''
    