# Bitwise Operators
a=input('Enter a value:')
b=input('Enter b value:')
#type casting
a=int(a)
b=int(b)
print('binary value of a:',bin(a))
print('binary value of a:',bin(b))
bitwise_AND = a&b
print('value of a&b:',bitwise_AND)
print('Binary of a&b:',bin(bitwise_AND))
print()

bitwise_OR = a|b
print('value of a|b:',bitwise_OR)
print('Binary of a|b:',bin(bitwise_OR))
print()

bitwise_XOR=a^b
print('value of a^b:',bitwise_XOR)
print('Binary of a^b:',bin(bitwise_OR))
print()

#Bitwise complement operator
x=int(input('Enter any number:'))
print(f'Complement of {x}, i.e., ~{x} is:{~x}')
#Bitwise Shift operator
n=int(input('Enter no.of digits to shift,n:'))
LeftShift=x<<n
print(f'left shift by {n} digits of {x} is :{LeftShift}')
print('Binary Value of left shift:',bin(LeftShift))
RightShift=x>>n
print(f'Right shift by {n} digits of {x} is :{x>>n}')
print('Binary Value of Right shift:',bin(RightShift))



