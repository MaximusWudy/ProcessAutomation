import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__) # get an object for your logging feature, responsible for logging everything
    # __name__ will catch the testing file name, by default it'll give 'root'

    # Set file path and formatting: formatter >> fileHandler >> set method >> logger
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler = logging.FileHandler('logfile.log')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) # will take filehandler object: decide the file path and format

    # set level of visibility: debug (info for developers on the code run) < info < warning < error < critical
    logger.setLevel(logging.INFO)

    logger.debug("A debug statement is executed.")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened, such as assertion error")
    logger.critical("Critical issue")

