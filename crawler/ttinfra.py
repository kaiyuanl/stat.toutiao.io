import urllib
import urllib2
import urlparse
import datetime
import os
import platform
import logging
import httplib

#logging relevant code
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


def get_html_content(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def gen_prev_url(year, month, day):
    return 'http://toutiao.io/prev/%04d-%02d-%02d'%(year, month, day)

def test_url_valid(url):
    result = None
    host, path = urlparse.urlparse(url)[1:3]
    try:
        httpconn = httplib.HTTPConnection(host)
        httpconn.request('HEAD', path)
        result = httpconn.getresponse().status
    except StandardError:
        pass

    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return result in good_codes


def gen_redir_url(url):
    if url is None:
        return url
    try:
        req = urllib2.Request(url)
        opr = urllib2.build_opener()
        f = opr.open(req)
        redir = f.url
        return redir
    except:
        print err
    finally:
        return url

def get_today_date():
    return datetime.date.today()

def get_days(start, end):
    start = start + datetime.timedelta(days = 1)
    diff = end - start
    for i in range(diff.days + 1):
        yield start + datetime.timedelta(i)

def process_str(raw_str):
    if raw_str is None:
        return raw_str
    return raw_str.replace('\n','').replace('&nbsp;','').strip()


#test code
if __name__ == '__main__':
    url = gen_prev_url(2015, 1, 18)
    print url
    #print get_html_content(url)
    if test_url_valid(url):
        print url, 'is accessable'

    origin_url = 'http://toutiao.io/r/w57a1'
    redir_url = gen_redir_url(origin_url)
    print redir_url

    print 'today is', get_today_date()
    dt = datetime.date(2015, 1, 10)
    period = get_days(dt, get_today_date())
    for d in period:
        print d
