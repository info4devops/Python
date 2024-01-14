"""This about shift operators  """

n=int(input('Enter any number to perform shift:'))
x= int(input('Number shift by: '))

#left shift
# x<<n is equal to x*[2]^n

l_result = n<<x
print(f'Result of number:{n}, after left shift by:{x} is:{l_result}')

# Right Shift
# x>>n is equal to x/[2]^n

r_result = n>>x
print(f'Result of number:{n}, after right shift by:{x} is:{r_result}')
