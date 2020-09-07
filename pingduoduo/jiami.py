import json
import time
import requests
import hashlib
access_token = 'b544694546234ae29fe56b1e9d5841879510862e'
client_id = "d5b6073a78cb40c99205bb870c5e3873"
client_secret = "bcd9dbe56a5a6d498ab80f9372a664fdae47f03a"

url = "https://gw-api.pinduoduo.com/api/router"

def sign(client_secret,data):
    text = ""
    for i in sorted(data.items()):
        text += i[0] + i[1]
    text = client_secret + text + client_secret
    hmd5 = hashlib.md5()
    hmd5.update(text.encode("utf-8"))
    sig = hmd5.hexdigest()
    data["sign"] = sig.upper()
    return data


#获取所有待发货且无售后或售后关闭的订单。
def order_number_list():
    headers = {
        'content-type': "application/x-www-form-urlencoded"
    }

    data = {
        "timestamp": "{}".format(int(time.time())),
        "access_token": access_token,
        "data_type": "JSON",
        "client_id": client_id,
        # "type": "pdd.order.number.list.get"
        # "page": "1",
        # "order_status": "1",
        "type": "pdd.goods.list.get",
        "goods_name":"爸爸装"
        #"type": "pdd.goods.detail.get",
        #"type": "pdd.goods.commit.list.get",
        #"check_status":"2",
        #"page":"2",
        #"page_size":"10"
        #"type": "pdd.goods.quantity.update",
        #"goods_id": "44622906858",
        #"quantity": "221981"
        #"type": "pdd.order.number.list.increment.get",
        #"is_lucky_flag":"0",
        #"order_status":"1",
        #"start_updated_at":"1578545130",
        #"end_updated_at":"1578545850",
        #"page":"2",
        #"refund_status":"5"
        #"type": "pdd.order.list.get",
        # "order_status":"1",
        # "start_confirm_at":"1578545130",
        # "end_confirm_at":"1578545850",
        # "page":"2",
        # "refund_status":"5",
        # "page_size":"3"
        #"type": "pdd.order.information.get",
        #"order_sn":"200109-063816663853129"
        # "type": "pdd.goods.add",
        # "carousel_gallery":"['https://www.baidu.com/img/bd_logo1.png']",
        # "cat_id":"0",
        # "cost_template_id":"0",
        # "country_id":"0",
        # "detail_gallery":"['https://www.baidu.com/img/bd_logo1.png']",
        # "goods_desc":"独立小包装",
        # "goods_name":"大白兔奶糖",
        # "goods_type":"1",
        # "is_folt":"true",
        # "is_pre_sale":"false",
        # "is_refundable":"true",
        # "market_price":"2345",
        # "second_hand":"false",
        # "shipment_limit_second":"86400",
        # "sku_list":"[{'is_onsale': 1, 'limit_quantity': 999, 'price': '2200', 'weight': 1000, 'multi_price': '1900', 'thumb_url': 'http://t06img.yangkeduo.com/images/2018-04-15/ced035033b5d40b589140af882621c03.jpg', 'out_sku_sn': 'L', 'quantity': 100, 'spec_id_list': '[25]', 'oversea_sku': { 'measurement_code': '计量单位编码', 'taxation': '税费', 'specifications': '规格' }]"
    }
    dat = sign(client_secret, data)
    print(dat)
    B=(requests.post(url, data=dat, headers=headers).text)
    #A=(requests.post(url, data=dat, headers=headers).text)

order_number_list()
