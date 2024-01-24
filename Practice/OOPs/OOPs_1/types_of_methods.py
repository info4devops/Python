# Python has 3 type of methods

class student:
  college_name = 'IIT Bombay' # Static Variable
  def __init__(self,name):
    self.name=name # Instance variable
    
  #instance method
  def getstudent_info(self):
    print('student name:',self.name)
  
  #class method
  @classmethod # decorator for class method
  def getcollege_info(cls):
    print('college name:',cls.college_name)
    
  # Static method
  @staticmethod # Decorator for static method
  def get_average(a,b,c):
    return (a+b+c)/3
    

s=student('virat') # Creating object

# Calling instance method
print('\n:::::::Instance method::::::::::')
s.getstudent_info()

#Calling class method
print('\n:::::::Class method::::::::::')
student.getcollege_info() # calling by using class name
s.getcollege_info() # Calling by using object reference

#Calling Static method
print('\n:::::::Static method::::::::::')
avg = student.get_average(10,20,30) # calling by using class name and assign a refrence variable

print('Average:',avg)


