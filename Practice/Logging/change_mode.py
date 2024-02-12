# Program to create log file and store either WARNING ar higher-level messages with explicitly mentioning file mode


import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR,filemode='w')
print('Logging Demo')
logging.debug('DEBUG Information')
logging.info('INFO Information')
logging.warning('WARNING Information')
logging.error('ERROR Information')
logging.critical('CRITICAL Information')
print()
