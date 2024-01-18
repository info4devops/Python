# Write a Python program that accepts a filename from the user and prints the extension of the file.

file_name=input('Enter file name: ')
extension = file_name.split('.')
print(f'File extension is:{extension[-1]}')
