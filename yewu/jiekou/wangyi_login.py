import unittest
import requests
from yewu.common.Common_old import get_md5,encrypted_request,basic_data_headers

class LoginTest(unittest.TestCase):
    ''' 登录接口 '''
    def setUp(self):
        self.base_url='http://music.163.com/weapi/login/cellphone?csrf_token='
    def test_login_success(self):
        print("test_login_success")
        #登陆成功
        username = "15074816863"
        password_md5=get_md5('15074816863')
        data={'phone':username,'password':password_md5,'rememberLogin': 'true'}
        payload = encrypted_request(data)
        #print(payload)
        s = requests.Session()
        r = s.post(self.base_url,headers=basic_data_headers(),data=payload)
        #print(r.json()) #登录时记住session
        self.result = r.json()
        self.assertEqual(self.result['code'],200)
        self.assertEqual(self.result["profile"]["nickname"],'樱桃你个车厘子1808')
        print(self.result['account']['id'])
        return self.result['account']['id']
'''
    def test_login_failed(self):
        print("test_login_failed")
        #登陆失败
        base_url = 'http://music.163.com/weapi/login/cellphone?csrf_token='
        username = "1507481686399"
        password_md5=get_md5('15074816863')
        data={'phone':username,'password':password_md5,'rememberLogin': 'true'}
        payload = encrypted_request(data)
        r = requests.post(base_url,headers=basic_data_headers(),data=payload)
        self.result = r.json()
        self.assertEqual(self.result['code'],400)
'''
if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suit = unittest.TestSuite()
    # suit.addTest(LoginTest("test_login_failed"))  # 把这个类中需要执行的测试用例加进去，有多条再加即可
    # runner = unittest.TextTestRunner()
    # runner.run(suit)  # 运行测试用例
