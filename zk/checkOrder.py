# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/29 上午11:51
@Auth ： wangzhanjun
确认核单
"""
import requests

# 核单详情获取 orderVerificationId
token = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2ODk4MzQ4OTAsInVzZXJJZCI6MTA2ODAzLCJpYXQiOjE2ODcxNTY0OTB9.SgGTLoayh5MHJqPTmcluOXZbkrgtrNha52rEhNGhQi6CGRGYbfhBX7yHkw81XYCJTnZZXJudAyHI0Go5Z9o8cA'


# 小程序确认核单

def getOrderVerificationId(suitOrderId, token):
    '''

    :param suitOrderId: 订单ID
    :param token:
    :return:
    '''
    url = "https://testonline.zk-house.com/api/giftbag/order/checkOrderDetail"
    headers = {
        "token": token
    }
    data = {"suitOrderId": suitOrderId}
    try:
        res = requests.post(url=url, headers=headers, json=data)
        try:
            orderVerificationId = res.json()['data']['orderVerificationId']
        except Exception as e:
            print("错误信息", e)
    except:
        print("获取orderVerificationId的接口请求错误")
    return orderVerificationId


def confirmOrderGoods(suitOrderId, orderVerificationId):
    '''
    :param suitOrderId: 订单ID
    :param orderVerificationId: 核单ID
    :return:
    '''
    url = 'https://testonline.zk-house.com/api/giftbag/order/confirmOrderGoods'
    headers = {
        "token": token
    }
    data = {"suitOrderId": suitOrderId, "orderVerificationId": orderVerificationId}
    res = requests.post(url=url, headers=headers, json=data)
    if res.json()['message'] == "成功":
        print("小程序核单确定完成")
    else:
        print("看看啥原因", res.json())


if __name__ == '__main__':
    token = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2ODk4MzQ4OTAsInVzZXJJZCI6MTA2ODAzLCJpYXQiOjE2ODcxNTY0OTB9.SgGTLoayh5MHJqPTmcluOXZbkrgtrNha52rEhNGhQi6CGRGYbfhBX7yHkw81XYCJTnZZXJudAyHI0Go5Z9o8cA'
    suitOrderId = '106602'
    orderVerificationId = getOrderVerificationId(suitOrderId, token)
    confirmOrderGoods(suitOrderId, orderVerificationId)
