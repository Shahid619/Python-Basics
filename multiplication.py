# Build a multiplication table generator.

inp=int(input('which table you want : '))

for i in range (1,11):
    print(f'{inp} x {i} = {inp*i}')
    
