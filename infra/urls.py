import urllib2
import httplib
import urlparse

from decorators import Retry

def get_html_content(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def gen_prev_url(year, month, day):
    return 'http://toutiao.io/prev/%04d-%02d-%02d'%(year, month, day)


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

@Retry(3)
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

#test code
if __name__ == '__main__':
    url = gen_prev_url(2015, 1, 18)
    print url

    if test_url_valid(url):
        print url, 'is accessable'