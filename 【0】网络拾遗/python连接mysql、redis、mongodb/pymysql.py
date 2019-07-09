# python连接mysql
# 方法一：
# import pymysql
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='devops', charset='utf8')
# print(conn)
# 打印出此信息说明python连接mysql成功。<pymysql.connections.Connection object at 0x000001933AA6CDD8>

# 方法二：
import pymysql
sqlArgs = {
'host':'127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'devops',
    'charset': 'utf8'
}
conn = pymysql.connect(**sqlArgs)
print(conn)

cursor = conn.cursor() # 建立游标
row = cursor.execute("show tables") #  执行sql语句
data = cursor.fetchone() # 取出一条数据
data = cursor.fetchmany(3) # 取出3条数据
data = cursor.fetchall() # 全部取出
print(data)

# 新增数据
# 单条
# row=cursor.execute("insert into stars (name,age)values('邓肯',23)")
# row=cursor.execute('insert into stars(name,age) VALUES (%s,%s)',('科比',23))
conn.commit()

# 批量
rows=cursor.executemany('insert into stars(name,age) VALUES (%s,%s)',[('杜兰特',1),('卡哇伊',2)])
conn.commit()

cursor.close()
conn.close()

# 完整规范示例：
try:
    rows=cursor.executemany('insert into stars(name,age) VALUES (%s,%s)',[('杜兰特',1),('卡哇伊',2)])
    conn.commit()
except :
    conn.rollback()
finally:
    cursor.close()
    conn.close()