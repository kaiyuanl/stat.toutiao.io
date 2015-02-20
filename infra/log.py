import os, platform, logging, datetime

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = 'crawler_log.log',
    filemode = 'a', #'a' opens the file for appending
)

logger = logging.getLogger('test_logger')

def info(msg):
    print msg
    logger.info(msg)

def warning(msg):
    print msg
    logger.warning(msg)

def error(msg):
    print msg
    logger.error(msg)

if __name__ == '__main__':
    info('info message')

    warning('warning message')

    error('error message')
