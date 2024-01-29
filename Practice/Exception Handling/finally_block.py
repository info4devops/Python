# Speciality of finally block: it will always execute irrespective of exception raised or not raised and handled or not handled.

try:
  print('Try Block Execution')
  print(10/0) # Zero Division Error


# Exception Not handled: No except block fo Zero Division Error
except NameError:
  print('Exection Block Execution')

finally:
  print('Finally Block Execution')


  
  

  