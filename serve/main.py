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
    notes = []
    results = []
    try:
        cursor.execute(sql)
        notes = cursor.fetchall()
        for row in notes:
            results.append(NOTE(row[0], row[1], row[2]).formateNote())
    except:
        print("Unable to fetch data!")
    conn.close()
    return results


# 删除笔记 需要发送POST请求
@app.route('/delnote', methods=['POST'])
def delnote():
    return 1


@app.route('/editnote', methods=['POST'])
def editnote():
    return 1


class NOTE:
    def __init__(self, key, title, content):
        self.key = str(key)
        self.title = str(title)
        self.content = str(content)

    def formateNote(self):
        result = {"key": self.key, "value": {"title": self.title, "content": self.content}}
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=23333, debug=False)
