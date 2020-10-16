# -*- coding: utf-8 -*-
"""
@Author  : guohaoyuan
@Time    : 2020/10/15 下午6:53
"""

from flask import Flask, request
import pymysql
import mysql_info as SQLINFO
import time
import datetime

app = Flask(__name__)


# 添加笔记 需要发送POST请求
@app.route('/addnote', methods=['POST'])
def addnote():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    title = request.form['title']
    content = request.form['content']
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = "INSERT INTO NOTE(title,content,createtime,updatetime) VALUES ('%s','%s','%s','%s')" % (
        title, content, now, now)
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
            results.update(NOTE(row[0], row[1], row[2], row[3], row[4]).formateNote(count))
            count += 1
    except:
        print("Unable to fetch data!")
    conn.close()
    return results


# 删除笔记 需要发送POST请求
@app.route('/delnote', methods=['POST'])
def delnote():
    notekey = request.form['notekey']
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = "DELETE FROM NOTE WHERE notekey = %d" % notekey
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    return "done"


@app.route('/editnote', methods=['POST'])
def editnote():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    notekey = request.form['notekey']
    title = request.form['title']
    content = request.form['content']
    conn = pymysql.connect(SQLINFO.HOST, SQLINFO.USER, SQLINFO.PASSWORD, SQLINFO.DATABASE)
    cursor = conn.cursor()
    sql = "UPDATE NOTE SET title = '%s',content = '%s',updatetime = '%s' WHERE notekey = %d" % (
    title, content, now, notekey)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    return "done"


class NOTE:
    def __init__(self, notekey, title, content, createtime, updatetime):
        self.notekey = int(notekey)
        self.title = str(title)
        self.content = str(content)
        self.createtime = createtime.strftime("%Y-%m-%d %H:%M:%S")
        self.updatetime = updatetime.strftime("%Y-%m-%d %H:%M:%S")

    def formateNote(self, count):
        result = {count: {"notekey": self.notekey, "title": self.title, "content": self.content,
                          "createtime": self.createtime, "updatetime": self.updatetime}}
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
