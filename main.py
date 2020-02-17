# -*-coding:utf-8 -*-
import requests
import json
from stock import Stock
from rule import PriceRule
from define import *
from sendEmail import sendEmail
import time

rules = [
    ['博通集成', 'sh603068', 120, 102],
    ['湖南黄金', 'sz002155', 8, 7.0],
    ['科技ETF', 'sh515000', 1.5, 1.2],
    ['欧菲光', 'sz002456', 18.6, 15],
    ['100红利', 'sh515180', 1.2, 0.93],
    ['贝瑞基因', 'sz000710',42, 39.3],
    ['半导体', 'sh512480', 2.26, 1.6],
    ['金发科技', 'sh600143', 9.6, 8],
]

def check():
    for rule in rules:
        stock = Stock(rule[0], rule[1])
        rule = PriceRule(rule[2], rule[3])
        ret = stock.fitPrice(rule)
        if (ret['code'] == CODE_SEND_EMAIL):
            sendEmail(ret['msg'], 'aaaaa')
        print(ret)

if(__name__=='__main__'):
    while(True):
        check()
        # break
        time.sleep(300)




