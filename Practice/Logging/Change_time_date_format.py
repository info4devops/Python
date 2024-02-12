# Program to create log file and store message with time stamp
# %I = 12hrs 
# %H = 24hrs


import logging
# 12 hrs format
#logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S%p') #12/02/2024 05:08:08PM:WARNING:WARNING Information

#24hrs format
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S%p') #12/02/2024 17:09:52PM:WARNING:WARNING Information

print('Logging Demo')
logging.debug('DEBUG Information')
logging.info('INFO Information')
logging.warning('WARNING Information')
logging.error('ERROR Information')
logging.critical('CRITICAL Information')
print()
