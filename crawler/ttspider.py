import re
import datetime
import ttpost
import ttinfra

class PostSpider:
    _re_item = re.compile(
        r'<li>[\s\S]*?</li>')

    _re_head_link = re.compile(
        r'<h4><a href="(.*?)".*?>(.*?)</a></h4>')

    _re_desc = re.compile(
        r'<p>[\s\S]*?</p>')

    _re_origin_by_from = re.compile(
        r'<p>([\s\S]*?)&nbsp;[\s\S]*?by([\s\S]*?)from([\s\S]*?)</p>')

    _re_origin_by = re.compile(
        r'<p>([\s\S]*?)&nbsp;[\s\S]*?by([\s\S]*?)</p>')

    _re_origin = re.compile(
        r'<p>([\s\S]*?)&nbsp;[\s\S]*?</p>')

    _re_link = re.compile(
        r'href="(.*?)"')

    def __init__(self, pub_date, url):
        self.pub_date = pub_date
        self.url = url

    def content(self):
        html = ttinfra.get_html_content(self.url)
        raw_items = self._re_item.findall(html)
        for raw_item in raw_items:
            head, link, author, author_link, submitter, submitter_link \
             =None, None, None, None, None, None

            match = self._re_head_link.search(raw_item)
            link = match.group(1)
            head = match.group(2)

            match = self._re_desc.search(raw_item)
            if (self._re_origin_by_from.search(match.group(0))) is not None:
                pass




if __name__ == '__main__':
    test_date = datetime.date(2014, 10, 10)
    spider = PostSpider(test_date, ttinfra.gen_prev_url(2014, 10, 10))
    spider.content()
