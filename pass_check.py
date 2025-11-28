# Create a password strength checker (length + digit + uppercase).

inp=input('Enter your password: ')

cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=0
small='abcdefghijklmnopqrstuvwxyz'
s=0
num  = '1235467890'
n=0
special= '!@#$%^&*_'
sp=0


for i in inp:
    for cp in cap:
      if i==cp:
         c+=1
    for sm in small:
       if i==sm:
          s+=1
    for nm in num:
       if i==nm:
          n+=1
    for spe in special:
       if i==spe:
          sp+=1

if c and s and n and sp >0:
   print('password is strong.')
else: 
   print('password is weak.')
