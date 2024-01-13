# if statements: certain condition is true
print('::::::::::Case-1::::::::::')

name=input('Enter Name:')
if name=='Python': # condition
    print('Python Programming Language')
print('Easy to learn')
print()

# if-else
print('::::::::::Case-2::::::::::')
name=input('Enter Name:')
if name=='Python': # condition
    print('Hello Python,Good Morning')
else:
    print('Hello Guest,Good Morning')
print('How are you')
print()
# if-elif-else
print('::::::::::Case-3::::::::::')
brand=input('Enter Brand name:')
if brand=='KF':
    print(f'{brand} too lite')
elif brand=='KO':
    print(f'{brand} is Too hard')
elif brand=='RC':
    print(f'{brand} Buy One Get One')
else:
    print('None')
    
