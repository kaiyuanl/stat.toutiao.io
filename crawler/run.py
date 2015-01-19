import ttspider
import ttpost
import ttdata
import ttinfra

last_date = ttdata.get_last_date()
today_date = ttinfra.get_today_date()
period = ttinfra.get_days(last_date, today_date)

for d in period:
    print d
    year = d.year
    month = d.month
    day = d.day

    ttprev_url = ttinfra.gen_prev_url(year, month, day)
    if ttinfra.test_url_valid(ttprev_url):
        spider = ttspider.PostSpider(d, ttprev_url)
        content = spider.content()
        posts = content[1]
        for p in posts:
            ttdata.add_post(p)
