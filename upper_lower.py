print('This is upper-> <-lower  function:')

"""  1st -> take input string 
     2nd -> loop -> each char
     3rd -> check each char -> replace -> capital letter
     4th -> save the output in a string list
     5th -> print output.
"""

#  Local methodolgy : 
def upper(word):
    upper=""
    for letter in word:
        if letter=='a':
            letter='A'
            upper+=letter
        elif letter=='b':
            letter='B'
            upper+=letter
        elif letter=='c':
            letter='C'
            upper+=letter
        elif letter=='d':
            letter='D'
            upper+=letter
        elif letter=='e':
            letter='E'
            upper+=letter
        elif letter=='f':
            letter='F'
            upper+=letter
        elif letter=='g':
            letter='G'
            upper+=letter
        elif letter=='h':
            letter='H'
            upper+=letter
        elif letter=='i':
            letter='I'
            upper+=letter
        elif letter=='j':
            letter='J'
            upper+=letter
        elif letter=='k':
            letter='K'
            upper+=letter
        elif letter=='l':
            letter='L'
            upper+=letter
        elif letter=='m':
            letter='M'
            upper+=letter
        elif letter=='n':
            letter='N'
            upper+=letter
        elif letter=='o':
            letter='O'
            upper+=letter
        elif letter=='p':
            letter='P'
            upper+=letter
        elif letter=='q':
            letter='Q'
            upper+=letter
        elif letter=='r':
            letter='R'
            upper+=letter
        elif letter=='s':
            letter='S'
            upper+=letter
        elif letter=='t':
            letter='T'
            upper+=letter
        elif letter=='u':
            letter='U'
            upper+=letter
        elif letter=='v':
            letter='V'
            upper+=letter
        elif letter=='w':
            letter='W'
            upper+=letter
        elif letter=='x':
            letter='X'
            upper+=letter
        elif letter=='y':
            letter='Y'
            upper+=letter
        elif letter=='z':
            letter='Z'
            upper+=letter
        else:
            letter=letter
            upper+=letter
        

    return upper
# print(upper('shahid'))




# ------------------
# proper way 

def upper_proper(inp):
    upper=""
    for char in inp:
        if 'a' <= char <= 'z':
            char=chr(ord(char)-32)
            upper+=char
        else:
            upper+=char
    return upper

# print(upper_proper('shahid'))

# ------------------------------------------ This was the methods to  create upper() function.


inp='Shahid is THE best person in 1122'
print(f"\ninput : {inp}\n")
print(f" upper-casing :using manual method : {upper(inp)}  \n upper-casing using ascii : {upper_proper(inp)}")




# ----------------------lower casing.
def lower(inp):
    lower=""
    for char in inp:
        if 'A'<=char <='Z':
            char=chr(ord(char)+32)
            lower+=char
        else:
            lower+=char
    return lower

print(f"lower-casing input: {lower(inp)}")