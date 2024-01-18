# List comprehension
s= 'The Quick Brown Fox Jumps Over the Lazy Dog'
words=s.split() # Split the str into list considering space separator
print(words)

print('Using For Loop')
l=[]
for element in words:
  l.append([element,len(element)])
print(f'l:{l}')
print()

print('Using List comprehension')

l1=[(element,len(element)) for element in words]

l2=[(element.upper(),len(element)) for element in words] # Upper case

print(f'l1:{l1}')
print()
print(f'l2:{l2}')

