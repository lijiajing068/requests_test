import unittest
import requests
from yewu.common.Common_old import basic_data_cookies
#from yewu.jiekou.wangyi_login import LoginTest


class select_detail(unittest.TestCase):
    #def tearDown(self):
        #print(self.result)

    def test_select_detail(self,ids='2695632861'):
        #ids为查询全部歌单中某一歌曲的id
        base_url = 'http://music.163.com/api/playlist/detail?id={0}'.format(ids)
        #s = LoginTest().test_login_success()
        #r=s.get(base_url,params=ids)
        r = requests.get(base_url, params=ids,cookies=basic_data_cookies())
        self.result=r.json()
        self.assertEqual(self.result['code'],200)
        return self.result

if __name__=='__main__':
    unittest.main()
