first_num = int(input("1st Number: "))
second_num = int(input("2nd Number:"))
num_of_terms = int(input("Enter the number of terms: "))
print(first_num,second_num)
print("The numbers in fibonacci series are : ")
while(num_of_terms-2):
   third_num = first_num + second_num
   first_num=second_num
   second_num=third_num
   print(third_num)
   num_of_terms=num_of_terms-1