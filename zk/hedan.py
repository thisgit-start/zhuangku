# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/27 上午10:14
@Auth ： wangzhanjun

"""
import requests
import datetime
from zk import createOrder, writetxt, checkOrder, random_phone, name
import datetime
import time

# 获取当前日期和时间
now = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

timeStamp = int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000.0)

# print(formatted_time)
backstageToken = '0e4b74422dd213020396e6fc7763efd1'


# 批次
def setpurchaseBatch(orderId, purchaseBatch):
    url = 'http://testonline.zk-house.com/api/cms/suitOrderVerification/vouching'

    headers = {
        "Token": backstageToken
    }
    data = {"orderId": orderId, "purchaseBatch": purchaseBatch}
    res = requests.post(url=url, headers=headers, json=data)
    print(res.json())
    return res.json()


# 核单
def suitOrderVerification(orderId):
    url = 'http://testonline.zk-house.com/api/cms/suitOrderVerification/notice'

    headers = {
        "Token": backstageToken
    }
    data = {"orderId": orderId}
    res = requests.post(url=url, headers=headers, json=data)
    # print(res.json())
    return res.json()


# 集中交付
def CentralizedDelivery(orderId, purchaseBatch):
    # 集中交付

    # 批次code
    setpurchaseBatchCode = setpurchaseBatch(orderId, purchaseBatch)["code"]
    # 核单code
    suitOrderVerificationCode = suitOrderVerification(orderId)['code']
    if (setpurchaseBatchCode == 0 and suitOrderVerificationCode == 0):
        # or (setpurchaseBatchCode == 0 and suitOrderVerificationCode == 43101):
        print("集中 后台核单完成，待业主确认")
    else:
        # print(setpurchaseBatch(), suitOrderVerification())
        print("核单失败", '\n', "*" * 100)


# 灵活交付设置交付时间
def saveOrderDeliveryTime(orderId, purchaseBatch):
    # 批次code
    setpurchaseBatchCode = setpurchaseBatch(orderId, purchaseBatch)["code"]
    # 核单code
    suitOrderVerificationCode = suitOrderVerification(orderId)['code']

    if setpurchaseBatchCode == 0 and suitOrderVerificationCode == 0:
        print("灵活交付核单完成，后续需要设置交付时间")
    else:
        print(setpurchaseBatch(orderId, purchaseBatch), '设置批次', "\n", suitOrderVerification(orderId), "\n", "*" * 100)
    url = "http://testonline.zk-house.com/api/cms/suitOrderVerification/saveOrderDeliveryTime"
    headers = {
        "Token": backstageToken
    }
    dataList = [
        {"orderId": orderId, "whether": "", "type": 10, "expectTime": "2023-07-30 00:00:00",
         "remark": "主材备注生成时间-{}".format(formatted_time), "deliverStatus": 1},
        {"orderId": orderId, "whether": "1", "type": "20", "expectTime": "2023-09-01 00:00:00",
         "remark": "家具备注生成时间-{}".format(formatted_time), "deliverStatus": 1},
        {"orderId": orderId, "whether": "1", "type": "30", "expectTime": "2023-10-01 00:00:00",
         "remark": "家电备注生成时间-{}".format(formatted_time), "deliverStatus": 1}

    ]
    for i in range(len(dataList)):
        res = requests.post(url=url, headers=headers, json=dataList[i])
        if res.json()['code'] == 0:
            if i == 0:
                print("主材交付时间设置完成")
            elif i == 1:
                print("家具交付时间设置完成")
            elif i == 2:
                print("家电交付时间设置完成")
        else:
            print(i, "交付时间设置失败")
            print(res.json())
    # 商品备注
    setGoodsRemark(orderId)
    # 订单备注
    orderRemark(orderId)
    updateDelivery(orderId)


# 核单详情信息
def getSuitCheckOrderInfo(orderId):
    '''
    :return: 核单详情
    '''
    try:
        url = "http://testonline.zk-house.com/api/cms/jjyl/order/getSuitCheckOrderInfo"
        headers = {
            "Token": backstageToken
        }
        data = {"id": orderId}
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())

        return res.json()
    except Exception as e:
        return None


# 设置商品备注
def setGoodsRemark(orderId):
    '''
    设置商品备注
    :return:
    '''
    # 获取订单核单详情
    OrderInfo = getSuitCheckOrderInfo(orderId)
    if OrderInfo != None:
        # 区域List
        groups = OrderInfo['data']['groups']
        # 区域下list
        groupList = []
        # 区域下商品list
        suitGoods = []
        # 商品ID list
        IDList = []
        for i in range(len(groups)):
            groupList.append(groups[i]['groupList'])
        # print(groupList, '区域下list')

        for i in range(len(groupList)):
            for j in range(len(groupList[i])):
                suitGoods.append(groupList[i][j]['suitGoods'])
        # print(suitGoods, '区域下商品list')

        for i in range(len(suitGoods)):
            for j in range(len(suitGoods[i])):
                IDList.append(suitGoods[i][j]['id'])
        # print(IDList)

        url = "http://testonline.zk-house.com/api/cms/jjyl/order/updateGoodsRemark"
        headers = {
            "Token": backstageToken
        }
        for i in IDList:
            # 当前时间
            # formatted_time
            remark = '-好多个商品'
            data = {"t": timeStamp, "remark": " 这是商品备注{} ".format(remark), "id": i}
            res = requests.post(url=url, headers=headers, json=data)
        print('商品备注设置成功')
    else:
        print('获取核单详情失败')


# 设置订单备注
def orderRemark(orderId):
    url = 'http://testonline.zk-house.com/api/cms/sys/note/record/add'
    headers = {
        "Token": backstageToken
    }
    # 当前时间 formatted_time
    data = {
        "recordId": orderId,
        "content": "订单的备注{}{}".format(str(orderId), "  "),
        "recordType": 1,
        "url": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/order/remark/1688554013641.jpeg"
    }
    res = requests.post(url=url, headers=headers, json=data)

    try:
        if res.json()['code'] == 0:
            print('订单备注添加成功')
    except Exception as e:
        print(url, '请求可能有问题')


# 设置其他联系人
def updateDelivery(orderId):
    '''
    核单设置其他联系人
    :param orderId: 订单ID
    :return:
    '''
    details = getSuitCheckOrderInfo(orderId)
    ownerName = details['data']['suitOrder']['ownerName']
    ownerPhone = details['data']['suitOrder']['ownerPhone']
    identityCard = details['data']['suitOrder']['identityCard']
    buildingNumber = details['data']['suitOrder']['buildingNumber']
    id = details['data']['suitOrder']['id']
    projectId = details['data']['suitOrder']['projectId']
    address = details['data']['suitOrder']['suitOrderExt']['address']
    print(ownerName, ownerPhone, identityCard, buildingNumber, id, projectId, address)
    url = 'http://testonline.zk-house.com/api/cms/suitOrder/updateDelivery'

    data = {
        "ownerName": ownerName,
        "ownerPhone": ownerPhone,
        "identityCard": identityCard,
        "buildingNumber": buildingNumber,
        "id": id,
        "projectId": projectId,
        "address": address,
        "otherContactItemVoList": [{
            "otherName": name.random_name(),
            "otherPhone": random_phone.create_phone()
        }, {
            "otherName": name.random_name(),
            "otherPhone": random_phone.create_phone()
        }],
        "entranceSource": 1
    }
    headers = {
        "Token": backstageToken
    }

    res = requests.post(url=url, json=data, headers=headers)

    print(res.json())


if __name__ == '__main__':
    # 交付方式 集中交付0   灵活交付1
    quickPay = 1
    orderId = createOrder.createOrder(quickPay)

    # 订单ID
    # orderId = 106612

    # 项目批次set
    purchaseBatch = 2
    writetxt.writeTxt("   批次：{} {} {}  ".format(purchaseBatch, "\n", "-" * 100))
    # 灵活
    saveOrderDeliveryTime(orderId, purchaseBatch)

    token = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2ODk4MzQ4OTAsInVzZXJJZCI6MTA2ODAzLCJpYXQiOjE2ODcxNTY0OTB9.SgGTLoayh5MHJqPTmcluOXZbkrgtrNha52rEhNGhQi6CGRGYbfhBX7yHkw81XYCJTnZZXJudAyHI0Go5Z9o8cA'

    orderVerificationId = checkOrder.getOrderVerificationId(orderId, token)
    checkOrder.confirmOrderGoods(orderId, orderVerificationId)

# phoenList = ['13521932982','18888802777','15201099888','13521669731',]
