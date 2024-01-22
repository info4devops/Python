# Demo for class and reference varible

class student:
  '''Developed by vamsi for class-demo'''
  def __init__(self): # Constructor
    self.name='Virat'
    self.rollnumber=18
    self.marks=90
  
  def talk(self):
    print('Hello,I am:',self.name)
    print('My Roll number is:',self.rollnumber)
    print('My Marks are:',self.marks)

# Creating reference varibale/object for the class student
s=student()

print('--------Version:1----------')
# Calling class method by using reference variable of a class
print(s.name)
print(s.rollnumber)
print(s.marks)

print('--------Version:2----------')
# Calling class functiom by using reference variable of a class
s.talk()

