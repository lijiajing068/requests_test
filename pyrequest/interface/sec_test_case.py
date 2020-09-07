import unittest
import requests

class GetEventListTest(unittest.TestCase):
    ''' 获得发布会列表 '''
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"

    def tearDown(self):
        print(self.result)

    def test_get_event_list_auth_null(self):
        ''' auth 为空 '''
        r = requests.get(self.base_url, params={'eid':1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10011)
        self.assertEqual(self.result['message'], 'user auth null')

    def test_get_event_list_auth_error(self):
        ''' auth 错误 '''
        auth_user=('adb','123')
        r = requests.get(self.base_url,auth=auth_user, params={'eid':1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10012)
        self.assertEqual(self.result['message'], 'user auth fail')

    def test_get_event_list_eid_null(self):
        ''' eid 为空 '''
        auth_user = ('admin', 'admin123456')
        r = requests.get(self.base_url,auth=auth_user, params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_get_event_list_eid_success(self):
        ''' 根据eid查询成功 '''
        auth_user = ('admin', 'admin123456')
        r = requests.get(self.base_url,auth=auth_user, params={'eid':'1'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['name'],u'红米Pro发布会')
        self.assertEqual(self.result['data']['address'],u'北京会展中心')


if __name__ == '__main__':
    unittest.main()
