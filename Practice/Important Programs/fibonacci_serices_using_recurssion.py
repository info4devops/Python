# Find fibonacci serices using recurssive function


def fibonacci(n):
  if n <=1:
    return n
  else:
    return (fibonacci(n-2)+fibonacci(n-1))
n_terms=int(input('How many fibonacci series number you want to print?:'))
if n_terms <=0:
  print('Negative number, Please enter correct number')
else:
  print(f'fibonacci serices of {n_terms} is')
for i in range (n_terms):
  print(fibonacci(i),end=' ')