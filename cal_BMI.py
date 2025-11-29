# Create a function to calculate BMI.
#  BMI :- Body Mass Index ( weight (KG)/Height (m^2))

def BMI():
    weight=float(input('Enter  weight in KG :'))
    height=float(input('Enter Height in meter (m) :'))

    BMI=weight/(height*height)
    print('Your BMI is :',BMI)
    if BMI < 18:
        print('you are underweight')
    elif 18<BMI<=25:
        print('your BMI is Normal')
    elif 30>BMI>25:
        print('you are overweight')
    elif BMI>30:
        print('your BMI is obesse!!!')
    else:
        print('Please enter valid input.')
    
BMI()
    