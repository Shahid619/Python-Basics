print('this is a find() function file.')

'''
    take whole text , sub_string to find.
    then if : find give index else: not found.
    using regex it would be easy.
'''

import re

def find_substr(sub_str,text):
# sub_string='substring'
    indx=re.search(sub_str,text)
    if indx:
        print(indx)
    else: 
        print('not found!')

txt='this is the substring finding from string code . which address how to find substring from string'
find_substr('is',txt)
