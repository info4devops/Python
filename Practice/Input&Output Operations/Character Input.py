#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
name=input("Enter Your name:")
age=int(input("Enter Your age:"))
temp=2023-age+100
print('{} Will turn to 100 years old by {}'.format(name,str(temp)))
