n=int(input("Enter any number:"))
if n%2==0:
    print("{} is an even number".format(n))
else:
    print("{} is an odd number".format(n))

# And something that looks slightly more complex (but is just a more complicated conditional):
num=int(input('Enter any number:'))
check=int(input("Enter a number to divide by:"))
if num%4==0:
    print("{} is divisible by 4".format(num))
elif num%2==0:
    print("{} is divisible by 2 and its an even number".format(num))
else:
    print("{} is an odd number".format(num))
if num%check==0:
    print('{} is evenly divisible by {}'.format(num,check))
else:
    print('{} is not evenly divisible by {}'.format(num,check))