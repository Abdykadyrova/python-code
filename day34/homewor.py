#Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод init(), внутри которого будут определены два динамических свойства: 
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
class Alphabet:
    def __init__(self, lang, letter):
        self.lang = lang
        self.letter = letter

    def class_py(self):
        print('language:',self.lang)


    def letter_num(self):
        print('letters in',self.lang,': ', self.letter)

alphabet = Alphabet("English", "a,b,c,d,e,f,g")
alphabet.class_py()
alphabet.letter_num()



#############################
 
# # Реализуйте класс Publication, конструктор которого принимает name, date, pages, library, type
class Publication:
    def __init__(self,name,date,pages,library,my_type):
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.my_type = my_type
    def prints(self):
        print(self.name,self.date,self.pages,self.library,self.my_type)

publication = Publication("Emilia",12,9,"Toktogul","kj")     
publication.prints()


# ###########################################################################################

# # Создайте класс Student, в конструкторе которого записывается firstname, lastname студента. 
# # Т.е. при создании экземпляра должны быть переданы имя и фамилия студента.

# ###########################################################################################

class Student:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def emilia(self):
        print(self.firstname,self.lastname)  


pupil = Student('Эмилия','Жолдошбаева')
pupil.emilia()





