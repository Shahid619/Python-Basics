# Build a function to clean text (lower, remove punctuation).
import re
def CLeaning(inp):

    inp=re.sub(r'\s+'," ",inp)
    inp=re.sub(r'<[^>]+>','',inp)

    return inp.lower().strip()

text='This  is <a>Shahid\'s coding Tut<\a> and    WE are GOIng to <h1>COpy Paste IT<\h> .  '
print(f"\nyour cleaned text ::  {CLeaning(text)}")
