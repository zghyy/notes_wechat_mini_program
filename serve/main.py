# -*- coding: utf-8 -*-
"""
@Author  : guohaoyuan
@Time    : 2020/10/15 下午6:53
"""

from flask import Flask
import pymysql
import mysql_info as SQLINFO

app = Flask(__name__)


# 添加笔记 需要发送POST请求
@app.route('/addnote', methods=['POST'])
def addnote():
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)

    return 1


# 查询笔记 直接发送GET请求
@app.route('/getnote', methods=['GET'])
def getnote():
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = '''SELECT * FROM NOTE'''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("Unable to fetch data!")
    conn.close()
    return 1


# 删除笔记 需要发送POST请求
@app.route('/delnote', methods=['POST'])
def delnote():
    return 1

@app.route('/editnote',methods=['POST'])
def editnote():
    return 1