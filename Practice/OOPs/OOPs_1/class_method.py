# Program about clas method

class Animal:
  legs =4
  @classmethod
  def walk(cls,name):
    # accessing using cls variable within the class i.e cls.legs
    print('{} walks with {} legs'.format(name,cls.legs))
    
# accessing using class name from outside of the class
Animal.walk('Dog')
Animal.walk('Cat')