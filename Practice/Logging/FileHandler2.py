# Program for file Handler : Used class name as logger name

import logging
class LoggerDemoFile:
  
  def testLog(self):
    # Creating logger object and set up level
    logger=logging.getLogger(LoggerDemoFile.__name__) # class name as logger name
    logger.setLevel(logging.DEBUG)
    
    # Creating Console Handler object and setting up level
    
    fileHandler=logging.FileHandler('xyz.txt',mode='a')
    fileHandler.setLevel(logging.ERROR)
    
    # Creating formatter object
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s',datefmt='%m-%d-%Y %I:%M:%S%p')
    
    # Setting up formatter object to Handler object
    fileHandler.setFormatter(formatter)
    
    #Adding consoleHandler object to logger object
    logger.addHandler(fileHandler)
    
    #Writting messages by using logger object
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')   
    logger.error('error message')
    logger.critical('critical message')
    
demo=LoggerDemoFile()
demo.testLog()