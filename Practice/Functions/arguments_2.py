# default arguments: Define at the time of function declaration

# Function declaration
def wish(name='Guest'): 
  print('Hello',name,'Good Morning')

# function calling
wish('Python')  # consider positional argument
wish() # consider default name

# Variable length Argument def f(*x): internally represent in the form of tuple
print(':::::::Variable Length Arguments::::::::::::::::')
def f(*x):
  print('The Number of arguments passed:',len(x))
  print('x:',x)
  print('The Type of x:',type(x))
  print()


f()
f(10,20,30,40)

