##!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import json
import time
import base64
import hmac, hashlib

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIMESTAMP= "%Y%m%d%H%M%S"
CON_KEY = ""
SECRET_KEY = ""


base_url = 'https://api.bithumb.com/'
sub_url = 'public/orderbook/'
cs_url = 'https://api.bithumb.com/public/ticker/ALL'

#r = requests.get(cs_url)
#result = r.json()
#print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ':')))
'''
cur_timestamp = float(result["data"]["date")/1000
print("Current time stamp: " + str(cur_timestamp))
print("ETH Average Price: " + result["data"]["ETH"]["average_price"])
cur_struct_time = time.localtime(cur_timestamp)
print("Current time: " + time.strftime(TIME_FORMAT, cur_struct_time))
print(r.status_code)
'''
#时间转换: 时间戳-->格式化字符串
def timestamp_to_str(sTimestamp):
    #timestamp: 13位数字字符串
    real_timestamp = float(sTimestamp)/1000
    struct_time = time.localtime(real_timestamp)
    time_str = time.strftime(TIME_FORMAT, struct_time)
    return time_str

#print('Current time: ' + timestamp_to_str(result["data"]["date"]))

#Parameter: sCurrency 要查询的虚拟货币
# Return: dist{} 当前市场最优买卖价 
def cur_best_price(sCurrency):
    r = requests.get(base_url + sub_url + sCurrency)
    data = r.json()['data']
    timestamp = data['timestamp']
    cur_time = timestamp_to_str(timestamp)
    payment_currency = data['payment_currency']
    bids_price_list = []
    asks_price_list = []
    bids = data['bids']
    asks = data['asks']    
    for item in bids:
        bids_price_list.append(item['price'])
    bids_best_price = max(bids_price_list)  #市场最高购买请求价
    for item in asks:
        asks_price_list.append(item['price'])
    asks_best_price = min(asks_price_list)  #市场最低出售请求价

    return {'cur_time': cur_time, 'payment_currency': payment_currency, 'bids_best_price': bids_best_price, 'asks_best_price': asks_best_price}


if __name__ == '__main__':
    print(cur_best_price('ETH'))
