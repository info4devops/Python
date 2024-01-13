# Generating first n prime numbers & finding there sum
n=int(input('Enter Some Random numbers:'))
list=[] # empty list
sum=0
count=0
n1=2
while True:
    # Code to check whether n1 is prime or not
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        list.append(n1) # Adding to list
        print(n1) # printing prime number
        count=count+1
    if count==n:
        break
    n1=n1+1

# finding the sum of n prime numbers
print(f'Elements in list:{list}')
for x in list:
    sum=sum+x
print(f'The sum of 1st {n} prime numbers is:{sum} ')



