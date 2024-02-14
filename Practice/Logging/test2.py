# Test file for logging configuration file

import logging
import logging.config

class LoggerDemoConf():
  def testLog(self):
    logging.config.fileConfig('configuration.txt')
    logger = logging.getLogger(LoggerDemoConf.__name__)
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
    
demo=LoggerDemoConf()
demo.testLog()