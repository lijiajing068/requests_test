import hashlib
from django.contrib import auth as django_auth
import base64
import json
from Crypto.Cipher import AES
import binascii
import random
#获取md5码
def get_md5(str):
    md5 = hashlib.md5()
    bytes_utf8 = str.encode(encoding='utf-8')
    md5.update(bytes_utf8)
    str_md5 = md5.hexdigest()
    return str_md5
#用户认证
def user_auth(request):
    get_http_auth=request.META.get('HTTP_AUTHORIZATION',b'')
    auth=get_http_auth.split()
    try:
        auth_parts=base64.b64decode(auth[1]).decode('utf-8').partition(':')
    except IndexError:
        return "null"
    userName,password=auth_parts[0],auth_parts[2]
    user=django_auth.authenticate(username=userName,password=password)
    if user is not None:
        django_auth.login(request,user)
        return "success"
    else:
        return "fail"

#AES加密登录接口请求参数
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = b'0CoJUm6Qyw8W8jud'
pubKey = '010001'
def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    # aes加密需要byte类型
    try:
        text = text.decode()
    except:
        pass

    text = text + pad * chr(pad)
    try:
        text = text.encode()
    except:
        pass

    encryptor = AES.new(secKey, 2, bytes('0102030405060708', 'utf-8'))
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext

def createSecretKey(size):
    #返回密钥
    return bytes(''.join(random.sample('1234567890qwertyuipasdfghjklzxcvbnm', 16)), 'utf-8')

def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    # 3中将字符串转成hex的函数变成了binascii.hexlify, 2中可以直接 str.encode('hex')
    rs = int(binascii.hexlify(text), 16) ** int(pubKey, 16) % int(modulus, 16)

    return format(rs, 'x').zfill(256)
#加密过程
def encrypted_request(text):

    text=json.dumps(text)
    secKey=createSecretKey(16)
    encText=aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
# params加密后是个byte，解下码。
    data = {
        'params': encText.decode(),
        'encSecKey': encSecKey
    }
    return data

def basic_data_headers():
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Host':'music.163.com',
            'Referer':'http://music.163.com',
            'Content-Type':'application/x-www-form-urlencoded'
        }
    return headers

def basic_data_cookies():
    cookies = {
        'appver': '2.1.2.184499',
        'os': 'pc',
        'channel': 'netease',
    }
    return cookies
