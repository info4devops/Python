# to display all positions of substring in each main string

s=input("Enter any string:")
sub_string=input("Enter any substring:")
n=len(s)
position=0
count=0
while True:
    result=s.find(sub_string,position,n)
    if result == -1:
        break
    else:
        print('Found at index:',result)
        count=count+1
        position=result+len(sub_string)
print(f"The total number of times the substring'{sub_string}' is present in main string:'{count}'")