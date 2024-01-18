# Sorting the characters of the string 1st alphabets and followed by numberic value
# input: ABCD123E4 O/p: ABCDE1234

s1=input('s1:')
alph=""
numric=""
for x in s1:
  if x.isalpha():
    alph=alph+x
  else:
    numric=numric+x
output="".join(sorted(alph)+sorted(numric))
print(f'output:{output}')

# Sorting the characters of the string 1st alphabets and  numberic value alternately
# input: ABCD123E4 O/p: A1B2C3D4E
output1=""
i,j=0,0
while i<len(alph) or j<len(numric):
  if i<len(alph):
    output1=output1+alph[i]
    i=i+1
  if j<len(numric):
    output1=output1+numric[j]
    j=j+1
print(f'output1:{output1}')




