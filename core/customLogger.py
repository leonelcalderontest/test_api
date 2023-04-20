import logging


class Logger:

    def __init__(self):
        self.logger = logging.getLogger(Logger.__name__)

    def testLog(self):
        """
        Sets up the logger for the test and returns it.
        :return: The logger object.
        :rtype: logging.Logger
        """
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s%(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
        if not self.logger.hasHandlers():
            pass
        else:
            self.logger.handlers.clear()
        return self.logger
