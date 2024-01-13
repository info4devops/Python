# Finding Armstrong number using while loop

# Take input from user
n=int(input('Enter any number: ')) # example n= 234
s=n # assigning input value to the s variable
b=len(str(n))
sum1=0
while n!=0:
	# finding units place
	r= n%10 # r= 4
	cube_of_digit=r**3 # finding cube of digit
	sum1=sum1+cube_of_digit
	#finding remaining digits except units place digit
	n=n//10 # new n value =23
	# repeate while loop until n value becomes 0
print(f'The sum of squeres of digits in n:{s} is:{sum1}')
if s == sum1:
    print(f"The given number {s} is an armstrong number")
else:
    print(f"The given number {s} is not an armstrong number")
