import bank

demir = bank.Bank(
    bank_name = 'Demir Bank',
    bank_balance = 750_000_000.00
)

demir.bank_info()
demir.get_bank_balance()

# открываю для себя счет на банке
nomer = demir.create_account(
    client_name='aiganyh',
    password=1212
)
print('Я получил номер счета:', nomer)

# я пополняю деньги на свой баланс
demir.add_money_to_balance(nomer, 7800)
demir.add_money_to_balance(nomer, 9600)

# Еще раз проверяю свой счет
demir.get_account(nomer)