n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1, i+1):
        print(j,end=' ')
    print()
for k in range(1, n):
    print(' '*k, end='')
    for i in range(1,n+1-k):
        print(i,end=' ')
    print()
print('\n')

#case-2
n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1, i+1):
        print('*',end=' ')
    print()
for k in range(1, n):
    print(' '*k, end='')
    for i in range(1,n+1-k):
        print('*',end=' ')
    print()
print('\n')

