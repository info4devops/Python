# Nested function-1

def outer():
  print('Outer function started')
  def inner():
    print('Inner function started')
  print('Outer function calling inner function')
  inner()

outer()
#inner() # NameError: name 'inner' is not defined. Did you mean: 'iter'?

# Nested function-2
print('::::::Nested Function-2:::::::::')
def outer():
  print('Outer function started')
  def inner():
    print('Inner function started')
  print('Outer function calling inner function')
  return inner
f1=outer()
f1() # Inner function started

# Difference between
#f1=outer : means function aliasing
# f1=outer() means--> calling outer function,which return inner function for the we are providing another name

