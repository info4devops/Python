# Demo about self variable

class Test:
  def __init__(self):
    print('Address of object referring by self:',id(self))
t=Test()
print('Address of object referring by t:',id(t))

