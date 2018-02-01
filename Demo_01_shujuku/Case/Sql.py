# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 0025 11:04
# @Author  : LaoZhongYi
# @File    : Sql.py
creat_database = 'CREATE DATABASE IF NOT EXISTS gloryroad DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
# 创建表的sql有问题,暂时忽略,直接手动创建
create_table = """
    drop table if exists testdata;
    create table testdata(
        id int not null primary key auto_increment comment '主键',
        bookname varchar(40) unique not null comment '书名',
        author varchar(30) not null comment '作者'
    )engine = innodb character set utf8 comment '测试数据表';
"""

