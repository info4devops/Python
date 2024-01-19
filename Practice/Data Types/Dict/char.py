# Finding character present in string

s=input('Enter any string:')
d={}
for x in s:
  d[x]=d.get(x,0)+1
for k,v in d.items():
  print(f'{k} present {v} times')
  