import unittest
import urllib.parse
import requests
from yewu.common.Common_old import basic_data_cookies,basic_data_headers

class select_allsongs(unittest.TestCase):
    # def setUp(self,cat='全部歌单', types='all', offset= 0, index= 1):
    #     self.base_url='http://music.163.com/api/playlist/list?cat=%s&type=%s&order=%s&offset=%d&total=true&limit=30&index=%d'%(urllib.parse.quote(cat), types, types, offset, index)


    def test_allsongs(self,cat='全部歌单', types='all', offset= 0, index= 1):
        base_url = 'http://music.163.com/api/playlist/list?cat=%s&type=%s&order=%s&offset=%d&total=true&limit=30&index=%d' % (
        urllib.parse.quote(cat), types, types, offset, index)
        # payload = {'cat': '全部歌单', 'types': 'all', 'offset': 0, 'index': 1}
        r=requests.get(base_url,headers=basic_data_headers(), cookies=basic_data_cookies())
        self.result=r.json()
        self.assertEqual(self.result['code'],200)
        return self.result['playlists'][1]["id"]

# if __name__=='__main__':
#     unittest.main()


