s='Python'
l=len(s)
evens=[]
odds=[]
i=0
while i<l:
  if i%2==0:
    evens.append(s[i])
  else:
    odds.append(s[i])
  i=i+1
print()
output1='+'.join(evens)  
output2='-'.join(odds)
print(output1)  
print(output2)  





