#Program to perform pickling and unpickling of multiple employee object

# emp.py is responsible to create an employee  object from Employee class
# sender.py is responsible to serialize an employee object to file
# receiver.py is responsible to deserialize employee object from file

# Creating Employee Class
class Employee:
  def __init__(self,eno,ename,esal,eaddr):
    self.eno=eno
    self.ename=ename
    self.esal=esal
    self.eaddr=eaddr

# Creating display class to print employee details
  def display(self):
    print('Employee Number:',self.eno)
    print('Employee Name:',self.ename)
    print('Employee Salary:',self.esal)
    print('Employee Address:',self.eaddr)