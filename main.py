name=input('Enter name: ')
f=open(f"D:\Python classes\\{name.lower()}.txt","w")
m1=int(input('Enter marks:'))
f.write(f'Student name:{name}\n')
f.write(f'Python:{m1}\n')
print('date written successfully')
date = f.read()
print(data)
f.close()