'''
往数据库批量插入数据
'''

import pymysql,re


f = open('dict.txt')

# 连接数据库
db = pymysql.connect(user = 'root',
                     password = 'xmm',
                     database = 'dict',
                     charset = 'utf8')

# 获取游标（操作数据库，执行SQL语句，得到执行结果）
cur = db.cursor()

# 执行语句
sql = 'insert into words (word,mean) values(%s,%s)'
for line in f:
    # tmp = line.split(' ',1)
    # word = tmp[0]
    # mean = tmp[1].strip()
    # cur.execute(sql,[word,mean])
    tup = re.findall(r'(\S+)\s+(.*)',line)[0]   # 正则表达式
    print(tup)
    cur.execute(sql,tup)

try:
    db.commit()
except:
    db.rollback()

# 关闭游标
cur.close()
# 关闭数据库
db.close()
