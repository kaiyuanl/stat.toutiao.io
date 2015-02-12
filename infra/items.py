class Post(object):
    def __init__(self,
        head, link,
        site,
        byy, byy_link,
        fromm, fromm_link,
        pub_date,
        raw_html):

        self.Head = head
        self.Link = link
        self.Site = site
        self.Byy = byy
        self.Byy_Link = byy_link
        self.Fromm = fromm
        self.Fromm_Link = fromm_link
        self.Pub_Date = pub_date
        self.Raw_Html = raw_html


    def __str__(self):
        return \
'''
{} <{}>
{} by {} <{}> from {} <{}>
{}
'''.format(
    self.Head,
    self.Link,
    self.Site,
    self.Byy,
    self.Byy_Link,
    self.Fromm,
    self.Fromm_Link,
    self.Pub_Date)


class Daily(object):
    def __init__(self, pub_date, status = -1, raw_html = None):
        self.Pub_Date = pub_date
        self.Status = status
        self.Raw_Html = raw_html

    def __str__(self):
        return str(self.Pub_Date)