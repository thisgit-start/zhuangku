# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/29 下午5:40
@Auth ： wangzhanjun

"""
import requests
import datetime
from zk import hedan, checkOrder

# 获取当前日期和时间
now = datetime.datetime.now()


# 将日期和时间格式化为字符串


def recheck(orderIdList):
    url = 'http://testonline.zk-house.com/api/cms/suitOrderVerification/moreVouching'
    headers = {
        'Token': 'e8cc7433707458f02b121fad2a6daabd'
    }

    for i in orderIdList:
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "orderId": i,
            "reasonText": "重新核单备注{}".format(str(formatted_time)),
            "reasonUrl": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/order/remark/1688031514296.jpeg"
        }
        res = requests.post(url=url, headers=headers, json=data)
        msg = res.json()['msg']
        print('订单ID：{}  重新核销 {}'.format(str(i), msg))


def vouching(orderIdList):
    # 核单

    # 项目批次set
    purchaseBatch = 5
    for i in orderIdList:
        hedan.saveOrderDeliveryTime(i, purchaseBatch)
        token = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2ODk4MzQ4OTAsInVzZXJJZCI6MTA2ODAzLCJpYXQiOjE2ODcxNTY0OTB9.SgGTLoayh5MHJqPTmcluOXZbkrgtrNha52rEhNGhQi6CGRGYbfhBX7yHkw81XYCJTnZZXJudAyHI0Go5Z9o8cA'

        orderVerificationId = checkOrder.getOrderVerificationId(i, token)
        checkOrder.confirmOrderGoods(i, orderVerificationId)


if __name__ == '__main__':
    orderIdList = ['106668']
    # 批量重新核单
    # recheck(orderIdList)

    # 批量核单
    vouching(orderIdList)
