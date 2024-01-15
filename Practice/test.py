n=int(input('Enter range value: '))
sum = 0
for x in range(n+1):
  if (x%2 !=0):
    print(x, end=" ")
    sum = sum+x

print(f'\nThe sum of Odd number present in the range of {n} is:{sum}')
