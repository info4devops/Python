# Demo of local and global variables

a=10 # global
def f1():
  a=777 # local
  print(f'f1_local:{2}')
  # Accessing global variable from function
  print(f'Global from f1 is:{globals()["a"]}') # globals.get('a)

f1() # prints function print statement
print(a) # prints global variable value
