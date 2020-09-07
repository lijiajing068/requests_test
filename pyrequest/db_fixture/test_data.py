import sys
sys.path.append('../db_fixture')
from mysql_db import DB
#创建测试数据
datas={
    #发布会测试数据
    'sign_event':[
        {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2019-10-12 12:00:00','create_time':'2019-12-12 23:0:00'},
        {'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'北京会展中心','start_time':'2019-10-12 12:00:00','create_time':'2019-12-12 23:0:00'},
        {'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'北京会展中心','start_time':'2019-10-12 12:00:00','create_time':'2019-12-12 23:0:00'},
        {'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2019-10-12 12:00:00','create_time':'2019-12-12 23:0:00'},
        {'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','start_time':'2019-10-12 12:00:00','create_time':'2019-12-12 23:0:00'},
    ],
}
#将测试数据插入表
def init_data():
    db=DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()
if __name__=='__main__':
    init_data()