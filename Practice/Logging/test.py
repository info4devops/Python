# test module for custom logger demo

import logging
from Customelogger import get_custom_logger
#from Customelogger import*

class Logging_Demo:
  
  def m1(self):
    logger=get_custom_logger(logging.DEBUG)
    # Writing message objects using logger object
    logger.debug('debug message from m1 module')
    logger.info('info message from m1 module')
    logger.warning('warning message from m1 module')
    logger.error('error message from m1 module')
    logger.critical('critical message from m1 module')
  
  def m2(self):
    logger=get_custom_logger(logging.WARNING)
    # Writing message objects using logger object
    logger.debug('debug message from m2 module')
    logger.info('info message from m2 module')
    logger.warning('warning message from m2 module')
    logger.error('error message from m2 module')
    logger.critical('critical message from m2 module')
  
  def m3(self):
    logger=get_custom_logger(logging.ERROR)
    # Writing message objects using logger object
    logger.debug('debug message from m3 module')
    logger.info('info message from m3 module')
    logger.warning('warning message from m3 module')
    logger.error('error message from m3 module')
    logger.critical('critical message from m3 module')

l=Logging_Demo()
print('Custome Logger Demo')
l.m1()
l.m2()
l.m3()

# Output will be appended in abc.log file