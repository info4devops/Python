# Program for console Handler : Used class name as logger name

import logging
class LoggerDemoConsole:
  
  def testLog(self):
    # Creating logger object and set up level
    logger=logging.getLogger(LoggerDemoConsole.__name__)
    logger.setLevel(logging.DEBUG)
    
    # Creating Console Handler object and setting up level
    
    consoleHandler=logging.StreamHandler()
    consoleHandler.setFormatter(logging.ERROR)
    
    # Creating formatter object
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s',datefmt='%m-%d-%Y %I:%M:%S%p')
    
    # Setting up formatter object to Handler object
    consoleHandler.setFormatter(formatter)
    
    #Adding consoleHandler object to logger object
    logger.addHandler(consoleHandler)
    
    #Writting messages by using logger object
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')   
    logger.error('error message')
    logger.critical('critical message')
    
demo=LoggerDemoConsole()
demo.testLog()