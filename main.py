num=int(input("Enter a number:"))
temp=num # aliasing
rev=0
dig=num%10 # finding digit value
rev=rev*10+dig
num = num//10
print(dig)
print(rev*10)
print(num//10)