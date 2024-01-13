# finding biggest number using if-else
a=int(input('a='))
b=int(input('b='))
if a>b:
    print(f'{a} is bigger number')
else:
    print(f'{b} is bigger number')
print('\n')

# finding biggest number using maximum function
a=int(input('a='))
b=int(input('b='))
max_number= max(a,b)
print(f'{max_number} is biggest number')
print()

# finding biggest number using ternary function
a=int(input('a='))
b=int(input('b='))
max_number= a if a>b else b
print(f'{max_number} is biggest number')
print()

# finding biggest number using list comprehension function
a=int(input('a='))
b=int(input('b='))
max_number= [a if a>b else b]
print(f'{max_number} is biggest number')
print()
