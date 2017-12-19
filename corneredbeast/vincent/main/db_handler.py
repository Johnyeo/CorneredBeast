# coding:utf-8
import pymysql


class Database(object):
    def __init__(self):
        pass

    # 查询数据 - 按名字
    def queryAll(self,name):
        conn = pymysql.connect(
            host = '127.0.0.1',
            port = '3306',
            password = '1004Xm@27',

        )

        return

