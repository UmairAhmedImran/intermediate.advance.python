import logging
logger = logging.getLogger(__name__) # __name__ makes the name = filename in this like helper
#logger.propagate = False # makes no result in main
logger.info('Hello from helper')