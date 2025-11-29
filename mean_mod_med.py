# Create function that takes a list and returns mean/median/mode.

'''
    for mean_mod_med : 1st step -> sort the list. 
            then move toward the fromulae and process.
'''
from statistics import mode ,median

lst=[60,40,70,43,67,89,95,20,90,59,59]
sorted_list=sorted(lst)

# print(sorted_list)


def mean_mod_med():


    mean=int(sum(sorted_list)/len(lst))
    mod=mode(sorted_list)
    med=median(sorted_list)

    return mean ,med , mod

print(f'Original list: {lst}\nSorted list: {sorted_list}\nMean,Median,Mode : {mean_mod_med()}')