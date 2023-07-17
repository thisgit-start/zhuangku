# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/27 下午4:07
@Auth ： wangzhanjun

"""
import requests
from zk import name, writetxt
from zk import jsondata
import random
import datetime
import time

import json

timeStamp = int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000.0)

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2ODk4MzQ4OTAsInVzZXJJZCI6MTA2ODAzLCJpYXQiOjE2ODcxNTY0OTB9.SgGTLoayh5MHJqPTmcluOXZbkrgtrNha52rEhNGhQi6CGRGYbfhBX7yHkw81XYCJTnZZXJudAyHI0Go5Z9o8cA'


# print("当前13位时间戳为：", timeStamp)
def createOrder(quickPay):
    phoneList = ['13521505782', '13521671973', '13521673937', '13521669731', '13552785162', '17610966911',
                 '17611599033',
                 '19231299633', '17501133255', '15600693579', '17611688011', '17610966255']

    ownerName = name.random_name()
    # ownerPhone = random.choice(phoneList)
    ownerPhone = 18401189610

    url = 'https://testonline.zk-house.com/api/giftbag/order/createOrder'

    headers = {
        'token': token
    }
    # 交付方式   集中0    灵活1
    quickPay = quickPay
    # 订单金额
    # orderAmount = None
    if quickPay == 0:
        orderAmount = 0.01
    elif quickPay == 1:
        orderAmount = 0.02

    data = {
        "suitGoods": [{
            "id": 474900,
            "suitId": 11046,
            "groupId": 101054,
            "goodsId": 16882,
            "goodsName": "白聚晶抛光砖",
            "goodsNum": 2,
            "isCheck": 0,
            "brandName": "瓷砖品牌",
            "brandId": "",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1687772320799.png",
            "marque": "pl001",
            "goodsSize": "320*550",
            "remark": "白聚晶抛光砖 棒",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "p123",
            "purchasePrice": 50,
            "marketPrice": 80,
            "showPrice": '',
            "settlementPrice": 60,
            "sortNo": 1,
            "categoryIdFirst": "1400",
            "categoryIdSecound": "1401",
            "categoryIdThird": "e",
            "goodsUnit": "片",
            "sceneImg": '',
            "color": '',
            "goodSceneImg": "",
            "original": 0,
            "makeUpPrices": 0,
            "labelType": 0,
            "specialType": 0
        }, {
            "id": 474901,
            "suitId": 11046,
            "groupId": 101055,
            "goodsId": 16883,
            "goodsName": "制单-沙发",
            "goodsNum": 3,
            "isCheck": 0,
            "brandName": "欧琳",
            "brandId": '',
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1687772502709.png",
            "marque": "sf560",
            "goodsSize": "5000*2000",
            "remark": "沙发 棒",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": '',
            "stockCode": "sf001",
            "purchasePrice": 1000,
            "marketPrice": 2000,
            "showPrice": '',
            "settlementPrice": 1100,
            "sortNo": 1,
            "categoryIdFirst": "0400",
            "categoryIdSecound": "0405",
            "categoryIdThird": "a",
            "goodsUnit": "个",
            "sceneImg": '',
            "color": '',
            "goodSceneImg": "",
            "original": 0,
            "makeUpPrices": 0,
            "labelType": 0,
            "active": 1,
            "specialType": 0
        }, {
            "id": 474902,
            "suitId": 11046,
            "groupId": 101056,
            "goodsId": 16885,
            "goodsName": "制单-卫浴-主柜",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "稚木青禾",
            "brandId": '',
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1687772867520.png",
            "marque": "weiyu321231",
            "goodsSize": "1000*800",
            "remark": "卫浴-主柜  棒",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": '',
            "stockCode": "zhugui001",
            "purchasePrice": 2000,
            "marketPrice": 3000,
            "showPrice": '',
            "settlementPrice": 2200,
            "sortNo": 1,
            "categoryIdFirst": "2100",
            "categoryIdSecound": "2111",
            "categoryIdThird": "h",
            "goodsUnit": "个",
            "sceneImg": '',
            "color": '',
            "goodSceneImg": "",
            "original": 0,
            "makeUpPrices": 0,
            "labelType": 0,
            "specialType": 0
        }, {
            "id": 474903,
            "suitId": 11046,
            "groupId": 101057,
            "goodsId": 16884,
            "goodsName": "制单-超薄电视",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "小米",
            "brandId": '',
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1687772715823.png",
            "marque": "dianshi5646",
            "goodsSize": "1200*800",
            "remark": "超薄电视   棒",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": '',
            "stockCode": "dianshi001",
            "purchasePrice": 6000,
            "marketPrice": 9000,
            "showPrice": '',
            "settlementPrice": 7000,
            "sortNo": 1,
            "categoryIdFirst": "4400",
            "categoryIdSecound": "4901",
            "categoryIdThird": "b",
            "goodsUnit": "台",
            "sceneImg": '',
            "color": '',
            "goodSceneImg": "",
            "original": 0,
            "makeUpPrices": 0,
            "labelType": 0,
            "specialType": 0
        }, {
            "id": 474904,
            "suitId": 11046,
            "groupId": 101058,
            "goodsId": 16886,
            "goodsName": "制单-小家电-生活小家电-电饭煲",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "电器品牌",
            "brandId": '',
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1687773016910.png",
            "marque": "dian124",
            "goodsSize": "300*500",
            "remark": "电饭煲 棒",
            "defaultCheck": 0,
            "requiredStatus": 0,
            "codeUrl": '',
            "stockCode": "dianfanbao002",
            "purchasePrice": 600,
            "marketPrice": 800,
            "showPrice": '',
            "settlementPrice": 700,
            "sortNo": 1,
            "categoryIdFirst": "2100",
            "categoryIdSecound": "2111",
            "categoryIdThird": "h",
            "goodsUnit": "台",
            "sceneImg": '',
            "color": '',
            "goodSceneImg": "",
            "original": 0,
            "makeUpPrices": 0,
            "labelType": 0,
            "specialType": 0
        }],
        "suitOrder": {
            "adviserId": "",
            "adviserName": "",
            "buildingNumber": "1231",
            "verificationCode": "564577",
            "exchange": 0,
            "houseId": "3588",
            "identityCard": "110100201712268892",
            "ownerName": ownerName,
            "ownerPhone": "18401189610",
            "projectId": "2318",
            "quickPay": quickPay,
            "signUrl": "",
            "suitId": 11046,
            # "orderAmount": orderAmount
            "orderAmount": orderAmount
        },
        "timeStamp": 1687864708245,
        "sign": "bde8db67a9b9259d14d2e1214fccb2c2",
        "appId": "wx1b208577709ac6b2",
        "openId": "ogmax5NscpPGoBuGhUSprfPHuDAI"
    }

    # res = requests.post(url=url, headers=headers,json=data)
    res = requests.post(url=url, headers=headers,
                        json=jsondata.createOrderData_xiangshan_zhidanyouhuaB1(ownerName, quickPay, orderAmount, ownerPhone)
                        # json=data
                        )
    orderID = res.json()['data']
    print(res, res.json())
    details = detail(orderID, token)
    print('details', details)
    writetxt.writeTxt(str(
        "订单ID：{}  姓名：{}  手机号：{}  交付方式：{}  订单编号：{}  礼包：{}  项目：{}  ".format(orderID, ownerName, ownerPhone, details[2],
                                                                          details[0], details[1], details[3])))
    return orderID


def detail(orderId, token):
    url = "https://testonline.zk-house.com/api/giftbag//order/getOrderDetail"
    headers = {
        'token': token
    }
    data = {"orderId": orderId}
    res = requests.post(url=url, headers=headers, json=data)
    resdetail = res.json()
    orderCode, suitName, quickPayName, projectName = resdetail['data']['orderCode'], resdetail['data']['suitName'], \
                                                     resdetail['data']['quickPayName'], resdetail['data']['projectName']
    return orderCode, suitName, quickPayName, projectName
    pass


if __name__ == '__main__':
    # 交付方式 集中交付0   灵活交付1
    quickPay = 0
    createOrder(quickPay)
