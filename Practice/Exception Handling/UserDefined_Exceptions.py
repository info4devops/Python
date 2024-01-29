# Create a user defined exception

class TooYoungException(Exception):
  def __init__(self,msg):
    self.msg=msg

class TooOldException(Exception):
  def __init__(self,msg):
    self.msg=msg

age=int(input('Enter Your Age:'))
if age>90:
  raise TooOldException('Already Too Old No chance of marrige')
elif age<18:
  raise TooYoungException('Too Young Need to wait for marrige')
else:
  print('You will get marry soon')

