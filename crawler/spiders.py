import re
import datetime
import sys
sys.path.append('..')
from infra.items import Post
from infra.urls import *
from infra.misc import *

class PostSpider:
    _re_item = re.compile(
        r'<div class="content"[\s\S]*?>([\s\S]*?</div>[\s\S]*?)</div>')

    _re_head_link = re.compile(
        r'<h3 class="title">[\s\S]*?<a[\s\S]*?href="(.*)">(.*)</a>[\s\S]*?</h3>')

    _re_desc = re.compile(
        r'<div class="meta">([\s\S]*?)</div>')

    _re_site_by_from = re.compile(
        r'<div class="meta">([\s\S]*?)&nbsp;[\s\S]*?by([\s\S]*?)from([\s\S]*?)&nbsp;')

    _re_site_by = re.compile(
        r'<div class="meta">([\s\S]*?)&nbsp;[\s\S]*?by([\s\S]*?)&nbsp;')

    _re_site_from = re.compile(
        r'<div class="meta">([\s\S]*?)&nbsp;[\s\S]*?from([\s\S]*?)&nbsp;')

    _re_site = re.compile(
        r'([\s\S]*?)&nbsp;[\s\S]*?')

    _re_link = re.compile(
        r'<a .*? href="(.*?)".*?>(.*?)</a>')

    def __init__(self, pub_date, url):
        self.pub_date = pub_date
        self.url = url
        self.posts = []

    def content(self):
        self.html = get_html_content(self.url)
        raw_items = self._re_item.findall(self.html)
        for raw_item in raw_items:
            head, link, site, by, by_link, fromm, fromm_link \
             =None, None, None, None, None, None, None

            match = self._re_head_link.search(raw_item)
            link = match.group(1)
            head = match.group(2)

            match = self._re_desc.search(raw_item)
            desc = match.group(0)

            match = self._re_site_by_from.search(desc)
            if match is not None:
                site = match.group(1)
                raw_by = match.group(2)
                raw_from = match.group(3)
                match = self._re_link.search(raw_by)
                if match is not None:
                    by = match.group(2)
                    by_link = match.group(1)
                else:
                    by = raw_by

                match = self._re_link.search(raw_from)
                if match is not None:
                    fromm = match.group(2)
                    fromm_link = match.group(1)
                else:
                    fromm = raw_from

                new_post = Post(head, link,
                    process_str(site),
                    process_str(by),
                    process_str(by_link),
                    process_str(fromm),
                    process_str(fromm_link),
                    self.pub_date,
                    raw_item)
                self.posts.append(new_post)

                continue

            match = self._re_site_by.search(desc)
            if match is not None:
                site = match.group(1)
                raw_by = match.group(2)
                match = self._re_link.search(raw_by)
                if match is not None:
                    by = match.group(2)
                    by_link = match.group(1)
                else:
                    by = raw_by
                new_post = Post(head, link,
                    process_str(site),
                    process_str(by),
                    process_str(by_link),
                    process_str(fromm),
                    process_str(fromm_link),
                    self.pub_date,
                    raw_item)
                self.posts.append(new_post)

                continue

            match = self._re_site_from.search(desc)
            if match is not None:
                site = match.group(1)
                raw_from = match.group(2)
                match = self._re_link.search(raw_from)
                if match is not None:
                    fromm = match.group(2)
                    fromm_link = match.group(1)
                else:
                    by = raw_by
                new_post = Post(head, link,
                    process_str(site),
                    process_str(by),
                    process_str(by_link),
                    process_str(fromm),
                    process_str(fromm_link),
                    self.pub_date,
                    raw_item)
                self.posts.append(new_post)

                continue

            match = self._re_site.search(desc)
            if match is not None:
                site = match.group(1)
                new_post = Post(head, link,
                    process_str(site),
                    process_str(by),
                    process_str(by_link),
                    process_str(fromm),
                    process_str(fromm_link),
                    self.pub_date,
                    raw_item)
                self.posts.append(new_post)

                continue

        for post in self.posts:
            post.link = gen_redir_url(post.Link)
            post.by_link = gen_redir_url(post.Byy_Link)
            post.fromm_link = gen_redir_url(post.Fromm_Link)

        return (self.posts, self.html, self.pub_date)





#test code
if __name__ == '__main__':
    test_date = datetime.date(2014, 10, 10)
    spider = PostSpider(test_date, gen_prev_url(2014, 10, 10))
    (posts, html, pub_date) = spider.content()
    for post in posts:
        print '-'*10
        print post
        #logger.info(post.head)
