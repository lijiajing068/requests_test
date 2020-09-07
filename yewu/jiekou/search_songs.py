import unittest
import requests
from yewu.common.Common_old import encrypted_request
class search_songs(unittest.TestCase):
    def setUp(self):
        self.base_url="http://music.163.com/weapi/cloudsearch/get/web"

    def tearDown(self):
        print(self.result)

    def test_search_songs(self):
        #s是需要搜索的关键字
        data = {
            's': '蔡依林',
            'offset': 0,
            'limit': 100,
            'type': 10
        }
        payload=encrypted_request(data)
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual=(['code'],200)
        return(self.result['result']['albums'][2]['id'])

if __name__=='__main__':
    unittest.main()