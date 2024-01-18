# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

first_name = input('Enter first name:')
last_name = input('Enter last name:')
print("Hello",last_name + " "+first_name) # print normally

print("Hello",last_name[::-1]+ " "+first_name[::-1]) # reverse the characters

