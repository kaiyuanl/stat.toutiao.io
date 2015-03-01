# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import *
from items import Post, Daily
from misc import get_today_date
from config import database_config

class Database:
    def __init__(self, user, pwd, host, db):
        conn_str = 'mysql://{}:{}@{}/{}?charset=utf8'.format(user, pwd, host, db)
        engine = create_engine(conn_str)
        metadata = MetaData(bind = engine, reflect = True)

        self.post_table = Table('post', metadata, autoload = True)
        self.daily_table = Table('daily', metadata, autoload = True)

        post_mapper = mapper(Post, self.post_table)
        daily_mapper = mapper(Daily, self.daily_table)

        self.session = create_session()

    def get_all_dailies(self):
        return self.session.query(Daily).all()

    def get_empty_dailies(self):
        return self.session.query(Daily).filter(self.daily_table.c.Status < 0)

    def get_last_date(self):
        q = self.session.query(self.daily_table.c.Pub_Date, func.max(self.daily_table.c.Pub_Date)).all()
        if q[0][1] is not None:
            return q[0][1]
        else:
            return datetime.date(2014, 9, 26)


    def add_post(self, post):
        self.session.add(post)

    def add_posts(self, posts):
        for post in posts:
            self.session.add(post)

    def add_daily(self, daily):
        self.session.add(daily)

    def __keyword(self, keyword):
        pass

    def search(self, keyword):
        '''search items whose heads contain keyword'''
        self.__keyword(keyword)
        return self.session.query(Post).filter(self.post_table.c.Head.like('%{}%'.format(keyword)))

    def commit(self):
        try:
            self.session.flush()
        except IntegrityError as err:
            print err


toutiao = Database(
    database_config['username'],
    database_config['password'],
    database_config['host'],
    database_config['database']
    )

#test code
if __name__ == '__main__':
    print toutiao.get_last_date()


