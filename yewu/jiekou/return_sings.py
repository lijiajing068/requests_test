import unittest
import requests
from yewu.common.Common_old import encrypted_request

class return_sings(unittest.TestCase):
    def setUp(self):
        self.base_url="http://music.163.com/weapi/song/enhance/player/url"

    def tearDown(self):
        print(self.result)

    def test_return_sings(self):
        data = {'csrf_token': '', 'ids': ['2978252207'], 'br': 999000}
        payload=encrypted_request(data)
        r=requests.post(self.base_url,data=payload,)
        self.result=r.json()
        self.assertEqual=(['code'],200)

if __name__=='__main__':
    unittest.main()