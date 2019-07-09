import pymysql

# insert语句
# conn = None
# cursor = None
#
# try:
#     conn = pymysql.connect('127.0.0.1', 'root', '123456', 'devops')
#     print(conn.ping(False))
#     cursor = conn.cursor()
#     insert_sql = "insert into magedu(name,age) values ('马永亮', 38)"
#     cursor.execute(insert_sql)
#     conn.commit()
# except Exception as e:
#     conn.rollback()
#     print(e)
# finally:
#     if conn:
#         conn.close()
#     if cursor:
#         cursor.close()

# 查询
