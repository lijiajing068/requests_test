import unittest
import requests
from yewu.common.Common_old import encrypted_request

class return_sings(unittest.TestCase):
    def setUp(self,areaID=0, offset=0, total='true', limit=100):
        self.base_url='http://music.163.com/api/discovery/new/songs?areaId=%d&offset=%d&total=%s&limit=%d' %\
              (areaID, offset, total, limit)

    def tearDown(self):
        print(self.result)

    def test_return_sings(self):
        cookies = {
            'appver': '2.1.2.184499',
            'os': 'pc',
            'channel': 'netease',
        }
        data = {'areaID': 9, 'offset': 0, 'total': 'true', 'limit': 100}
        payload=encrypted_request(data)
        r=requests.get(self.base_url,params=payload, cookies=cookies)
        self.result=r.json()
        self.assertEqual=(['alias'],'电影《我和我的祖国》主题曲')

if __name__=='__main__':
    unittest.main()