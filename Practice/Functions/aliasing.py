# In Python everything is an object

# Function aliasing

# Declaration of function
def wish(name):
  print('Hello',name,'Good Morning')
  
# Function Aliasing
greeting = wish

print(id(greeting))
print(id(wish))
if id(greeting) == id(wish):
  print(f'IDs are same')
else:
  print(f'IDs are not same')

# Function calling
wish('virat')
greeting('rohit')

# Deleting one funtion name but still we can call function with 2nd name

del wish

greeting('Sachin')

  