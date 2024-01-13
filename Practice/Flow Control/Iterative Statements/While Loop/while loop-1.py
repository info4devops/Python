# While: execute a block of statements repeatedly until a given condition is satisfied.
x=0
while x<=5:
    print('Hello While-Loop')
    x=x+1
print('\n')

# To Print numbers from 1-20 which are divisible by 3 using while loop
print('Numbers divisible by 3 from 1-20')
x=1
while x<20:
    if x%3==0:
        print(x,end=' ')
    x=x+1
print('\n')

#To display sum of n numbers using while loop
#sum of n numbers = ([n*(n+1)]/2)
print('Sum of n numbers')
n=int(input('Enter number:'))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(f'The sum:{sum}')
