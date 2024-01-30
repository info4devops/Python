# Find a factorial of a number using recurssion
# recurssion: It is a process in which a function calls itself direcetly or in directly

n=int(input('n='))
def fact(n):
  if n==0:
    result = 1
  else:
    result = n*fact(n-1)
  return result
print(f'factorial of {n} is:{fact(n)}')