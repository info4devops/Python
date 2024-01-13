# Membership operator[in & not in] for string
s='PYTHON'
print(f'is "H" is a member of "{s}"?:{"H" in s}')
print(f'is "X" is a member of "{s}"?:{"X" in s}')
print(f'is "P" is a member of "{s}"?:{"P"  not in s}')
print(f'is "Z" is a member of "{s}"?:{"Z"  in s}')
print('\n')

# Taking string and substring from user and check whether its member or not
string=input("Enter any string:")
sub_string=input("Enter any sub string:")
if sub_string in string:
    print(f"'{sub_string}' is A MEMBER of '{string}'")
else:
    print(f"'{sub_string}' is NOT A MEMBER of '{string}'")

