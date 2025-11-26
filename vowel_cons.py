print('This is code of count frequency of Vowel & Consonent from MultiLingual text')

'''
    input txt , loop through each char.
    if: vowel : v_count+ , elif: consonent : c_count+ ,else :continue
    print : freq: vowel & freq: consonent

'''
# ascii -> to extract consonent out of whole English letter list.
# ------------------------
import string
def Freq(txt):
    v_count=0
    c_count=0
    Vowel='aeiouAEIOU'
    # drive consonent as well . using ascii
    all_letters=string.ascii_letters
    consonent=[char for char in all_letters if char not in Vowel]
    # print(consonent)

    for char in txt:
        for v in Vowel:
            if char==v:
                v_count+=1
        for c in consonent:
            if char ==c:
                c_count+=1

    return c_count,v_count


text='Meri امی (ammi) ne biryani پکائی (pakayi) hai, but the taste is not good.'
print(Freq(text))
    
