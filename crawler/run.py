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
        ttinfra.logger.info('url is valid. spider start for {}'.format(ttprev_url))
        spider = ttspider.PostSpider(d, ttprev_url)
        posts = spider.content()
        for p in posts:
            ttdata.add_post(p)
    else:
        ttinfra.logger.waring('url <{}> is not access'.formate(ttprev_url))
    continue

ttinfra.logger.info('-'*10 + 'crawler finish' + '-'*10)
