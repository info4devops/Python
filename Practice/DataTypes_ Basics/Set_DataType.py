# creating set object
#s={} # Empty dict not set
s=set() # empty set
print('Type of s:',type(s))

# Creating set with some elements
s={10,20.20,'Java',(11+22j)}
print('Original set, s:',s)
print()

#Indexing & slicing: Not applicable

# Adding and removing elements
s.add(111)
s.add(222)
s.add('HTML')
print('After adding, s:',s)
s.remove((11+22j))
s.remove(20.2)
print('After removing, s:',s)



