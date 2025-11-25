print('this is replace () file.')

'''
   inp1 : replaced by inp2 , inp2: take place of  inp1
   loop through lst|string and search for inp2.
   inp2 find : replace with inp1 else : not found error.
'''

import re


def replace(being_replace, to_replace_with):
    text=re.sub(being_replace,to_replace_with,text)
    return text

text ='The substring to be to replaced by to.'
print(text.replace('to','Shahid',))