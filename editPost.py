# -*- coding: utf-8 -*-
import pymysql
import re
import time

def submitPosts(contents):
    try:
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        #connnect db
        # contents = "<h1>title,type</h1><h2>description</h2><p>fuck you</p>"
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='crazyblog',charset='utf8')
        cur = conn.cursor()

        sql = ""
        titleType = re.findall(r'<h1>([\s\S]*?)</h1>', contents)
        contents = re.sub(r'<h1>([\s\S]*?)</h1>','', contents)
        description = re.findall(r'<h2>([\s\S]*?)</h2>', contents)
        contents = re.sub(r'<h2>([\s\S]*?)</h2>','', contents)
        temp = titleType[0].split(',')
        title = temp[0]
        type = temp[1]
        curTime = str(time.strftime("%d/%m/%Y"))
        Time = curTime.split('/')
        dataTime = month[int(Time[1])-1] + ' ' + Time[0] + ',' + ' ' + Time[2]

        sql += '\'' + title + '\'' + ', ' + '\'' + type + '\''+ ', ' + '\'' + description[0] + '\'' + ', ' + '\'' + contents + '\''+ ', ' + '\'' + dataTime + '\''
        sql = "insert into posts(title,types, description, content, datatime) values(" + sql + ")"
        #
        # sql = "truncate table posts"
        # cur.execute(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        return 'success'
    except:
        return 'failed'

def indexPosts():
    file = []

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='crazyblog', charset='utf8')
    cur = conn.cursor()
    sql = "select * from posts"
    cur.execute(sql)

    temp = cur.fetchall()
    for i in range(len(temp)):
        if i == 10:
            break
        file.append(list(temp[i]))

    file = sorted(file, key=lambda x: x[0], reverse=True)
    conn.commit()
    cur.close()
    return file

def selectPosts(postId):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='crazyblog', charset='utf8')
    cur = conn.cursor()
    sql = "select * from posts WHERE Id = " + str(postId)
    cur.execute(sql)

    content = list(cur.fetchall()[0])
    conn.commit()
    cur.close()
    return content

def postsType():
    typeList = []
    file = []

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='crazyblog', charset='utf8')
    cur = conn.cursor()
    sql = "select * from posts"
    cur.execute(sql)

    temp = cur.fetchall()
    for i in range(len(temp)):
        post = list(temp[i])
        if post[2] not in typeList:
            typeList.append(post[2])

    for types in typeList:
        List = []
        sql = "SELECT * FROM posts WHERE types IN(SELECT types FROM posts GROUP BY types HAVING types = '" + types + "')"
        cur.execute(sql)

        temp = cur.fetchall()
        for i in range(len(temp)):
            if i == 3:
                break
            List.append(list(temp[i]))
        file.append(List)
    conn.commit()
    cur.close()
    return file

def selectPoststype(types):
    detail = []
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='crazyblog', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM posts WHERE types IN(SELECT types FROM posts GROUP BY types HAVING types = '" + types.strip() + "')"
    cur.execute(sql)

    temp = cur.fetchall()
    for i in range(len(temp)):
        detail.append(list(temp[i]))

    conn.commit()
    cur.close()
    return detail

def searchPost(Input):
    file = []
    dic = []
    result = []

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='crazyblog', charset='utf8')
    cur = conn.cursor()
    sql = "select * from posts"
    cur.execute(sql)

    temp = cur.fetchall()
    for i in range(len(temp)):
        if i == 10:
            break
        List = list(temp[i])
        List.append(0)
        file.append(List)

    for i in range(len(file)):
        # print(type(Input))
        if Input in str(file[i][1]):
            file[i][6] += 10
        if Input in str(file[i][2]):
            file[i][6] += 5
        if Input in str(file[i][3]):
            file[i][6] += 3
        if Input in str(file[i][5]):
            file[i][6] += 5
        dic.append(file[i])

    dic = sorted(dic, key=lambda x: x[6], reverse=True)
    conn.commit()
    cur.close()

    for i in range(len(dic)):
        if i == 10:
            break
        result.append(dic[i])
    return result


# contents = "<h1>tale,tassa</h1><h2>description</h2><p>fuck you</p>"
# submitPosts(contents)
# print(indexPosts())
# print(selectPosts(14))
# print(postsType())
# print(selectPoststype('a'))
# print(searchPost('ti'))





