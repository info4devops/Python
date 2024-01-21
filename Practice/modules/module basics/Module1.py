# __name__ is a built in variable which evaluates to the name of the current module
def f1():
  if __name__ == '__main__':
    print('Module is executing directly as a main program')
  else:
    print('Module is executing indirectly because of import statement')

import Vmath

f1() # Module is executing directly as a main program

