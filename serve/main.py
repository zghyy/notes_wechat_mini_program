# -*- coding: utf-8 -*-
"""
@Author  : guohaoyuan
@Time    : 2020/10/15 下午6:53
"""

from flask import Flask, request
import pymysql
import mysql_info as SQLINFO

app = Flask(__name__)


# 添加笔记 需要发送POST请求
@app.route('/addnote', methods=['POST'])
def addnote():
    title = request.form['value']['title']
    content = request.form['value']['content']
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = "INSERT INTO NOTE(title,content) VALUES ('%s','%s')" % (title, content)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    return "done"


# 查询笔记 直接发送GET请求
@app.route('/getnote', methods=['GET'])
def getnote():
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = '''SELECT * FROM NOTE'''
    results = {}
    try:
        cursor.execute(sql)
        notes = cursor.fetchall()
        count = 0
        for row in notes:
            results.update(NOTE(row[0], row[1], row[2]).formateNote(count))
            count += 1
    except:
        print("Unable to fetch data!")
    conn.close()
    return results


# 删除笔记 需要发送POST请求
@app.route('/delnote', methods=['POST'])
def delnote():
    key = request.form['key']
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = "DELETE FROM NOTE WHERE key = %s" % key
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    return "done"


@app.route('/editnote', methods=['POST'])
def editnote():
    key = request.form['key']
    title = request.form['value']['title']
    content = request.form['value']['content']
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = "UPDATE NOTE SET title = %s,content = %s WHERE key = %s" % (title, content, key)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    return "done"


class NOTE:
    def __init__(self, key, title, content):
        self.key = str(key)
        self.title = str(title)
        self.content = str(content)

    def formateNote(self, count):
        result = {count: {"key": self.key, "value": {"title": self.title, "content": self.content}}}
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=23333, debug=False)
