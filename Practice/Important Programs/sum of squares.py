# Finding sum of squares for n natural number
# taking input from user

n=int(input('Enter any number:'))
sum=0
# iterating each number in range of n
for x in range(1,n+1):
    # finding square for each number
    squares=x**2
    sum=sum+squares
print(f'Sum of squares of first {n} natural numbers is:{sum}')

