# fullmatch(): To macth a pattern to all the target string. i.e., complete string should matched according to given pattren

# Macth available: Returns Match object else returns None

import re
target = input('Enter Target String: ') #abcpqrcba
pattern = input('Enter Pattern to check: ') #abc
m = re.fullmatch(pattern,target)
if m!=None:
  print('Full Pattern Matched')
else:
  print('Full Pattren Matched with Target')
