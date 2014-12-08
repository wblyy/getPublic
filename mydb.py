#coding=utf-8
import random

import MySQLdb
import sys

class Mydb(object):
    def __init__(self, user, passwd, dbname):
        self._id = 0           # use in pop function
        self.user = user
        self.passwd = passwd
        self.dbname = dbname

    @property
    def db(self):
        return MySQLdb.connect("192.168.1.111", self.user, self.passwd, self.dbname, charset='utf8')

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def _execute(self, *args, **kwargs):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args, **kwargs)
        conn.commit()

    def _query_row(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchone()
        return rows

    def _query_rows(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchall()
        return rows    

class Ganhuo(Mydb):
    def __init__(self):
        Mydb.__init__(self, 'root', '654321', 'ganhuo')

    def get_questions(self):
        return self._query_rows('select qid,title from zhidao_music_tag where title like "%什么名字%" or title like "%插曲%" or title like "%歌词是%" or title like "%哪首歌%" or title like "%这首歌%" or title like "%背景乐%" or title like "%片尾曲%" or title like "%片头曲%" or title like "%背景音乐%" or title like "%猜歌%" or title like "%什么歌%" ')
    def insert_data(self, title, post_date, source, content):
        self._execute('insert ignore weixin (title, post, source, content) values (%s, %s, %s, %s)', (title, post_date, source, content))

if __name__ == "__main__":
    mydb = Tiedb()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    print mydb.get_ties()
    sys.exit(0)
    with open('./csdn.csv', 'r') as f:
        for line in f:
            row = line.strip('\r\n').split(' # ')
            print '\t'.join(row)
            mydb.insert_data(row[0], row[1], row[2])
