class Person:
    def __init__(self, name = 'Нету', age = 0):
        self.name = name
        self.__age = age

    def set_age(self, age):
        if age > 100:
            print('Не допустимый возраст')
        else:
            self.__age = age
    
    def get_age(self):
        if self.__age == 0 or self.__age == None:
            return 'вы не ввели возраст'
        else:
            return self.__age


me = Person( name = 'Zalkar')
print(me.name)
me.set_age(90)
print(me.get_age())

