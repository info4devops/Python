# Program to create log file and store either WARNING ar higher-level messages with explicitly mentioning file mode


import logging
logging.basicConfig(filename='mylog.txt',
                    level=logging.DEBUG,                    
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S%p')

logging.info('A New Request Came')
try:
  x=int(input('x='))
  y=int(input('y='))
  result=x/y
  print('The Result:',result)

except ZeroDivisionError as msg:
  print('Division with zero is not possible')
  logging.exception(msg)

except ValueError as msg:
  print('Please Enter Interger Values Only')
  logging.exception(msg)

logging.info('Request Processing Completed')
print()