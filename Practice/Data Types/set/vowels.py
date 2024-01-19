# Program to print different vowels present in the given word
word = input('Enter any string:')
s=set(word)
v={'a','e','i','o','u'}
result=s.intersection(v)
result1=sorted(result)
print(f'Before Sorting Vowels in word:{result}')
print(f'After Sorting Vowels in word:{result1}')