# -*-coding:utf-8 -*-
import requests
import json
from stock import Stock
from rule import PriceRule
from define import *
from sendEmail import sendEmail

def value_get(code):
    slice_num, value_num = 21, 3
    name, now = u'——无——', u'  ——无——'
    if code in ['s_sh000001', 's_sz399001']:
        slice_num = 23
        value_num = 1
    r = requests.get("http://hq.sinajs.cn/list=%s" % (code,))
    res = r.text.split(',')
    print(json.dumps(res))
    if len(res) > 1:
        name, now = res[0][slice_num:], res[value_num]
    return name + ' ' + now


if(__name__=='__main__'):
    stock = Stock('ST慧业', 'sz000816')
    rule = PriceRule(1.1, 1.0)
    ret = stock.fitPrice(rule)
    if(ret['code'] == CODE_SEND_EMAIL):
        sendEmail(ret['msg'], 'aaaaa')
    print(ret)
