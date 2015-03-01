import sys
sys.path.append('..')

from spiders import *
from infra.items import *
from infra.misc import *
from infra.mails import send_mail
from infra.data import toutiao
import infra.xlog as log

log.info('-'*10 + 'crawler start' + '-'*10)
last_date = toutiao.get_last_date()
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
        spider = PostSpider(d, ttprev_url)
        (posts, html, pub_date) = spider.content()
        daily = Daily(pub_date, 1, html)
        toutiao.add_daily(daily)
        toutiao.commit()

        log.info(daily)
        for post in posts:
            toutiao.add_post(post)
            log.info(post)

        toutiao.commit()

    else:
        log.warning('url <{}> can not be accessed'.format(ttprev_url))
        daily = Daily(d, -1, None) #-1 stands for 'fail to obtain'
        toutiao.add_daily(daily)
        log.info(daily)
        toutiao.commit()

send_mail()
log.info('-'*10 + 'crawler finishs' + '-'*10)
