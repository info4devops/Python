# Function to find factorial of a number
def fact(n):
  result=1
  while n>=1:
    result=result*n
    n=n-1
  return result
for i in range(1,6):
  print('The Factorial of {} is:{}'.format(i,fact(i)))


# Function to find factorial of a given number
print('::::::::::Finding Factorial:::::::::::')

def fact(n):
  result=1
  while n>=1:
    result=result*n
    n=n-1
  print(result)

n=int(input('Enter number to find factorial:'))
fact(n)

  