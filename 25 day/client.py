class Client:
    def __init__(self,name,login,password):
        self.name = name
        self.login =login
        # self.__password = password
        self.set_password(password)
        
    def set_password(self,password):
        if len(password) < 8:
            print('password very easy')
        else:    
            self.__password = password
            print('password very good', self.__password)
    def get_password(self):
        return 'шифрованный'
    def raw_password(self):
        print('никому не рсказывыйте')   
        return self.__password 

#internet shop
turgun = Client('Турунбай','trgun','14544254')

# print(turgun.set_password(90))
# print(turgun.get_password())
# print(turgun.raw_password())

