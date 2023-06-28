import logging
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG) # makes a file and write message on it
#logging.debug('debug')
#logging.info('info')
#logging.warning('warning')
#logging.error('error')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
#logging.debug("debug")
#logging.info("ingo")
#logging.warning("warning")
#logging.error("error")
#logging.critical("critical")

#import helper
#logger = logging.getLogger(__name__)
#stream_h = logging.StreamHandler()
#file_h = logging.FileHandler('file.log')

#stream_h.setLevel(logging.WARNING)
#file_h.setLevel(logging.ERROR)

#formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#stream_h.setFormatter(formatter)
#file_h.setFormatter(formatter)

#logger.addHandler(stream_h)
#logger.addHandler(file_h)
#logger.warning('this is warning')
#logger.error('this is a error')


#import logging.config

#logging.config.fileConfig('logging.conf')

#logger = logging.getLogger('simpleExample') # .conf file is not supported but does the same thing
#logger.debug('debug')
#logger.info('info')

#try:
    #a = [1, 2, 3]
    #val = a[4]
#except IndexError as e:
    #logging.error(e, exc_info=True) # including second argument gives traceback of error

# beautiful code for storing data of exact 2000 bytes
#from logging.handlers import RotatingFileHandler
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

#handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
#logger.addHandler(handler)
#for _ in range(10000):
  #  logger.info("Hello World!")

#from logging.handlers import TimedRotatingFileHandler
#import time
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

#handler = TimedRotatingFileHandler('time_test.log', when='s', backupCount=5)
#logger.addHandler(handler)
#for _ in range(6):
  #  logger.info("Hello World!")
   # time.sleep(5)

#logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %p')
#logging.debug('debug')
#logging.warning('warning')
#logging.error('errpr')
