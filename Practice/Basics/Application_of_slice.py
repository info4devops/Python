string1='abcdefghijklmnopqrstuvwxyz'
string2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('string1: ',string1)
print('string2: ',string2)
print('Length of string1:',len(string1))
print('Length of string2:',len(string2))

output_1=string1[0:5].upper()+string2[8:1:-1].lower()
print('output_1:',output_1)

output_2=string1[0:10]+string2[26:0:-3]
print('output_2:',output_2)

output_3=string1[0:(len(string2)-1)]+string2[(len(string1)-1):0:-1]
print('output_3:',output_3)


