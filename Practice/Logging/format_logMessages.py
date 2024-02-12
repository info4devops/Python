# Program to create log file and store either WARNING ar higher-level messages with explicitly mentioning file mode


import logging
#logging.basicConfig(format='%(levelname)s') # Print only Level Name i.e WARNING ect

logging.basicConfig(format='%(levelname)s:%(message)s') # Print both Level and message i.e WARNING:WARNING Information ect

print('Logging Demo')
logging.debug('DEBUG Information')
logging.info('INFO Information')
logging.warning('WARNING Information')
logging.error('ERROR Information')
logging.critical('CRITICAL Information')
print()
