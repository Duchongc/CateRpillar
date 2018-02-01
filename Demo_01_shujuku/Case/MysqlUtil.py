# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 0025 11:04
# @Author  : LaoZhongYi
# @File    : MysqlUtil.py
import pymysql
from Demo_01_shujuku.Case.DatabaseInit import DataBaseInit
class MYMYSQL(object):
    def __init__(self,host,port,dbname,username,password,charset):
        dbInit = DataBaseInit(host,port,dbname,username,password,charset)
        dbInit.create()
        dbInit.insertDatas()
        self.conn = pymysql.connect(
            host = host,
            port = port,
            db = dbname,
            user = username,
            passwd = password,
            charset = charset

        )
        self.cur = self.conn.cursor()
    def getDataFromDataBases(self):
        self.cur.execute("select bookname,author from testdata;")
        datasTuple = self.cur.fetchall()
        return datasTuple
    def closeDatabase(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

