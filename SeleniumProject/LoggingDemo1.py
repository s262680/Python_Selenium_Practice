import logging

#Creating log file, log file will be save in the project folder with dir
logging.basicConfig(filename="C://TempForTesting/Log/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s', #specify the format of the message
                    datefmt='%m/%d/%Y %I:%M:%S %p') #specify the date format (Not necessary)
                    #level=logging.DEBUG) #set logging level start from debug

#By default ebug and Info msg will not be displayed in the console window since they are not important unless changing the setting
#logging.debug("This is a debug message")
#logging.info("This is a info message")

#Printing Warning,Error and Critical message in the console window
#logging.warning("This is a warning message")
#logging.error("This is a error message")
#logging.critical("This is a critical message")


#Another method

#Create logger object
logger=logging.getLogger()
#set logging level start from debug
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")