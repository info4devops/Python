# finding smallest number using if-else
a=int(input('a='))
b=int(input('b='))
if a<b:
    print(f'{a} is smallest number')
else:
    print(f'{b} is smallest number')
print('\n')

# finding smallest number using maximum function
a=int(input('a='))
b=int(input('b='))
min_number= min(a,b)
print(f'{min_number} is smallest number')
print()

# finding smallest number using ternary function
a=int(input('a='))
b=int(input('b='))
min_number= a if a<b else b
print(f'{min_number} is smallest number')
print()

# finding smallest number using list comprehension function
a=int(input('a='))
b=int(input('b='))
min_number= [a if a<b else b]
print(f'{min_number} is smallest number')
print()
