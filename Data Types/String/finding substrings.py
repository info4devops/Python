# Finding substrings [rfind(),rindex(), find() and index()]
# returns 1st index if found else return -1

string=input('Enter any string:')
sub_sting=input('Enter substring:')

# Finding substring in forward direction
print('\nSearching for substring in Forward Direction')

result=string.find(sub_sting)
if result != -1:
    print(f"The substring '{sub_sting}' is FOUND at index:'{result} from forward direction'")
else:
    print(f"The substring '{sub_sting}' is NOT FOUND in '{string}'")

# Finding substring in forward direction
print('\nSearching for substring in Backward Direction')
result=string.rfind(sub_sting)
if result != -1:
    print(f"The substring '{sub_sting}' is FOUND at index:'{result}' in Backward Direction")
else:
    print(f"The substring '{sub_sting}' is NOT FOUND in '{string}'")
