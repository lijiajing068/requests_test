import pytest
import requests
from common.common import encrypted_request
from common.logger import Log
class TestReturn_sings():
    log = Log()
    def test_return_sings(self,areaID=0, offset=0, total='true', limit=100):
        self.log.info("-------------start:new_songs----------")
        cookies = {
            'appver': '2.1.2.184499',
            'os': 'pc',
            'channel': 'netease',
        }
        self.base_url = 'http://music.163.com/api/discovery/new/songs?areaId=%d&offset=%d&total=%s&limit=%d' %\
              (areaID, offset, total, limit)
        #data = {'areaID': 9, 'offset': 0, 'total': 'true', 'limit': 100}
        #payload=encrypted_request(data)
        try:
            r=requests.get(self.base_url, cookies=cookies,timeout=1)
        except requests.exceptions.ReadTimeout:
            print("请求超时")
        else:
            print("请求成功")
        #print(r.status_code)
            self.result=r.json()
            #print(self.result)
        #self.assertEqual=(['alias'],'电影《我和我的祖国》主题曲')
            assert r.status_code == 200
        #self.log.info(u"查询新歌曲成功:%s"%self.result)
        #print(r.elapsed)
        #print(r.elapsed.total_seconds())
        #print(r.elapsed.microseconds)
        self.log.info("-------------end:new_songs----------")

if __name__=='__main__':
    pytest.main(['-s','--reruns','1','test_newsongs.py','--html=report.html','--self-contained-html'])