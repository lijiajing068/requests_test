import unittest
import requests
import re
from collections import namedtuple

class return_sings_lists():
    def setUp(self,songId):
        songId='210042'
        self.base_url='http://music.163.com/song?id={}'.format(songId)

    def tearDown(self):
        print(self.payload)

    def test_return_singslists(self):
        songId='210042'
        r=requests.get(self.base_url,params=songId)
        containedUl=re.findall(r'<ul class="m-rctlist f-cb">[.\s\S]+?</url>',r.text)
        if not containedUl:
            containedUl=''
        else:
            containedUl=containedUl[0]
        self.payload=set(re.findall(r'data-res-id="(.+)"',containedUl))
        return self.payload

#if __name__=='__main__':
    #unittest.main()
