print('regex extraction of : email,phone ,dates')

import re

txt='my name is Shahid khan , email: skk15834@gmail.com, contact: +92 (326) 9670904 '

email=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',txt)
print(f'emails from a text: {email}')


