def wish(name,msg):
  print('Hello',name,msg)
  
wish('Python','Good Morning') # Positional arguments
wish(name='Java',msg='How Are You') # Keyword arguments
wish(msg='How Are You',name='C++') # Keyword arguments

# wish(msg='How Are You','C++') # Error: Positional argument followed by Keyword arguments

wish('HTML',msg='How Are You')
 