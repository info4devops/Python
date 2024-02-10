# Mobile number check using fullmacth()

import re
mobile_number=input('Enter Mobile Number to Validate: ')
pattern = '[6-9][0-9]{9}'
m=re.fullmatch(pattern,mobile_number)
if m!=None:
  print('Valid 10-digits Number')
else:
  print('Invalid 10-digits Number')