import pytest
import requests
from common.common import basic_data_cookies
from common.logger import Log
from common.RequestFen import MyHttpservice
#from yewu.jiekou.wangyi_login import LoginTest


class TestSelect_detail():
    log = Log()
    #def tearDown(self):
        #print(self.result)
    def test_select_detail(self,ids='2695632861'):
        #self.log.info("-------------start:select_detail----------")
        #ids为查询全部歌单中某一歌曲的id
        url = 'http://music.163.com/api/playlist/detail?id={0}'.format(ids)
        params = ids
        cookies = basic_data_cookies()
        #s = LoginTest().test_login_success()
        #r=s.get(base_url,params=ids)
        #r = requests.get(base_url, params=ids,cookies=basic_data_cookies())
        request=MyHttpservice.get
        request(self)
        #self.result=r.json()
        #assert r.status_code == 200
        #self.log.info(u"查询歌曲详情：%s"%self.result['code'])
        #self.log.info("-------------end:select_detail----------")
        #return self.result

if __name__=='__main__':
    pytest.main(['-s','test_select_detail.py'])
