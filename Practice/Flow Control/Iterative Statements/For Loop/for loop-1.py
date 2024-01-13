#for: to execute some action for every element present in some sequence
#printing each character present in sequence
s=input('Enter any String:')
for x in s:
    print(x,end=' ')
print('\n')

#printing each character present in sequence index wise
s=input('Enter any String:')
i=0
for x in s:
    print(f'The Character present at {i} index is:{x} ')
    i=i+1

