# Libarary: pymal and module: ymal
from pyaml import yaml
emp_dict={'Number':111,
          'Age':23}

# Serialization to ymal string
ymal_string=yaml.dump(emp_dict)
print(ymal_string)
print()

# Serialization to ymal file
with open('emp.ymal','w') as f:
  yaml.dump(ymal_string,f)

# De-Serialization to ymal string
print('::::De-Serialization to ymal string::::::')
New_emp_dict = yaml.safe_load(ymal_string)
print("New Employee Dict:",New_emp_dict)

for k,v in New_emp_dict.items():
  print('{}:{}'.format(k,v))
print()

#De-Serialization to ymal file
print('::::De-Serialization from ymal file::::::')
with open('emp.ymal','r') as f:
  New_emp_dict=yaml.safe_load(f)
print(New_emp_dict)


  