print('counting vowel')

text ='Barking dogs seldom bites'

vowels = 'aeiouAEIOU'
count=0
for word in text:
    for v in vowels:
        if word == v:
            count+=1
print(f'Sentence : {text} \n vowels in text :{count}')
