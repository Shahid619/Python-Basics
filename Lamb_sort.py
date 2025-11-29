# Write a lambda to sort tuples by second element.
data=[(1,3,5),(2,4,6),(1,'2')]

sorted_data_by_first = sorted(data, key=lambda x: x[0])
print(sorted_data_by_first)