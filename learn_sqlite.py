'''
操作SQL数据库时，首先提供''数据库对应的驱动''，然后''connection''连接数据库。
通过''Cursor''执行SQL语句

最后一定要关闭cursor和connection
'''

#导入SQLite驱动
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn=sqlite3.connect('test.db')
# 创建一个Cursor:
cursor=conn.cursor()
# 执行一条SQL语句，如果列表已存在将其删除
cursor.execute('drop table if exists user506')
# 执行一条SQL语句，创建user表
cursor.execute('create table user506 (id varchar(20) primary key,name varchar(20))')
# 继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user506 (id,name) values (\'1\',\'Michael\')')
cursor.execute('insert into user506 (id,name) values (\'2\',\'Jason\')')
# 通过rowcount获得插入的行数:
cursor.rowcount
# 关闭Cursor
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

#试试查询表中的信息
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
# 执行查询语句:
cursor.execute('select * from user506 where id=? ',(2,))
# 获得查询结果集:
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()




'''
#SQLite数据库操作练习
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('drop table if exists user')
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select name from user where score>? and score<? order by score',(low,high))
    name_list=[]
    for select_name in cursor.fetchall():
        name_list.append(select_name[0])
    cursor.close()
    conn.close()
    return name_list

'''


























