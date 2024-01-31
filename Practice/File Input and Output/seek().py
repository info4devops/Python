# seek(offset,fromwhere): used to move cursor pointer to a specific loaction
#offset ==> represents number of positions
#from where ==> allowed value is 0[default value]

f=open('abc.txt','r')
print(f.seek(3))
print(f.read(3))
print(f.tell())