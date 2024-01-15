# Covert Digit to Word 0-9999

words_upto_ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Tweleve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']

words_for_tens = ['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']

words_for_hundreds = ['','One Hundred','Two Hundred','Three hundred','Four Hundred','Five Hundred','Six Hundred','Seven Hundred','Eight Hundred','Nine Hundred']

words_for_Thousand = ['','Thousand','Two Thousand','Three Thousand','Four Thousand','Five Thousand','Six Thousand','Seven Thousand','Eight Thousand','Nine Thousand']

n = int(input('Enter a digit from 0-999: '))
output = " "
if n ==0:
  output="Zero"
elif n <=19:
  output=words_upto_ones[n]
elif n <=99:
  output = words_for_tens[n//10]+" "+words_upto_ones[n%10]

elif n <=999:
  output = words_for_hundreds[n//100]+" And "+ words_for_tens[(n//10)%10]+" "+words_upto_ones[n%10]
  
elif n <=9999:
  output = words_for_Thousand[n//1000] +" "+ words_for_hundreds[(n//100)%10]+" And "+ words_for_tens[(n//10)%10]+" "+words_upto_ones[n%10]
  
else:
  output = print('please enter a number from 0-99')
print(output)
