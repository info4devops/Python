# function or method, if return statement encounters then the function or method execution will be stopper and return the control to the caller
# if function/method having multiple return statment then finally block return statement will be executed.


def f1():
  try:
    print('Try Block')
    return 111
    
  except:
    print('Except Block')
    return 222
  finally:
    print('Finally Block')
    return 333

print(f1())
