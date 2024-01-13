# program to check prime number or not
n=int(input('Enter Some Random Number: '))
if n<=1:
    print(f'Enter number:{n}, is not a prime number')
else:
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime == True:
        print(f'Entered Number :{n}, is a prime number')
    else:
        print(f'Entered Number:{n}, is not a prime number')

