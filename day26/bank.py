import random

class Bank:
    def __init__(self, bank_name, bank_balance):
        self.bank_name = bank_name
        self.bank_balance = bank_balance

    # Информация о банке
    def bank_info(self):
        print('Добро пожаловать: ', self.bank_name)

    # оборот банка
    def get_bank_balance(self):
        print(
            'Общий баланс банка:', 
            self.bank_balance
        )

    # открытие счета
    def create_account(self, client_name, password):
        rnd = random.randint(1000, 2000)
        self.accounts = {
            rnd: {
                "name": client_name,
                "password": password,
                "balance": 0
            }
        }
        print(
            'Ваш аккаунт открыт:','\n',
            'Имя: ',self.accounts[rnd]['name'],'\n',
            'Пароль: ',self.accounts[rnd]['password'],'\n',
            'Баланс: ',self.accounts[rnd]['balance'],'\n',
        )
        print('Счет вашего аккаунта:', rnd)
        return rnd
    
    # данные о счете clienta
    def get_account(self, nomer):
        print('Ваш счет:', self.accounts[nomer])

    # получаем баланс на счете
    def get_balance(self, nomer):
        print(
            'Деньги на вашем счете:',
            self.accounts[nomer]['balance']
        )

    # добавляем деньги на наш счет
    def add_money_to_balance(self, nomer, money):
        self.accounts[nomer]['balance'] = self.accounts[nomer]['balance'] + money
        print('Ваши деньги увеличились на:', money)

    # создаем электронную карту
    def create_card(self, 
    client_name, type, password):
        pass

    # получаем карты клиента
    def get_credits_card(self, client_name):
        pass