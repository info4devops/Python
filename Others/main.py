[loggers]
keys=root,LoggerDemoConf

[handlers]
keys=fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[logger_LoggerDemoConf]
level=DEBUG
handlers=fileHandler
qualname=demoLogger

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
filename=example.log
mode=w

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S %p
