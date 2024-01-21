# Program to print fibonacci series

# recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))

n_terms = int(input('Enter any value:'))

# check if the number of terms is valid or not
if n_terms <= 0:
    print('Invalid input, Please enter a positive value')
else:
    print(f'Fibonacci Series of {n_terms} is:')

for i in range(n_terms):
    print(recursive_fibonacci(i), end=' ')
