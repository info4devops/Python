#case-1
n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ') # print value for j
    print('') #print value for i
print('\n')

#case-2
n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    for j in range(i,n+1):
        print('*',end=' ')
    print()
print('\n')