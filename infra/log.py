import os, platform, logging, datetime

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'sttlogging.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'sttlogging.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w', #'a' opens the file for appending
)

logger = logging.getLogger('test_logger')

def info(msg):
	logger.info(msg)

def warning(msg):
	logger.warning(msg)

def error(msg):
	logger.error(msg)

def exception(msg):
	logger.exception(msg)

if __name__ == '__main__':
    info('info message')

    warning('warning message')

    error('error message')

    exception('exception message')