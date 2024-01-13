# Finding factorial of number
# get the number from user
n=int(input('Enter any number: '))

# check if the number is negative
if n<0:
    print(f'{n} is negative number, Factorial is not defined for negative number')
else:
    factorial=1
    # calculate the factorial value
    for i in range(1,n+1):
        factorial=factorial*i
print(f'factorial of {n} is {factorial}')

