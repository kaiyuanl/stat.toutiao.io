# -*- coding: utf-8 -*-
import ConfigParser
from sqlalchemy import *
from sqlalchemy.orm import *
from sttpost import Post, Daily, Keyword

class Database:
    def __init__(self, user, pwd, host, db):
        conn_str = 'mysql://{}:{}@{}/{}?charset=utf8'.format(user, pwd, host, db)
        engine = create_engine(conn_str)
        metadata = MetaData(bind = engine, reflect = True)
        self.post_table = Table('post', metadata, autoload = True)
        self.daily_table = Table('daily', metadata, autoload = True)
        #keyword_table = Table('keyword', metadata, autoload = True)
        post_mapper = mapper(Post, self.post_table)
        daily_mapper = mapper(Daily, self.daily_table)
        #keyword_mapper = mapper(Keyword, keyword_table)

        self.session = create_session()

    def __del__(self):
        pass

    def search(self, keyword):
        q = self.session.query(Post).filter(self.post_table.c.Head.like('%{}%'.format(keyword)))
        return q

    def list_post(self):
        q = self.session.query(Post).all()
        return q


config = ConfigParser.ConfigParser(allow_no_value = True)
config.read('.config')
user = config.get('dbconnstr', 'User')
pwd = config.get('dbconnstr', 'Password')
host = config.get('dbconnstr', 'Host')
db = config.get('dbconnstr', 'Database')

toutiao = Database(user, pwd, host, db)

#some test code
if __name__ == '__main__':
    l = toutiao.list_post()
    for i in l:
        print i.Head.encode('utf-8')

    r = toutiao.search(u'贝索斯'.encode('utf-8'))
    for i in r:
        print i.Head.encode('utf-8')
    