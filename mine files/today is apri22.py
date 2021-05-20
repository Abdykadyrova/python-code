#print('online shop ')
# laptop MAKK
# aliexpress visa and paypal
# mastercard and elcard ne prinimaut  
predatorsena = 3500
balance = 3000
len = 16
print('chtoby kupit aser predtor 3500$:')
sposob = (input('write payment method:')).lower()
if sposob == 'mastercard':
    print('sorry we didnt youth elcard')
elif sposob == 'elcard':
   
    print('sorry we didnt youth elcard') 
     
    summa = int(input('введите сумму:'))
    
    if summa<balance:
     print('у вас недостаточно сретство')
else:
    print('такой вид карты не поддерживается')      

