# To print 'python' 2 times
for x in range(2):
    print('Python')
print('\n')

#To display odd number from 0-10
for x in range(11):
    if (x%2 !=0): # use (x%2 ==0) to print even numbers
        print(x,end=' ')
print('\n')

# To Print sum of number present inside list
list=eval(input('Enter list: '))
sum=0
for x in list:
    sum=sum+x
print(f'The Sum:{sum}')


