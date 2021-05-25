# def my_function(name,number) :
#     print('world',name)
#     print('country')
#     print('great jobs')
#     print(name,'\n')
#     name = name + 'republik'
#     # number = number ** number
#     if number < 0:
#         print('on san')
#     else:
#         number = number ** number

# my_function('kyrgyzstan',5 )    





# def my_function(num):
#     if num < 0:
#         print('on san')
#     else:
#         num = num * num
#         print(num)
# my_function(-9)           



# def divided(num1,num2):
#     if num2 ==0:
#         print('we cant divaid to zero')
#     else:
#         print(num1/num2)
# divided(10,0)        




# print('exmaple: 0776545454')
# phone = input('write your phone number: ')

# if len(phone) > 11 or len(phone) < 9 or phone[0]== '0' :
#     print('it isnt match')
# elif len(phone) == 10:
#     print('number is true')
    

# def chek_phonnumber(nomer):
#     if len(nomer) == 10 and nomer[0]=='0':
#         print('number is true')

#     else:
#         print('example: 0987654332')

# phone = input('write phone number: ')        
# chek_phonnumber(phone)


# r = 7977
# def myprint(san):
#     print(san * r )

#     print(r)
#     print(r)
# myprint(6456)    


# def about_me(name,last_name,age):
#     print(f'\my name is,{name}, and my{last_name},also i am {age}. ')
# about_me ()   












operators = {
    'megacom': [
        '0558',
        '0551',
        '0555',
        '0557',
        '0996',
        '0550',
    ],
    'beeline': [
        '0770',
        '0777'
    ],
    'o': [
        '0700',
        '0999'
    ],
    'Gorod':[
        '03222',
        '03231',
        '03200',
        '03230',
        '03211'
    ],
}
def check_phone_number(nomer):
    if len(nomer) == 10 and nomer[0] == '0':
        print('Номер телефона правильный')
        code = nomer[0:4]
        if code in operators['o']:
            print('your operator is O!')
        elif code in operators['beeline']:
            print('your operator is BEELINE')  
        elif code in operators['megacom']:
            print('your operator is MEGAKOM')
        code = nomer [0 : 5 ]

        if code in operators['Gorod']:
            print('this operator youth gorod')    
    else:
        print('Вы ввели неправильный номер')
phone = input('Введите номер телефона: ')
check_phone_number(phone)

