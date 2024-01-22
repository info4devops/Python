#WAP to create a student class and create am object to it. Call the method to display student details.

# Demo for class and reference varible

class student:
  '''Developed by vamsi for class-demo'''
  def __init__(self,name,rollno,marks): # Constructor
    self.name=name
    self.rollno=rollno
    self.marks=marks
  
  def talk(self):
    print('Hello,I am:',self.name)
    print('My Roll number is:',self.rollno)
    print('My Marks are:',self.marks)

# Creating reference varibale/object for the class student
s1=student('Rohit',45,34)
s2=student('Virat',18,52)

print('--------Version:1----------')
# Calling class method by using reference variable of a class
print(s1.name)
print(s1.rollno)
print(s1.marks)

print('--------Version:2----------')
# Calling class functiom by using reference variable of a class
s1.talk()
s2.talk()



