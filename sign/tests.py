from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):#在这里添加的数据并不会真正向数据库添加
        Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,address="shenzhen",start_time='2019-10-12')
        Guest.objects.create(id=1,event_id=1,realname="alen",phone='12324',email='alen@qq.com',sign=False)
    def test_event_models(self):
        result=Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address,"shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='12324')
        self.assertEqual(result.realname,'alen')
        self.assertFalse(result.sign)
class IndexPageTest(TestCase):
    def test_index_page_renders_index_template(self):
        response=self.client.get('/index/')
        self.assertEqual(response.status_code,200)#断言进入index是否返回200
        self.assertTemplateUsed(response,'index.html')#判断是否进入index.thml页面
#测试登录
class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','admin@mail.com','admin123456')
    def test_add_admin(self): #测试添加用户
        user=User.objects.get(username="admin")
        self.assertEqual(user.username,"admin")
        self.assertEqual(user.email,"admin@mail.com")
    def test_login_action_username_password_null(self):#用户名，密码为空
        test_data={'username':'','password':''}
        response=self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password is error!",response.content)
    def test_login_action_username_password_error(self):
        test_data={'username':'abc','password':'123'}
        response=self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password is error!",response.content)
    def test_login_action_username_password_right(self):
        test_data={'username':'admin','password':'admin123456'}
        response=self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code, 302)#登陆成功后跳转到了event_manage重定向了
#测试发布会管理
class EventManageTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','admin@mail.com','admin123456')
        Event.objects.create(name="xiaomi5",limit=2000,address="beijing",status=1,start_time='2019-10-23 12:30:00')
        self.login_user={'username':'admin','password':'admin123456'}
    def test_event_manage_success(self):#测试发布会'xiaomi5'
        response=self.client.post('/login_action/',data=self.login_user)#先登录再进入会员页
        response=self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)
    def test_event_manage_search(self):#测试发布会搜索
        response=self.client.post('/login_action/',data=self.login_user)#先登录再进入会员页
        response=self.client.post('/search_name/',{"name":"xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

class GuestManageTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','admin@mail.com','admin123456')
        Event.objects.create(id=1,name="xiaomi6",limit=2000,address="beijing",status=1,start_time='2019-10-23 12:30:00')
        Guest.objects.create(realname="alen",phone='12345',email="alen@mail.com",sign=0,event_id=1)
        self.login_user={'username':'admin','password':'admin123456'}
    def test_event_manage_success(self):
        response=self.client.post('/login_action/',data=self.login_user)
        response=self.client.post('/guest_manage/')
        self.assertIn(b"alen", response.content)
        self.assertIn(b"12345", response.content)
    def test_event_manage_search(self):
        response=self.client.post('/login_action/',data=self.login_user)
        response=self.client.post('/search_phone/',{'phone':'12345'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"12345", response.content)