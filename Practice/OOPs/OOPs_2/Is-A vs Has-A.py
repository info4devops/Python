# Is-A: Extending Exisiting functionality with some more
# Has-A: Just to us existing functionality without extending

# Employee & Person HAS-A relation (Inheritance)
# Employee & Car IS-A relation (Composition)

class Car:
  def __init__(self,name,model,color):
    self.name=name
    self.model=model
    self.color=color
  def getcarInfo(self):
    print('\t Car Name:{}\n\t Model:{} \n\t Color:{}'.format(self.name,self.model,self.color))
  
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def eatnDrink(self):
    print('Eat Biryani and Drint Beer')

class Employee(Person):
  def __init__(self,name,age,eno,esal,car):
    super().__init__(name,age)
    self.eno=eno
    self.esal=esal
    self.car=car
    
  def work(self):
    print('Work:Coding Python')
  
  def empInfo(self):
    print('Employee Name:',self.name)
    print('Employee Number:',self.eno)
    print('Employee Age:',self.age)
    print('Employee Salary:',self.esal)
    print('Car Info')
    self.car.getcarInfo()

c=Car('BMW','2.5V','Black')
e=Employee('Rohit',34,12345,90000,c)
e.empInfo()
e.eatnDrink()
e.work()