# Writing data into CSV file

import csv

with open('emp.csv', 'w', newline='') as g:
    w = csv.writer(g)
    w.writerow(['E-No', 'E-NAME', 'E-SAL'])
    n = int(input('Enter number of employees: '))
    
    for i in range(n):
        e_no = input('Enter Employee Number: ')
        e_name = input('Enter Employee Name: ')
        e_sal = input('Enter Employee Salary: ')
        w.writerow([e_no, e_name, e_sal])
        print('Data Inserted Successfully')
        
        option = input('Do you want to enter more records? [Y/N]: ')
        if option.lower() == 'n':
            break

print('All The Employee Details Entered Successfully')
