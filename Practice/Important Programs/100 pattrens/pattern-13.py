n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(i-1),end='')
    for j in range(0, n+1-i):
        print(n+1-i, end='')
    for k in range(1, n+1-i):
        print(n+1-i, end='')
    print()
print('\n')

#case-2
n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(i-1),end='')
    for j in range(0, n+1-i):
        print(2*n+1-2*i, end='')
    for k in range(1, n+1-i):
        print(2*n+1-2*i, end='')
    print()
print('\n')
