# Accessing members of one class from other class
#1. By Composition(Has-A relationship)

class Engine:
  def useEngine(self):
    print('Engine Specific Functionalities')

class Car:
  def __init__(self):
    self.Engine=Engine() # passing Engine class as instance varible inside Car class
  def useCar(self):
    print('Car required Engine related functionalities')
    self.Engine.useEngine() # Calling Engine functionalities using class name
    

c=Car()
c.useCar()
