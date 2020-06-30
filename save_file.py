'''
往数据库批量插入数据
'''

import pymysql

# 连接数据库
db = pymysql.connect(user = 'root',
                     password = 'xmm',
                     database = 'stu',
                     charset = 'utf8')

# 获取游标（操作数据库，执行SQL语句，得到执行结果）
cur = db.cursor()

# 执行语句
# 存入图片
# with open('dog.jpg','rb') as f:
#     data = f.read()
# sql = 'insert into images values (1,%s,%s)'
# cur.execute(sql,[data,'Dog'])
#
# try:
#     db.commit()
# except:
#     db.rollback()

# 提取图片

sql = 'select photo from images where comment = "Dog"'
cur.execute(sql)
data = cur.fetchone()[0]
with open('1.jpg','wb') as f:
    f.write(data)

# 关闭游标
cur.close()
# 关闭数据库
db.close()
