import requests
import pytest
import jsonpath
import json
import pytest_html
import time
from HttpRequest import HTTPrequest
from common.common import get_md5,encrypted_request,basic_data_headers
from py._xmlgen import html
from logger import Log
class TestLogin(HTTPrequest):
    ''' 登录接口 '''
    def setup_class(self):
        log=Log()
    def setup_method(self):
        self.base_url = 'http://music.163.com/weapi/login/cellphone?csrf_token='
    def httpRequest(self,*args,**kwargs):
        data=kwargs.get('data')#data中可包含多个参数
        if data:
            data=encrypted_request(data)
        log.info("进行网易云请求, args: {0}, kwargs: {1}".format(args,kwargs))
        html=super(TestLogin,self).httpRequest(*args,**kwargs)
        loger.info("url: {0} 请求失败. Header: {1}".format(
            args[0], kwargs.get('headers')))
        return False
    def test_login_success(self):
        #登陆成功
        username = "15074816863"
        password_md5=get_md5('15074816863')
        data={'phone':username,'password':password_md5,'rememberLogin': 'true'}
        payload = encrypted_request(data)
        #s = requests.Session()
        #r = s.post(self.base_url,headers=basic_data_headers(),data=payload)
        r=self.httpRequest(url,method="POST",data=data)
        #print(r.json()) #登录时记住session
        self.result = r.json()
        #print(self.result)
        #print(self.result)
        #加载为json对象
        dict=json.loads(r.text)
        #assert self.result['code'] == 200
        #assert self.result["profile"]["nickname"] == '樱桃你个车厘子1808'
        #return self.result['account']['id']
        self.h=jsonpath.jsonpath(dict, '$.account..id')
        self.j=jsonpath.jsonpath(dict,'$.loginType')
        return self.h,self.j

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
if __name__=='__main__':
    pytest.main(["-s",'test_login.py','--html=../report/report-login.html'])

    # 构造测试集
    #suit = unittest.TestSuite()
    #suit.addTest(LoginTest("test_login_success"))  # 把这个类中需要执行的测试用例加进去，有多条再加即可
    #runner = unittest.TextTestRunner()
    #runner.run(suit)  # 运行测试用例
