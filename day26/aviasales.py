class Avia:
    def __init__(self):
        self.tickets = {
            'Moscow':{
                'date':'20.01.2021',
                'price':27_000
            },
            'Dubai':{
                'date':'01.06.2021',
                'price':45_000
            }
        
        }

    def get_biletter(self,kuda):
        if kuda in self.tickets:
            print(
                kuda,
                'date: ',
                self.tickets[kuda]['date'],
                '\n',
                'price: ',
                self.tickets[kuda]['price'],
                '\n'
            )
            pass
        else:
            print('билеты на:' ,kuda,'not')   

samturAvia = Avia()
mesto = input('where do you want to go ? : ')
samturAvia.get_biletter(mesto)
samturAvia.get_biletter(mesto)

