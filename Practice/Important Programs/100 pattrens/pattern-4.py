#case-1
n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=' ')
    print()
print('\n')

#case-2
n=int(input('Enter number of rows:'))
for i in range(1,n+1): # column value
    for j in range(1,n+1): # row values
        print(n+1-j,end=' ')
    print()