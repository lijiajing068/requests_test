import unittest
import requests
from yewu.common.Common_old import encrypted_request,basic_data_headers
#from wangyi_login import LoginTest
class SelectSongs(unittest.TestCase):
    def test_select_songs(self,uid="1541194463"):
        #self.id=LoginTest.test_login_success()
        #print(self.id)
        #uid为登录后返回的用户id
        base_url = "http://music.163.com/weapi/user/playlist"
        data={'offset': 0, 'uid': uid, 'limit': 1000, 'csrf_token': ''}
        payload = encrypted_request(data)
        r=requests.post(base_url,data=payload,headers=basic_data_headers())
        print(r.content)
        self.result=r.json()
        #print(self.result)
        self.assertEqual(self.result['playlist'][0]['creator']['nickname'],'樱桃你个车厘子1808')
        #return result


if __name__ == '__main__':
    unittest.main()