#encoding=utf-8
import re
import json
import logging
import urllib.parse
import sys
import io
from collections import namedtuple

from common.RequestFen import HttpRequest, ignored
from common.common import encrypted_request, hashlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
logger = logging.getLogger(__name__)

SongInfo = namedtuple(
    'SongInfo', ['music_id', 'url', 'author', 'time', 'name', 'music_img', 'lyric'])


class NetEaseWebApi(HttpRequest):

    cookies = {
        'appver': '2.1.2.184499',
        'os': 'pc',
        'channel': 'netease',
    }


    default_timeout = 10


    def __init__(self):
        super(NetEaseWebApi, self).__init__()
        self.headers['Host'] = 'music.163.com'
        self.headers['Referer'] = 'http://music.163.com'
        self.headers['Content-Type'] = 'application/x-www-form-urlencoded'

        self.vertifyHeaders = self.headers.copy()
        self.vertifyHeaders['Host'] = 'ac.dun.163yun.com'
        self.vertifyHeaders['Accept'] = 'image/png,image/*;q=0.8,*/*;q=0.5'
        self.vertifyHeaders['Content-Type'] = ''

        self.urlEamilHeaders = self.headers.copy()
        self.urlEamilHeaders['Referer'] = ''
        self.urlEamilHeaders['Origin'] = 'orpheus://orpheus'


    def httpRequest(self, *args, **kwargs):
        data = kwargs.get('data')

        if data:
            kwargs['data'] = encrypted_request(data)

        logger.info("进行网易云Url请求, args: {0}, kwargs: {1}".format(args, kwargs))
        html = super(NetEaseWebApi, self).httpRequest(*args, **kwargs)

        with ignored():
            return json.loads(html.text)

        logger.info("url: {0} 请求失败. Header: {1}".format(
            args[0], kwargs.get('headers')))
        return False