print('this is a calculator file')

'''
    take input 1 and 2 ,then
    give option +,-,/,*,%
    then based on option output.
'''



def addition(inp1 ,inp2):
    print( inp1 + inp2)

def subtract ( inp1,inp2):
    print (inp1 - inp2)

def multiply ( inp1 , inp2):
    print( inp1*inp2)

def deivide (inp1 , inp2):
     print(inp1 / inp2)

def percentage(obtained,total):
    print ((obtained/total)*100)

# --------------------------

inp1=int(input('enter 1st value: '))
inp2=int(input('enter 2nd value: '))

choice =int(input('select operation: 1-add , 2-subtract , 3-multiply , 4-divide, 5-percentage :'))

if choice==1:
    addition(inp1,inp2)
elif choice ==2:
    subtract(inp1 , inp2)
elif choice==3:
    multiply(inp1 ,inp2)
elif choice==4:
    deivide(inp1,inp2)
elif choice==5:
    percentage(inp1,inp2)
else :
    print('not valid , please retry')
