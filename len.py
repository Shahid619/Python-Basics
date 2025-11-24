print( 'this is a length Function.')
'''
    takes input 
    loop through input and count each char.
    return count as a length of the input.
'''

def len(inp):
    count=0
    for char in inp:
        count+=1
    print(f'lenght of -> { inp} is : {count} ')
 
inp='shahid is good boy'
len(inp)