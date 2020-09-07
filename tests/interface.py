import requests
import unittest
class GetEventListTest(unittest.TestCase):
    #查询发布会接口测试
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/get_event_list"
    #发布会ID为空
    def test_get_event_null(self):
        r=requests.get(self.url,params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'] ,'parament error')
    #发布会ID不存在
    def test_get_event_error(self):
        r = requests.get(self.url, params={'eid': '901'})
        result = r.json()
        self.assertEqual (result['status'] ,10022)
        self.assertEqual (result['message'] ,'query result is empty')
    #发布会ID为2，查询成功
    def test_get_event_success(self):
        r = requests.get(self.url, params={'eid': '2'})
        result = r.json()
        # 断言接口返回值
        self.assertEqual (result['status'] ,200)
        self.assertEqual (result['message'] ,'add event success')
        self.assertEqual (result['data']['name'], '红米')
        self.assertEqual (result['data']['address'] , '北京')
        self.assertEqual (result['data']['start_time'] ,'2019-10-10T00:00:00')
if __name__ == '__main__':
    unittest.main()