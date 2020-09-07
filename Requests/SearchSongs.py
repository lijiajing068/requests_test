
from common.HttpRequest import NetEaseWebApi

def search(self, s, offset=0, limit=100, stype=1):

    # url = 'http://music.163.com/api/search/get/web'
    url = 'http://music.163.com/weapi/cloudsearch/get/web'
    data = {
        's': s,
        'offset': str(offset),
        'limit': str(limit),
        'type': str(stype)
    }
    self.httprequest = NetEaseWebApi.httpRequest(self)
    html = self.httprequest(url, method='POST', data=data)
    try:
        return html['result']
    except:
        return {'songCount': 0, 'songs': []}

if __name__ == '__main__':
    print(search(self,"蔡依林"))