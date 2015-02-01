# -*- coding: utf-8 -*-
import ConfigParser
from sqlalchemy import *

class Database:
    def __init__(self, user, pwd, host, db):
        conn_str = 'mysql://{}:{}@{}/{}?charset=utf8'.format(user, pwd, host, db)
        engine = create_engine(conn_str)
        metadata = MetaData(bind = engine, reflect = True)
        self.posts = Table('post', metadata, autoload = True)
        self.daily = Table('daily', metadata, autoload = True)

    def __del__(self):
        pass

    def search(self, keyword):
        q = self.posts.select(self.posts.c.Head.like('%{}%'.format(keyword)))
        return q.execute().fetchall()

    def list(self):
        q = self.posts.select()
        return q.execute().fetchall()

    def site(self, site):
        q = self.posts.select(self.posts.c.Site.like('%{}%'.format(site)))
        return q.execute().fetchall()


config = ConfigParser.ConfigParser(allow_no_value = True)
config.read('.config')
user = config.get('dbconnstr', 'User')
pwd = config.get('dbconnstr', 'Password')
host = config.get('dbconnstr', 'Host')
db = config.get('dbconnstr', 'Database')

toutiao = Database(user, pwd, host, db)

#some test code
if __name__ == '__main__':
    l = toutiao.list()
    for i in l:
        print i[1].encode('utf-8')

    q = toutiao.search(u'盖茨'.encode('utf-8'))
    for i in q:
        print i[1].encode('utf-8')