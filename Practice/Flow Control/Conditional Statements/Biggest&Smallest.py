# Finding Biggest number
print(':::::::::::Case-1:::::::::::')

a=eval(input('Enter value of a:'))
b=eval(input('Enter value of b:'))
if a>b: # use a<b to find smallest
    print(f'Biggest Number is:{a}')
else:
    print(f'Biggest Number is :{b}')
print()

# Finding Smallest number
print(':::::::::::Case-2:::::::::::')

a=eval(input('Enter value of a:'))
b=eval(input('Enter value of b:'))
c=eval(input('Enter value of c:'))

if a<b and a<c: # use a<b to find smallest
    print(f'Smallest Number is:{a}')
elif b<c:
    print(f'Smallest Number is:{b}')
else:
    print(f'Smallest Number is :{c}')
print()
