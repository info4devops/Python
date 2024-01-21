# reduce(function,sequence): This function present in 'functools' module
#importing reduce() from 'functool' module
from functools import* # from functool inport reduce

# Initialising list 
l=[10,20,30,40]
print(f'list l:{l}')

# Printing sum of all elements present in list
print(':::::::::Sum Of All Elements is list')
sum = reduce(lambda x,y:x+y,l)
print(f'The Sum of all elements in list:{sum}')

# Printing sum of all elements present in list
print(':::::::::Product Of All Elements is list')
product = reduce(lambda x,y:x*y,l)
print(f'The Product of all elements in list:{product}')
