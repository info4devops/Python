# Function to find factorial of a number
def fact(n):
  result=1
  while n>=1:
    result=result*n
    n=n-1
  print(result)

n=int(input('Enter number to find factorial:'))
fact(n)

  