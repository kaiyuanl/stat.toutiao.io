import infra.log
from infra.spiders import *
from infra.items import *
from infra.misc import *
from infra.data import *



log.info('-'*10 + 'crawler start' + '-'*10)
last_date = get_last_date()
today_date = get_today_date()
log.info('last_date:{}\t today_date:{}'.format(last_date, today_date))

period = get_days(last_date, today_date)

for d in period:
    year = d.year
    month = d.month
    day = d.day

    ttprev_url = gen_prev_url(year, month, day)
    log.info('date:{}\turl:{}'.format(d, ttprev_url))
    if test_url_valid(ttprev_url):
        log.info('url <{}>is valid. spider starts'.format(ttprev_url))
        spider = ttspider.PostSpider(d, ttprev_url)
        (posts, html, pub_date) = spider.content()
        add_daily(pub_date, 1, html)
        for p in posts:
            add_post(p)
    else:
        log.warning('url <{}> can not be accessed'.format(ttprev_url))
        add_daily(d, -1, None)

log.info('-'*10 + 'crawler finishs' + '-'*10)
