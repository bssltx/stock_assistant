# -*-coding:utf-8 -*-
import requests
import json
from stock import Stock
from rule import PriceRule
from define import *
from sendEmail import sendEmail
import time

rules = [
    ['博通集成', 'sh603068', 140, 102],  #高价出手
    ['湖南黄金', 'sz002155', 8.5, 7.0],
    ['科技ETF', 'sh515000', 1.58, 1.2],
    ['欧菲光', 'sz002456', 19, 15],
    ['100红利', 'sh515180', 1.2, 0.93],
    ['贝瑞基因', 'sz000710',42, 39.3],
    ['半导体', 'sh512480', 2.26, 1.6],
    ['金发科技', 'sh600143', 9.6, 8],
    ['药明康德', 'sh603259', 120, 93],
    ['格力电器', 'sz000651', 70, 49],
    ['5GETF', 'sh515050', 1.4, 1.0],
    ['西安旅游', 'sz000610', 9.9, 7.5],
    ['沃特股份', 'sz002886', 26, 21],
    ['民生银行', 'sh600016', 6.38, 5.8],
    ['建投能源', 'sz000600', 5.0, 4.0],
    ['长电科技', 'sh600584', 35, 23],
    # ['大华股份'],
    # ['京东方'],
    # ['伟星新材']
]

def check():
    for rule in rules:
        stock = Stock(rule[0], rule[1])
        rule = PriceRule(rule[2], rule[3])
        ret = stock.fitPrice(rule)
        if (ret['code'] == CODE_SEND_EMAIL):
            sendEmail(ret['msg'], 'aaaaa')
        print(json.dumps(ret, ensure_ascii=False))

if(__name__=='__main__'):
    while(True):
        check()
        # break
        time.sleep(300)




