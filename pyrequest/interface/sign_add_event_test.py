import unittest,requests,hashlib
from time import time
class AddEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url="http://127.0.0.1/api/sec_add_event"
        self.api_key="&Guest-Bugmaster"
        now_time = time()
        self.client_time = str(now_time).split('.')[0]
        #获取客户端签名和时间戳
        md5 = hashlib.md5()
        sign_str = self.client_time + '&Guest-Bugmaster'
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()
    def test_add_event_request_error(self):
        ''' 请求方法错误 '''
        r = requests.get(self.base_url)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10011)
        self.assertEqual(self.result['message'], 'request error')
    def test_add_event_sign_null(self):
        ''' 签名参数为空 '''
        payload={'eid':1,'name':'','limit':'','address':'','start_time':'','create_time':'','time':'','sign':''}
        r = requests.get(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10012)
        self.assertEqual(self.result['message'], 'user sign null')

    def test_add_event_time_out(self):
        ''' 请求超时 '''
        now_time=str(int(self.client_time)-61)
        payload = {'eid': 1, 'name': '', 'limit': '', 'address': '', 'start_time': '', 'create_time':'','time':now_time,'sign':'adc'}
        r = requests.get(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10013)
        self.assertEqual(self.result['message'], 'user sign timeout')

    def test_add_event_sign_error(self):
        ''' 签名错误 '''
        payload = {'eid': 1, 'name': '', 'limit': '', 'address': '', 'start_time': '', 'create_time': '',
                   'time': self.client_time, 'sign': 'abc'}
        r = requests.get(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10014)
        self.assertEqual(self.result['message'], 'user sign error')

    def test_add_event_sign_success(self):
        ''' 添加event成功 '''
        payload = {'eid': 21, 'name': '一家5手机发布会', 'limit': '234', 'address': '上海', 'start_time': '2019-12-13 12:00:00', 'create_time': '2019-12-14 13:00:00',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.get(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    unittest.main()
