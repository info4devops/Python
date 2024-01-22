# WAP to generate a random OTP using randint() function
from random import*
print('::::::Method-1::::::')
OTP=randint(000000,999999)
print(f'OTP:{OTP}')
print('\n::::::Method-2::::::')
for i in range(6):
  print(randint(0,9),end='')

print('\n::::::Method-3::::::')
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")


