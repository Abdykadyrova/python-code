
accounts = [
    {
        "name": 'Demir Bank',
        'balance':'5000$',
        'valuta':'som',
        'pin':'12',
    },
    {
        "name": 'Optima Bank',
        'balance':'6574788',
        'valuta':'$$$',
        'pin':'13',
    },
    {
        "name": 'KICB',
        'balance':'90876',
        'valuta':'rub',
        'pin':'14',
    },
    {
        "name": 'Dos-Credo Bank',
        'balance':'2345',
        'valuta':'tenge',
        'pin':'15',
    },
]
cours = { 
    'som':101.65,
    '$$$':84.80,
    'rub':1.23,
    'tenge':0.010
}

for i in accounts:
    print(i)
print('my account:')

for index in range(len(accounts)):
    print(index,accounts[index]['name'])  
aindex = int(input('выберите акаунт:'))
if aindex < 5 and aindex >= 1:
    rindex = aindex - 1
    print(accounts[aindex-1]['name'])
    pin = input('банка тиешелуу pin кодунуз териниз: ')
    if pin == accounts[rindex]['pin']:
        print(
            'welcome to',
            accounts[rindex]['name']
        )
        print(
            'ваш баланс:',
            accounts[rindex]['name']
        )
        print(
            'ваш баланс:',
            accounts[rindex]['balance']
        )
else:
    print('андай акаунт жокоо((')        
for i in banks:
    print(i)
print(banks[0]['name']), banks[0]['address']
print(banks[1]['name']), banks[1]['address']
print(banks[2]['name']), banks[2]['address']
print(banks[3]['name']), banks[3]['address']

for bank in banks:
    print(bank)
for indeks in range(4):
    print(indeks + 1,':',banks[indeks]['name'])

select_bank = int(input('choose bank: '))

for i in range(1,len(banks)+1):
    if select_bank == i:
        print(banks[i-1])
if select_bank < 5 and select_bank>= 1:
    print(
        'баланс банка:',
        banks[select_bank - 1]['balance'],
        banks[select_bank - 1]['valuta'],


        )      
          
else:
    print('such kind of bank not exist')        
    



















# courses = [
# {
#     'name':'akademka',
#     'address':'aravanski',   
# }, 
# {
#     'name':'advance',
#     'address':'phrunze',

# },
# {
#     'name':'teilor',
#     'address':'vostok',
# } ,  
# ]    
# for h in courses:
#     print(h)


# for course in courses:
#     print(courses)  

