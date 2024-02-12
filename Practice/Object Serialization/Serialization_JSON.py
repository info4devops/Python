# Serialization using JSON
#dumps():it serializes python dict to json string
#dump(): it serializes python dict to json and write that json to file. i.e serializes to file

#loads(): it de-serializes json string to python dict 
#load(): reading json form file and convert to python dict object. i.e. Deserilizes from json file

import json
#Employee Object:Used python dict
employee={'name':'Sunny',
          'age':22,
          'ismarried':True,
          'GF_name':None
          }

# Serialization: dict to json string
json_string=json.dumps(employee,indent=4,sort_keys=True) # for readability
print(json_string)
print('Type of json_string:',type(json_string))

# Serialization: dict to json string and write that to a file
#Open file using with

with open('emp.json','w') as f:
  json.dump(employee,f,indent=4)
