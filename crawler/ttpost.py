class Post:
    def __init__(self,
        head, link,
        site,
        by, by_link,
        fromm, fromm_link,
        pub_date
        raw_html):

        self.head = head
        self.link = link
        self.site = site
        self.by = by
        self.by_link = link
        self.fromm = fromm
        self.fromm_link = fromm_link
        self.pub_date = pub_date
        self.raw_html = raw_html


    def __str__(self):
        return \
'''
{} <{}>
{} by {} <{}> from {} <{}>
{}
'''.format(
    self.head,
    self.link,
    self.site,
    self.by,
    self.by_link,
    self.fromm,
    self.fromm_link,
    self.pub_date)
