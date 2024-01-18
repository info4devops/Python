s1=input('s1:')
alph=""
numric=""
for x in s1:
  if x.isalpha():
    alph=alph+x
  else:
    numric=numric+x
output=""
i,j=0,0
while i<len(alph) and j<len(numric):
  if i<len(alph):
    output=output+alph[i]
    i=i+1
  if j<len(numric):
    output=output+numric[j]
    j=j+1
print(output)



