# Program to create log file and store either WARNING ar higher-level messages with explicitly mentioning file mode


import logging

#logging.basicConfig(format='%(asctime)s') #2024-02-12 16:59:25,185

#logging.basicConfig(format='%(asctime)s:%(levelname)s') #2024-02-12 17:00:17,424:WARNING

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s') #2024-02-12 17:01:06,915:WARNING:WARNING Information

print('Logging Demo')
logging.debug('DEBUG Information')
logging.info('INFO Information')
logging.warning('WARNING Information')
logging.error('ERROR Information')
logging.critical('CRITICAL Information')
print()
