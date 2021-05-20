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



def translate():
    print('say hello!')


def getfullname(fname,lname):
    return fname + ' ' + lname   


def hello():
    print('hello word')


