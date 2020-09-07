import unittest
import requests
from yewu.common.Common_old import basic_data_cookies

class fnew_sings(unittest.TestCase):
    def setUp(self,year=2019, month=10, area='ALL'):
        self.base_url='http://music.163.com/api/discovery/new/albums/area?year=%d&month=%d&area=%s&type=hot&offset=0&total=true&limit=20&rcmd=true' \
              % (year, month, area)

    def tearDown(self):
        print(self.result)

    def test_fnew_sings(self):
        data={'year':2019, 'month':10, 'area':'ALL'}
        r=requests.get(self.base_url,params=data, cookies=basic_data_cookies())
        self.result=r.json()
        self.assertEqual(['alias'],'电影《我和我的祖国》主题曲')
        if ['alias']=='电影《我和我的祖国》主题曲':
            print("test_fnew_sings is pass!")
        else:
            print("test_fnew_sings is faild!")


if __name__=='__main__':
    unittest.main()