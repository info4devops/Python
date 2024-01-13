# Generating prime number less than or equal to given numbers
n=int(input('Enter Some Random numbers:'))
n1=2
while n1<=n:
    # Code to check whether n1 is prime or not
    is_prime=True
    for i in range(2,n1):
        if n1%2==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1,end=' ')
    n1=n1+1

