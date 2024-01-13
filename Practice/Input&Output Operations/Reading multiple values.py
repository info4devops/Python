# Reading multiple values from keyboard in single line and print their sum
a,b=[int(x) for x in input('Enter 2 values, separated with space:').split()] # separated with space
print('The value of a:',a)
print('The value of b:',b)
print('The sum of 2 numbers:',a+b)

p,q=[int(x) for x in input('Enter 2 values,separated with comma:').split(',')] # separated with ,
print('The value of p:',p)
print('The value of q:',q)
print('The sum of 2 numbers:',p+q)

# Reading multiple values from keyboard in single line and print their product
p,q,r=[float(x) for x in input('Enter 3 float values,separated with comma:').split(',')] # separated with ,
print('The product 3 numbers:',p*q*r)


