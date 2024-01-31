# tell(): used to return current cursor position(file pointer)

f= open('abc.txt','r')
print('current cursor position:',f.tell())

print(f.read(3)) # reading 3 characters
print('current cursor position:',f.tell())

print(f.read()) # reading all remaing characters
print('current cursor position:',f.tell())

