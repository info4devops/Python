s= input('s:')
l=[]
for x in s:
  if x not in l:
    l.append(x)
print(l)
output = ''.join(sorted(l))
#result=''.join(sorted(output))
print(output)


