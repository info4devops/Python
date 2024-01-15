# To find out the sum of natural numbers

n= int(input('Enter Range Value: '))
sum =0
i = 1
while i<=n:
  sum = sum+i
  i=i+1
print(f'The Sum of 1st {n} numbers is:{sum}')
