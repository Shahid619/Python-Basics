# Simulate ATM withdrawals with conditions.
'''
Docstring for Day4.cash_withdraw-----simple flow
    take card - check expiry  , if Expire : give error.
        if NOt Expire :- take pin , check if Valid or not : if wrong else: repeat for 3 times.
            if : yes -> take input & check balance accordingly
                if balance > input : give withdraw 
                    else: try small amount .
'''

from datetime import date


card={
    'Name':'ATM',
    'Expiry':date(2027,12,1),
    'balance':12000,
    'pin':1122
}

expiry=date.today()



if expiry<card['Expiry']:

 for i in range(0,3):
    pin=int(input("Enter pin: "))
    if pin!=card['pin']:
       print('try again !')
       if i>=2:
          print('your card is blocked!!!')
    
    if pin == card['pin']:
        bal=int(input("Enter amount to withdraw: "))
        if bal<card['balance']:
            print('processing...')
            print(f'after withdraw {bal} , your balance will be :{card["balance"]-bal}')
            break
        else:
            print('your amount is insufficient!')
            break
      
elif expiry>=card['Expiry']:
    print('Error: your card is expire!')