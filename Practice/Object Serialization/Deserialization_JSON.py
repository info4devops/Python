# Deserialization using JSON

import json

#Taken json string in triple quotes because it containe multistring laterals

json_string = '''{
  "name": "Sunny",
  "age": 22,
  "ismarried": true,
  "GF_name": null
  }'''
  
print('Type of json_string:',type(json_string))

# De-serialization from json string to python dict
emp_dict=json.loads(json_string)
print('Name:',emp_dict['name'])
print('Age:',emp_dict['age'])
print('ismarried:',emp_dict['ismarried'])
print('GF_name:',emp_dict['GF_name'])
print()

# Printing using key-values pairs of dict

for k,v in emp_dict.items():
  print('{}:{}'.format(k,v))