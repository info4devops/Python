import logging
import inspect
def get_custom_logger(level):
  function_name=inspect.stack()[1][3]
  logger_name=function_name+'logger'
  # Creating logger object and set up level
  logger = logging.getLogger(logger_name)
  logger.setLevel(level)
  
  #Creating File Handler object and set up level
  fileHandler=logging.FileHandler('abc.log',mode='a') #append mode
  fileHandler.setLevel(level)
  
  #Creating formatter object for file Handler: 12hr format
  formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s',datefmt='%m-%d-%Y %I:%M:%S%p')
  
  #Setting up formatter object to file Handler object
  fileHandler.setFormatter(formatter)
  
  #Adding Handler Object to Logger Object
  logger.addHandler(fileHandler)
  return logger