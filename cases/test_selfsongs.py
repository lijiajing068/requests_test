import pytest
import requests
import pytest_html
from selenium import webdriver
from test_login import TestLogin
from common.common import get_md5,encrypted_request,basic_data_headers
class TestSelf():
    def test_select_songs(self):
        id = TestLogin.test_login_success(self)
        base_url = "http://music.163.com/weapi/user/playlist"
        data = {'offset': 0, 'uid': id, 'limit': 1000, 'csrf_token': ''}
        payload = encrypted_request(data)
        r = requests.post(base_url, data=payload, headers=basic_data_headers())
        self.result = r.json()
        assert r.status_code == 200
if __name__ == '__main__':
    pytest.main(["-s",'test_selfsongs.py'])
