from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    name=models.CharField(max_length=100)   #发布会标题
    limit=models.IntegerField()             #参加人数
    status=models.BooleanField()            #状态
    address=models.CharField(max_length=200)#地址
    start_time=models.DateTimeField('event time')  #发布会时间
    create_time=models.DateTimeField('2019-12-12 23:00:00')#创建时间
    def _str_(self):#告诉python如何将对象以str的方式显示
        return self.name

#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE) #外键关联发布会id
    realname=models.CharField(max_length=64)   #姓名
    phone=models.CharField(max_length=16)   #电话
    email=models.EmailField()                  #邮箱
    sign=models.BooleanField()                 #签名状态
    create_time=models.DateTimeField('2019-12-12 23:00:00')#创建时间

class Meta:   #Meta内部类，用于定义模型类的行为
    unique_together=("event","phone")#设置这两个字段为联合主键

def _str_(self):
    return self.realname