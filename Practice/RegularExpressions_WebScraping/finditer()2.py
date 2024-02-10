# finditer(): Returns an iterator object which yeilds match object for every match

import re
count =0
matcher=re.finditer('x','a7b @K9z') # replace 'x' with any predefinded character classes i.e \s or \S etc
for match in matcher:
  print(match.start(),'....',match.group())
print('The Number of occurrences:',count)
