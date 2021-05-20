class Animal:
    def __init__(self,name,weight,kolichestvo_zd):
        self.name = name
        self.weight = weight
        self.kolichestvo_zd = kolichestvo_zd

    def attack_foot(self):
        print(f'{self.name}   can atack with food')    
        pass


class Lion(Animal):
    def __init__(self,name,weight,kolichestvo_zd):
        Animal.__init__(self,name,weight,kolichestvo_zd)
    def bite(self):
        print(f'{self.name}   can bite')    
    pass

class KingKong(Animal):
    def __init__(self,name,weight,kolichestvo_zd):
        Animal.__init__(self,name,weight,kolichestvo_zd)
    def hit(self):
        print(f'{self.name}  can hit')    
    pass

class Krocodile(Animal):
    def __init__(self,name,weight,kolichestvo_zd):
        Animal.__init__(self,name,weight,kolichestvo_zd)
    def eat(self):
        print(f'{self.name}   can eat everything')    


predator = Lion('Tarzan',200,100)
predator.attack_foot()
predator.bite()
print('name: ', predator.name)
print('weight: ', predator.weight)
print("количество сил:", predator.kolichestvo_zd)
vulture = KingKong('Maugli',1000,500)
vulture.attack_foot()
vulture.hit()
print( 'name: ', vulture.name)
print('weight: ',vulture.weight)
print('kolichestvo_zd: ',vulture.kolichestvo_zd)
harpy = Krocodile('Gena',400,300)
harpy.attack_foot()
harpy.eat()
print('name: ', harpy.name)
print('weight: ', harpy.weight)
print('kolichestvo_zd: ', harpy.kolichestvo_zd)    






    

# у каждого животного должен быть
# имя, вес, количество здоровья
# у каждого должна быть attack функция
# attack должны быть разными
# Еще у каждого должна быть общая атака
# attack_foot - удар ногой















class House:
    def __init__(self,name,color,balkony,windows,doors,rooms,bath,toilet):
        self.name = name
        self.color = color
        self.balkony = balkony
        self.windows = windows
        self.doors = doors
        self.rooms = rooms
        self.bath = bath
        self.toilet = toilet
    def description(self):
        print(f'{self.name}  is ten floor and there/re 30 room,90 windows,40 doors') 

class Vip(House):
    
    def house_balkon(self):
            self.balkon = True
            print(self.balkony)

           

    def house_balkon2(self):
            self.balkon = False
            print(self.balkony)

home = Vip('Emakom ','orange',90,40,30,28,30,32)
home.description()
home.house_balkon()  
home.house_balkon2() 
print('name :',home.name)
print('color: ',home.color)
print('balkony: ',home.balkony)   
print('windows: ',home.windows)
print('doors: ',home.doors)
print('rooms: ',home.rooms)  
print('bath: ',home.bath)
print('toilet: ',home.toilet)      










# class Animal:
#     def init(self, name, hp):
#         self.name = name
#         self.hp = hp


# class Lion(Animal):
#     def to_attack(self):
#         print(self.name,':','Roar', 'Tackle')
#         print('health: ', self.hp)

# class KingKong(Animal):
#     def to_attack(self):
#         print(self.name,':','Hyper Punch','Tackle')
#         print('health: ', self.hp)


# class Krokodile(Animal):
#     def to_attack(self):
#         print(self.name,':','Earthquake','Tackle')
#         print('health: ', self.hp)
# animal  = Animal('leo',55)

# leo = Lion(
#     name='leo',
#     hp=130
# )
# kingkong = KingKong(
#     name='kingkong',
#     hp=630

# )    
# krok = Krokodile(
#     name='krok',
#     hp=55
# )


# kingkong.to_attack()
# leo.to_attack()
# krok.to_attack()