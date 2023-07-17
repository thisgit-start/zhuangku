import json
import time

import requests


class zk():
    def __init__(self, order):
        self.token = '8d7fa6693137ec1ed11368e369c0464e'
        self.order = order
        self.nowtime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    def determine(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token
        }
        body = {"t": 1664244449235, "orderAmount": 20000,
                "payAmount": "11111", "exchange": 0, "quickPay": 1,
                "suitStatus": 6, "id": self.order,
                "paidTime": self.nowtime}
        url = 'http://testonline.zk-house.com/api/cms/jjyl/order/updateSuitOrderInfo'
        res = requests.post(url=url, headers=headers, json=body).text
        return res

    def dsrw(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token
        }
        body = {
            "param": {"id": 1}
        }
        url = 'http://123.57.50.102:8408/order/enterpriseAwardToPerson'
        res = requests.post(url=url, headers=headers,json=body).text
        print(res)


if __name__ == '__main__':
    # a = zk(104792).determine()
    b = zk(123).dsrw()

