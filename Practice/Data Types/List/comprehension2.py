# write a program to differentiate vowels and consonants from a given string

string= input('Enter any string:')
vowels =['a','e','i','o','u']
consonants=[]
find=[]

print('::::::::::Using for loop::::::::')
# To find vowels
for x in string:
  if x in vowels:
    if x not in consonants:
      find.append(x)
      
# To find consonants
  else:
    if x not in vowels:
      if x not in consonants:
        consonants.append(x)
        
print(f'Vowels present in string are:{find}')
print(f'Consonants present in string are:{consonants}')
print()

print('::::::::::Using List Comprehension::::::::')
l_vowels=[x for x in string if x in vowels]
print(f'Vowels present in string are:{l_vowels}')
l_consonants=[x for x in string if x not in vowels]
print(f'Consonants present in string are:{l_consonants}')


      