# Some methods of string

#1.count(substring,start,end) : returns number of occurences of substring in the given string
string=input("Enter some string:")
sub_string=input('Enter substring:')

# Finding number of occurence using count()
no_of_Occurence=string.count(sub_string)
print(f"The substring '{sub_string}' Total number of Occurrences in entire string is:{no_of_Occurence}")

# including start and end index as well
print('\nIncluding start and end index as well')
start=int(input('Enter start index:'))
end=int(input('Enter end index:'))
no_of_Occurence=string.count(sub_string,start,end)
print(f"The substring '{sub_string}' Total number of Occurrences between {start} and {end}:{no_of_Occurence}")

