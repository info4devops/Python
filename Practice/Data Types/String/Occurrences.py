# write a program to find the number of occurrences of each character present in the given string

s= input('s:')
d={} # empty dict
for x in s:
  if x not in d:
    d[x]=1
  else:
    d[x]=d[x]+1
print(f'd:{d}') # Optput will be dict

# traversing the dict elements

for k,v in d.items():
  print(f'{k} is occurs {v} time in the given string')
  