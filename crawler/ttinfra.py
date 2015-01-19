import urllib
import urllib2
import urlparse
import datetime
import httplib

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
    req = urllib2.Request(url)
    opr = urllib2.build_opener()
    f = opr.open(req)
    return f.url

def get_today_date():
    return datetime.date.today()

def get_days(start, end):
    diff = end - start
    for i in range(diff.days + 1):
        yield start + datetime.timedelta(i)


if __name__ == '__main__':
    url = gen_prev_url(2015, 1, 18)
    print url
    print get_html_content(url)
    if test_url_valid(url):
        print url, 'is accessable'

    origin_url = 'http://toutiao.io/r/ps2vm'
    redir_url = gen_redir_url(origin_url)
    print redir_url

    print 'today is', get_today_date()
