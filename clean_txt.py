# Clean a dirty text: remove HTML-tags, remove extra spaces

print('this is regex cleaning of text')

'''
    input text 
        check for HTML tags | xtra space 
            if exit remove then return | else : return.
'''
import re

txt='<p>  This is <b>  an example  </b> of  <a href=" dirty  text ">dirty text</a>   with   HTML tags and extra   spaces.  </p>'

def cleaning(text):
    text=re.sub(r'<[^>]*>',"",text)
    text=re.sub(r'\s+'," ",text)
    text=text.lower().strip()
    return text

cleaned_text=cleaning(txt)
print(f"\n Original text : {txt}\n\n Cleaned text : {cleaned_text}\n")