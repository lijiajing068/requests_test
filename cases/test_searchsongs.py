import pytest
import requests
from common.common import encrypted_request
from common.logger import Log
import pandas as pd
import json
class TestSearch():
    log = Log()
    def setup_class(self):
        data = pd.read_csv("D:\Python\Scripts\lvmama\cases\login_data.csv", encoding='gb18030')
        df = pd.DataFrame(data)
        self.songs=df['songs']
        self.respect=df['respect']
        self.actural=df['actural']

    def test_searchsongs01(self):
        #s是需要搜索的关键字
        base_url = "http://music.163.com/weapi/cloudsearch/get/web"
        self.log.info("-------------start:search_songs----------")
        data = {
            's':self.songs[0],
            'offset': 0,
            'limit': 100,
            'type': 10
        }
        payload=encrypted_request(data)
        r=requests.post(base_url,data=payload)
        self.result=r.json()
        assert r.status_code == self.respect[0]
        #self.log.info(u"查询成功: %s"%self.result["code"])
        self.log.info("-------------end:search_songs----------")
        #return(self.result['result']['albums'][2]['id'])
    def test_searchsongs2(self):
        #@pytest.mark.skip(reason="no way of currently testing this")
        self.base_url = "http://music.163.com/weapi/cloudsearch/get/web"
        self.log.info("-------------start:search_songs02----------")
        data = {
            's':self.songs[1],
            'offset': 0,
            'limit': 100,
            'type': 10
        }
        payload = encrypted_request(data)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        assert r.status_code == self.respect[1]
        #self.log.info(u"查询成功: %s" % self.result["code"])
        self.log.info("-------------end:search_songs----------")
if __name__=='__main__':
    pytest.main(['-s',"test_searchsongs.py",'--html=../report/report-songs02.html'])