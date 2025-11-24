print('this is rang() function file.')

'''
  input , loop until size of inp. 
  print each cond. on each phase.
'''
#  -------------------provide return in desc order.
def desc_rnge(inp):
    lst=[]
    while(inp>0):
        lst.append(inp)
        inp-=1
        if inp==0:
            break
    return lst

inp=5
for i in desc_rnge(inp):
    print(5*i)
# for i in range(inp):
#     print(5*i)


# ------------provide return in ascending order.
def ascen_rnge(inp):
    count=0
    lst=[]
    while(count<inp):
        lst.append(count)
        count+=1
        if count==inp:
            break
    return lst

inp=5
for i in ascen_rnge(inp):
    print(5*i)