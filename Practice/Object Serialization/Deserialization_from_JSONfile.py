# De-serialization from JSON file
import json

# Reading the emp.json file using with

with open('emp.json','r') as f:
  emp_dict=json.load(f)
  
# De-serialization from json string to python dict
print('Name:',emp_dict['name'])
print('Age:',emp_dict['age'])
print('ismarried:',emp_dict['ismarried'])
print('GF_name:',emp_dict['GF_name'])
print()

# Printing using key-values pairs of dict
print('--Printing the data as key-values pairs--')

for k,v in emp_dict.items():
  print('{}:{}'.format(k,v))