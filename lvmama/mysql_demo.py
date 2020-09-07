from pymysql import cursors,connect
#连接数据库
conn=connect(host='127.0.0.1',
             user='root',
             password='123456',
             db='lvmama',
             charset='utf8mb4',
             cursorclass=cursors.DictCursor)
try:
    with conn.cursor() as cursor:
    #创建嘉宾数据库
        sql='INSERT INTO sign_guest(realname,phone,email,sign,event_id,create_time) VALUES ("tom",12233,"tom@mail.com",0,1,NOW());'
    #提交事务
    conn.commit()

    with conn.cursor() as cursor:
        sql="SELECT realname,phone,emali,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql,('12233',))
        result=cursor.fetchone()
        print(result)
finally:
    conn.close()