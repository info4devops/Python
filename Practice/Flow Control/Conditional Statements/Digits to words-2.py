# Converting two digit number into corresponding english word

words_upto_19=[',','One','Two','Three','Four','Five','Six','Seven','Eight','Nine',
               'Ten','Eleven','Twelve','Thirteen','Fourteen','fifteen','sixteen','seventeen',
               'Eighteen','Nineteen']

words_for_tens=['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']

n=int(input('Enter any 2 digits number:'))
output=''

if n==0:
    print(f'Entered Number is {n} and its corresponding Word is: Zero')

elif n<=19:
    output=words_upto_19[n]
    print(f'Entered Number is {n} and its corresponding Word is: {output}')

elif n<=99:
    output=words_for_tens[n//10]+' '+words_upto_19[n%10]
    print(f'Entered Number is {n} and its corresponding Word is: {output}')

else:
    output='Please Enter a value from 0 to 99 only'
    print(f'Entered Number is {n} and its corresponding Word is: {output}')


