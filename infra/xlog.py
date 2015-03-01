import os
import platform
import logging
import datetime

from mails import need_to_send

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = 'crawler_log.log',
    filemode = 'a', #'a' opens the file for appending
)

xlogger = logging.getLogger('test_logger')

def info(msg):
    print msg
    xlogger.info(msg)
    need_to_send.append(msg)

def warning(msg):
    print msg
    xlogger.warning(msg)
    need_to_send.append(msg)


def error(msg):
    print msg
    xlogger.error(msg)
    need_to_send.append(msg)


if __name__ == '__main__':
    info('info message')

    warning('warning message')

    error('error message')
