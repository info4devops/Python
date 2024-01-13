#case-1
n=int(input('Enter number of rows:'))
for i in range(1,n+1): # column value
    for j in range(1,n+1): # row values
        print(f'j:{j}',end=' ')
        print(f'i:{i}',end=' ')
    print()

#case-2
n=int(input('Enter number of rows:'))
for i in range(1,n+1): # column value
    for j in range(1,n+1): # row values
        print(f'i:{i}',end=' ')
        print(f'j:{j}',end=' ')
    print()