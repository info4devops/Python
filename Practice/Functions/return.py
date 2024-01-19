# Function with return statement

def f1():
  print('Hello')

#f1() # Hello
print(f1()) 

# Function with multiple return values
print('::::::Function-2::::::::::')
def cal(a,b):
  sum = a+b
  sub = a-b
  return sum,sub
x,y = cal(100,50)
print('The Sum:',x)
print('The Subtraction:',y)

