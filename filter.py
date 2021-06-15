# Filter
# my_list =[1,4,5,6,9,13,19,21]
# odd = list(filter(lambda x: x%2 !=0,my_list))
# print(odd)

# Map
my_list =[1,2,3,4,5]
square = list(map(lambda x: x**2,my_list))
print(square)

from functools import reduce
# Reduce
my_list =[2,2,2,2,2]
multiplied = reduce(lambda a,b: a*b,my_list)
print(multiplied)