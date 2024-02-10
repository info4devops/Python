# Quantifiers: a,a+,a*,a?,a{m} and a{m,n}

import re
count = 0
matcher = re.finditer('a{2,10}','ababababaababa')
for match in matcher:
  count=count+1
  print(match.start(),'...',match.group())
print('The number of occurences:',count)
