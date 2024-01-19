# WAP to Enter student name and percentage of marks in dictionary and display information on the screen

d={}
n=int(input('Enter No.of Students:'))
i=len(d)

while i<n:
  name=input('Enter Name:')
  marks=input('Enter Student Marks:')
  d[name]=marks
  print('--Student Record Saved Successfullt--')
  i=i+1
print('\n All Records saved successfully')
print('\nName \t\tMarks')
print('#'*20)
for x in d:
  print('{}\t\t{}'.format(x,d[x]))
print('#'*20)
print(n)
print(i)