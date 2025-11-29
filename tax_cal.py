# Make a reusable function for tax calculation.

def tax_cal():
    initial_amount=float(input('Enter salary: '))
    tax=float(input('Enter tax in number: '))
    tax_centage=tax/100
    Total_tax=initial_amount*(tax_centage)
    Net_amount=initial_amount-Total_tax

    print(f'tax percentage : {tax} % .\n Total Tax: {Total_tax} .\nNet-amount: {Net_amount}')
    return Net_amount

tax_cal()
    
