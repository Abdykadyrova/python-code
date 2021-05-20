
    sum = 0
    for a in args:
        sum = sum + a 
    print(sum)    

def sample(*args):
    print(args[0] + args[1] + args[2] + args[3])

sample(4,6,70,80)    

def sample(**kwargs):
    print(kwargs['name'])
    print(kwargs['model'])
    print(kwargs['weight'])
    print(kwargs['god'])
    print(kwargs['price'])
sample(
    name = 'toyota',
    model = 'prius',
    weight = '2400kg',
    god = '2012year',
    price = 'болушу 43300'
)    





























def sample(*args):
    print(args[0] + args[1] + args[2] + args[3])

sample(4, 6, 70, 80)

def sample(**kwargs):
    print(kwargs['name'])
    print(kwargs['model'])
    print(kwargs['weight'])
    print(kwargs['god'])
    print(kwargs['price'])

sample(
    name = 'Toyota', 
    model = 'Prius',
    weight = '2400 кг',
    god = '2012 Жылкы',
    price = 'Болушу 423 000 сом'
)

def my_computer(**kwargs):
    print(kwargs['processor'])
    print(kwargs['ghz'])
    print(kwargs['core'])
    print(kwargs['harddisk'])
    print(kwargs['videocard'])
    print(kwargs['ram'])
    print(kwargs['model'])


my_computer(
    processor = 'Intel Core i7 8700K',
    ghz = '8.6 GHZ',
    core = '36',
    harddisk = '500 TБ',
    videocard = 'GTX 9080 Ti',
    ram = '128 GB',
    model = 'ASUS ROG STRIX 2070',
)
