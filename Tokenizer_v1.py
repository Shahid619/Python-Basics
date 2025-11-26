# Tokenizer v1 → split on spaces only (manual, don’t use .split())
# print('this is phase 1 of creationg of Tokenizer manually!')

'''
    input text 
        chck for whitespace 
            if : is there -> replace with -> comma.
            else : continue.
'''
import re
def splitt(text):
    text=re.sub(r' ',',',text)   
    return text

text='this is phase 1 of creationg of Tokenizer manually'
# print(splitt(text))

# Now here we used : re.sub .....let's create this sub.  TO know how exactly he is doing this .

text = 'this is shahid khan\'s practices'
strr=[]
for char in text:
    if char==' ':
        char=','
    strr.append(char)

txt=''.join(strr)

print(txt)
