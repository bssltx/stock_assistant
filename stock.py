# -*-coding:utf-8 -*-

import requests
import json
from sendEmail import errorEmail
from define import *

class Stock:
    def __init__(self,name,code):
        self.name = name
        self.code = code


    def __getPrice(self):
        slice_num, value_num = 21, 3
        name, now = u'——无——', u'  ——无——'
        if self.code in ['s_sh000001', 's_sz399001']:
            slice_num = 23
            value_num = 1
        r = requests.get("http://hq.sinajs.cn/list=%s" % (self.code,))
        res = r.text.split(',')
        print(json.dumps(res))
        if len(res) > 1:
            name, now = res[0][slice_num:], res[value_num]
        return name, float(now)

    def fitPrice(self, rule):
        name,price = self.__getPrice()
        if(name!=self.name):
            msg = '股票名字不符，code: %s, local_name: %s, name: %s 。' % (self.code, self.name, name.encode('utf-8'))
            errorEmail(msg)
            print(msg)
        else:
            print('name ok!')
        if(rule.high_threshold and price > rule.high_threshold):
            return {'code': CODE_SEND_EMAIL, 'msg': '高价提醒'}
        elif(rule.low_threshold and price < rule.low_threshold):
            return {'code': CODE_SEND_EMAIL, 'msg': '低价提醒'}
        else:
            return {'code': CODE_NOT_SEND_EMAIL, 'msg': '无提醒'}


