import inspect
import logging
'''
Use base class to control the global logging instance
Use BaseClass as parent class and we need to inherit it in our child class
'''

class BaseClass:

    def getLogger(self):
        # in order to print the child class file location in logger, in place of the '__name__' default one
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # get an object for your logging feature, responsible for logging everything
        # __name__ will catch the testing file name, by default it'll give 'root'

        # Set file path and formatting: formatter >> fileHandler >> set method >> logger
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # will take filehandler object: decide the file path and format

        # set level of visibility: debug (info for developers on the code run) < info < warning < error < critical
        logger.setLevel(logging.INFO)
        return logger

