# create a lambda function to find smallest and largest

a,b = input('Enter 2 values with , seperate:').split(',')
s_small = lambda a,b: a if a<b else b
s_large = lambda a,b: a if a>b else b

print(f'Smallest of {a} and {b} is:'.format(s_small(a,b)))
print(f'Largest of {a} and {b} is:'.format(s_large(a,b)))

