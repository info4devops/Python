# finditer(): Returns an iterator object which yeilds match object for every match

import re
count =0
matcher=re.finditer('ab','abbabaabaaabab')
for match in matcher:
  print(match.start(),'....',match.end(),'...',match.group())
print('The Number of occurrences:',count)
