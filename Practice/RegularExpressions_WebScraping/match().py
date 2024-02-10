# match(): To check the given pattern at the begining of the string or not
# Macth available: Returns Match object else returns None

import re
target = input('Enter Target String: ') #abcpqrcba
pattern = input('Enter Pattern to check: ') #abc
m = re.match(pattern,target)
if m!=None:
  print(f'Target String starts with:{pattern}')
  print(f'Start Index:{m.start} and End Index:{m.end()}')
else:
  print(f'Target String not starts with:{pattern}')
