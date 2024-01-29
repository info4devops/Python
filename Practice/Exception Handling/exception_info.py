# Program to print exception information

try:
  print(10/0)
except ZeroDivisionError as msg:
  print(msg)