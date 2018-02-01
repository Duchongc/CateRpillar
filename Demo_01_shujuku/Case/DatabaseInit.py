# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 0025 11:04
# @Author  : LaoZhongYi
# @File    : DatabaseInit.py
import pymysql
class DataBaseInit(object):
    # 本类用于完成初始化数据操作
    # 创建数据库,创建数据表,向表中插入测试数据
    def __init__(self,host,port,dbname,username,password,charset):
        self.host = host
        self.port = port
        self.db = dbname
        self.user = username
        self.passwd = password
        self.charset = charset
    def create(self):
        try:
            # 连接数据库
            conn = pymysql.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                passwd = self.passwd,
                charset = self.charset
            )
            # 获取数据库游标
            cur = conn.cursor()
            # 创建数据库,如果有库,将会报错,提示库已存在,所以暂时注释掉
            # cur.execute(creat_database)
            # 选择创建好的gloryroad数据库
            conn.select_db("gloryroad")
            # 创建测试表,忽略忽略忽略
            # cur.execute(create_table)
        except pymysql.Error as e:
            raise e
        else:
            # 关闭游标
            cur.close()
            # 提交操作
            conn.commit()
            # 关闭连接
            conn.close()
            print("创建数据库及表成功")
    def insertDatas(self):
        try:
            # 连接数据库中的某个库
            conn  = pymysql.connect(
                host = self.host,
                port = self.port,
                db = self.db,
                user = self.user,
                passwd = self.passwd,
                charset = self.charset
            )
            cur = conn.cursor()
            # 向测试表中插入测试数据
            sql = "insert into testdata(bookname,author) values(%s,%s);"
            cur.executemany(sql,[('selenium webdriver 实战宝典','吴晓华'),
                                       ('http权威指南','古尔利'),
                                       ('探索式软件测试','惠特克'),
                                       ('暗时间','刘未鹏')])
        except pymysql.Error as e:
            raise e
        else:
            conn.commit()
            print("初始数据插入成功")
            # 确认数据插入成功
            cur.execute("select * from testdata;")
            for i in cur.fetchall():
                print(i[1],i[2])
            cur.close()
            conn.close()

