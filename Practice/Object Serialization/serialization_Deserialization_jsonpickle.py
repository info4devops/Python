# Jsonpickle module contain functions which convert any type of object type to json string and wiseversa

# encode(): convert any object to json string
# decode(): convert json to our original object

import json
import jsonpickle

# Creating Employee class
class Employee:
  def __init__(self,eno,ename):
    self.eno=eno
    self.ename=ename
    
# Displya class for printing 
  def display(self):
    print('Number:',self.eno)
    print('Name:',self.ename)

# Creating Employee Object
e=Employee(111,'virat')
print('Type of e:',type(e)) # <class '__main__.Employee'>
print()


#serilization using jsonpickle
json_string=jsonpickle.encode(e)
print('json_string:',json_string)
print()

#serilization to file
with open('emp3.json','w') as f:
  f.write(json_string)

#De-serilization using jsonpickle
print('::::De-serilization using jsonpickle:::::::')
New_Employee=jsonpickle.decode(json_string)
New_Employee.display()
print()

#De-serilization from file
print('::::De-serilization from file:::::::')
with open('emp3.json','r') as f:
  json_string=f.readline()

New_Employee = jsonpickle.decode(json_string)
New_Employee.display()


