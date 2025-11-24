print('count_in file is a int counting code : from a mixed list.')

'''
    take list as input.
    looping .with condition : if int count+1 else move on .
    then return count as frequency of integer with-in list.
'''
def count_in(lst):

# print(lst)
    count=0
    for idx in lst:
        if isinstance(idx,int):
            count+=1
    print(f" freq of integers from a list: {lst} is : {count} ")
   

lst=[23.4, 12, 'a','r','5', 56, 89, 4300.0, 450000]
count_in(lst)