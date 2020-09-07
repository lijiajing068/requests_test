import unittest
import requests
from yewu.common.Common_old import get_md5
class GetEventListTest(unittest.TestCase):
    ''' 登录接口 '''
    def setUp(self):
        self.base_url = "https://login.lvmama.com/nsso/geetest/login/validateNormalLogin.do"

    def tearDown(self):
        print(self.result)

    def test_username_null(self):
        #用户名为空
        auth_user = ('', '123')
        r = requests.post(self.base_url,auth=auth_user)
        self.result = r.json()
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['errorCode'], 101)
        self.assertEqual(self.result['errorMsg'], '用户名或密码不能为空!')

    def test_password_null(self):
        #密码为空
        auth_user = ('1507', '')
        r = requests.post(self.base_url,auth=auth_user)
        self.result = r.json()
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['errorCode'], 101)
        self.assertEqual(self.result['errorMsg'], '用户名或密码不能为空!')

    def test_username_error(self):
        #密码错误
        auth_user = ('1507', '123')
        r = requests.post(self.base_url,auth=auth_user)
        self.result = r.json()
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['errorCode'], 101)
        self.assertEqual(self.result['errorMsg'], '用户名或密码不能为空!')

    def test_login_success(self):
        #登陆成功
        str = 'ljj863667546'
        password_md5=get_md5(str)
        payload = {'userName':'15074816863', 'password':password_md5,'verifyCode':''}
        r = requests.post(self.base_url,data=payload)
        #userName=request.POST.get('userName','')
        #password=request.POST.get('password','')
        #request.session['user']=userName
        #request.session['mima']=password
        #b=request.session.get('user','')
        #a=request.session.get('mima','')
        #print(a)
        #print(b)
        self.result = r.json()
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['errorCode'], 0)

if __name__ == '__main__':
    unittest.main()
