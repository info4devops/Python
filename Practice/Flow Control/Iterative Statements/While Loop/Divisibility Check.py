# To print Numbers which are divisible by the given number
Limit = int(input('Enter the range value:'))
n = int(input('Enter Divisor value:'))
list_of_divisibles = []
x=1
while x<=Limit:
  if x%n ==0:
    list_of_divisibles.append(x)
  x = x+1
print(f'The List of all divisible number between 0-{Limit} are:{list_of_divisibles}')
print(f'The Total Number of divisible number between 0-{Limit} are:{len(list_of_divisibles)}')

