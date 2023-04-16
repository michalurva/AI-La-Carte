import logging

class Logger:
    """
    A generic logger class that simplifies the usage of Python's logging library.

    This class is designed to be easily integrated into existing classes or modules and provides
    a consistent logging format and level throughout the application.

    Usage:
        # Instantiate the Logger class
        logger = Logger(__name__)

        # Use the logger for various log levels
        logger.debug("Debug message")
        logger.info("Information message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")
    """
    def __init__(self, name):
        # Create a logger with the specified name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler and set its log level to DEBUG
        file_handler = logging.FileHandler('log.txt')
        file_handler.setLevel(logging.DEBUG)
        
        # Create a console handler and set its log level to DEBUG
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Create a formatter for log messages
        formatter = logging.Formatter('%(asctime)s - %(name)-20s - %(levelname)-8s - %(message)s')

        # Add the formatter to the file handler
        file_handler.setFormatter(formatter)
        # Add the formatter to the console handler
        console_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)
        # Add the console handler to the logger
        self.logger.addHandler(console_handler)        

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)
        
    def info_header(self, message):
        self.logger.info("=======================================================")
        self.logger.info(message)

    def info_footer(self, message):
        self.logger.info(message)
        self.logger.info("=======================================================")

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
    
    #log class properties, including values of lists and dictionaries
    def log_class_properties(self, obj):
        self.logger.info("Class properties for " + obj.__class__.__name__)
        for key in obj.__dict__:
            self.logger.info(key + ": " + str(obj.__dict__[key]))
            # if type(obj.__dict__[key]) is list:
            #     for item in obj.__dict__[key]:
            #         self.logger.info(item.__class__.__name__ + ": " + str(item))
            # elif type(obj.__dict__[key]) is dict:
            #     for item in obj.__dict__[key]:
            #         self.logger.info(item.__class__.__name__ + ": " + str(item))