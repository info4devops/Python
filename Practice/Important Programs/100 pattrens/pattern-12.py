n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,i):
        print(i-j,end='')
    for k in range(0,i):
        print(k,end='')
    print()
print('\n')

#case-2
n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i-1,0,-1):
        print(k,end='')
    print()
print('\n')

#case-3
n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    for k in range(1,i+1):
        print(k,end='')
    print()
print('\n')