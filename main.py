class Engine:
  def useEngine(self):
    print('Engine Specific Functionalities')

class Car:
  def __init__(self):
    self.Engine=Engine
  def useCar(self):
    print('Car required Engine related functionalities')
    self.Engine.useEngine()
    

c=Car()
c.useCar()
Engine=Engine()
Engine.useEngine()