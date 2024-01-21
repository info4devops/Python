# finding factorial of a number by using recursion

def factorial(n):
  if n==0:
    result =1
  else:
    result = n*factorial(n-1)
  return result
n=int(input('Enter a digit to find factorial: '))
print(f'factorial of {n} is equal to: {factorial(n)}')
