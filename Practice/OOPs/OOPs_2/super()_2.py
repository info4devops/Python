class Person:
  def __init__(self,name,eno):
    self.name=name
    self.eno=eno
  def eatnDrink(self):
    print('Eat Biryani and Drink Beer')

class Employee(Person):
  def __init__(self,name,eno,age,esal):
    super().__init__(name,eno)
    self.age=age
    self.esal=esal
  def work(self):
    print('Work:Coding Python')
  
  def empInfo(self):
    print('Name:',self.name)
    print('Emp Number:',self.eno)
    print('Salary:',self.esal)
    print('Age:',self.age)


  
e=Employee('Virat',123,34,10000)
e.empInfo()
e.work()
e.eatnDrink()