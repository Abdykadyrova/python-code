# Problem1

# Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. 
# По умолчанию name = Aman, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, 
# setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента, 
# метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения 
# данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, 
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.
class Student:
    name = 'Aman'
    groupnumber = '10A'
    age = 18



        

    def getName(self):
        print(f'{self.name} is my name')



    def getGroupNumber(self):   
        print(f'{self.name}/s group is 10A') 


    def getage(self):
        print(f'{self.name} is 18 years old')  


    def setNameAge(self):
        print(self.name)


    def setGroupNumber(self):
        print(f'{self.name}/s group we change')



pupil = Student() 
pupil.getName()
pupil.getGroupNumber()
pupil.getage()  
pupil.setNameAge()
pupil.setGroupNumber()
# Problem2

# Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение, 
# multiplication — умножение, division — деление, subtraction — вычитание. 
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
class Math:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.b + self.b)

    def multiplication(self):
        print(self.a * self.b) 

    def division(self):
        print(self.a / self.b) 


    def subtraction(self):
        print(self.a - self.b)             
problems = Math(8,6)         
problems.addition()
problems.multiplication()
problems.division()
problems.subtraction()


# Problem3

# Напишите программу с классом Car. Создайте конструктор класса Car. 
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год). 
# Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. 
# Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self,color,type,year):
        self.color = color
        self.type = type
        self.year = year

    def sss(self):
        print('автомобиль заведен!!!')    

    def ddd(self):
        print('автомобиль заглушен!!!')    

    def ggg(self):
        print(self.year)    

    def fff(self):
        print(self.type)    


new = Car('black','BMW',2015) 
new.sss()
new.ddd()
new.ggg()
new.fff()      