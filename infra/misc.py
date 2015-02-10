import datetime

def get_today_date():
    return datetime.date.today()

def get_days(start, end):
    start = start + datetime.timedelta(days = 1)
    diff = end - start
    for i in range(diff.days + 1):
        yield start + datetime.timedelta(i)

def process_str(raw_str):
    if raw_str is None:
        return raw_str
    return raw_str.replace('\n','').replace('&nbsp;','').strip()

if __name__ == '__main__':
    print 'today is', get_today_date()
    dt = datetime.date(2015, 1, 10)
    period = get_days(dt, get_today_date())
    for d in period:
        print d