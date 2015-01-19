import mysql.connector
from mysql.connector import errorcode
import ConfigParser
import ttpost
import datetime

class MySqlConn:
    def __init__(self, user, pwd, host, db):
        try:
            self.conn = mysql.connector.connect(
                user = user,
                password = pwd,
                host = host,
                database = db,
                autocommit = True
                )
            self.cursor = self.conn.cursor()

        except mysql.connector.Error as err:
            print err

    def __del__(self):
        try:
            self.conn.close()
        except mysql.connector.Error as err:
            print err

    def get_last_date(self):
        args = (0, )
        result = self.cursor.callproc('GetLastDate', args)
        if result[0] is None:
            return datetime.date(2014, 10, 10)
        else:
            result_str = result[0].encode('ascii', 'replace')
            dt = datetime.datetime.strptime(result_str, '%Y-%m-%d')
            return datetime.date(dt.year, dt.month, dt.day)

    def add_post(self, head, link, site, by, by_link,
        fromm, fromm_link, pub_date):
        args = (head, link, site, by, by_link,
            fromm, fromm_link, pub_date)
        try:
            result = self.cursor.callproc('AddPost', args)
        except mysql.connector.Error as err:
            print err


config = ConfigParser.ConfigParser(allow_no_value = True)
config.read('.config')

user = config.get('dbconnstr', 'User')
pwd = config.get('dbconnstr', 'Password')
host = config.get('dbconnstr', 'Host')
db = config.get('dbconnstr', 'Database')

conn = MySqlConn(user, pwd, host, db)

def get_last_date():
    return conn.get_last_date()

def add_post(new_post):
    conn.add_post(new_post.head, new_post.link, new_post.site, new_post.by,
        new_post.by_link, new_post.fromm, new_post.fromm_link, new_post.pub_date)

