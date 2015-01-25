import ttspider
import ttpost
import ttdata
import ttinfra

ttinfra.logger.info('-'*10 + 'crawler start' + '-'*10)
last_date = ttdata.get_last_date()
today_date = ttinfra.get_today_date()
ttinfra.logger.info('last_date:{}\t today_date:{}'.format(last_date, today_date))

period = ttinfra.get_days(last_date, today_date)

for d in period:
    year = d.year
    month = d.month
    day = d.day

    ttprev_url = ttinfra.gen_prev_url(year, month, day)
    ttinfra.logger.info('date:{}\turl:{}'.format(d, ttprev_url))
    if ttinfra.test_url_valid(ttprev_url):
        ttinfra.logger.info('url <{}>is valid. spider starts'.format(ttprev_url))
        spider = ttspider.PostSpider(d, ttprev_url)
        (posts, html, pub_date) = spider.content()
        ttdata.add_daily(pub_date, 1, html)
        for p in posts:
            ttdata.add_post(p)
    else:
        ttinfra.logger.warning('url <{}> can not be accessed'.format(ttprev_url))
        ttdata.add_daily(d, -1, None)

ttinfra.logger.info('-'*10 + 'crawler finishs' + '-'*10)
