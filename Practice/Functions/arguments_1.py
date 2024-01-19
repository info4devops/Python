# Positional and keyword arguments: declare at the time of function calling

# Function declaration
def wish(name,msg):
  print('Hello',name,msg)
  
# function calling
wish('Python','Good Morning') # Positional arguments
wish(name='Java',msg='How Are You') # Keyword arguments
wish(msg='How Are You',name='C++') # Keyword arguments

 # Error: Positional argument followed by Keyword arguments
 # wish(msg='How Are You','C++')

wish('HTML',msg='How Are You')
 