# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/7 下午5:02
@Auth ： wangzhanjun

"""
import requests

import random

url = 'http://testonline.zk-house.com/api/cms/releaseGoods/spuSaveOrUpdate'
headers = {
    'Token': '2054130517a702113252e020a3f6ea4e'
}
random_number = random.randint(100, 9999)
print(random_number)


# 主材 - 墙地饰材>瓷砖>抛光砖 品牌：稚木青禾
def crateGoods_a():
    '''
     主材 - 墙地饰材>瓷砖>抛光砖 品牌：稚木青禾
    :return:
    '''

    stockCode = 'b' + str(random.randint(100, 9999))
    # 销售属性
    valueName = 'xs' + str(random.randint(100, 9999))
    # 商品型号
    marque = 'sp' + str(random.randint(100, 9999))
    # 市场价
    customerPrice = random.randint(100, 999)
    # 会员价
    memberPrice = random.randint(100, 999)
    # 结算价
    settlementPrice = random.randint(100, 999)
    # 含税采购价
    salePrice = random.randint(100, 999)
    # 规格名称
    attributeName = 'gg' + str(random.randint(100, 999))
    # 规格值
    attributeValue = 'ggz' + str(random.randint(100, 999))
    data = {
        "t": 1689132086933,
        "goodsName": "地砖800*800",
        "categoryIdThird": "e",
        "categoryIdFirst": "1400",
        "categoryIdSecound": "1401",
        "saleAttributeStatus": 1,
        "checkedAttributeList": [],
        "saleAttributeList": [{
            "isImage": "false",
            "attributeName": "001",
            "id": 0.2147544274635289,
            "attributeValueList": [{
                "valueName": valueName,
                "id": 0.04994170765193151
            }]
        }],
        "categoryIdZero": "10",
        "info": "",
        "brandId": 189,
        "brandName": "稚木青禾",
        "orderingCycle": "22",
        "factoryId": 117,
        "factoryName": "咖啡工厂",
        "goodsSkuList": [{
            "saleAttributes": [{
                "attributeName": attributeName,
                "attributeValue": attributeValue
            }],
            "brandId": 189,
            "goodsName": "地砖800*800",
            "factoryId": 117,
            "orderingCycle": "22",
            "id": 0.5255212693521087,
            "categoryIdThird": "e",
            "categoryIdFirst": "1400",
            "categoryIdSecound": "1401",
            "stockCode": stockCode,
            "checkedAttributeList": [],
            "salePrice": salePrice,
            "settlementPrice": settlementPrice,
            "memberPrice": memberPrice,
            "customerPrice": customerPrice,
            "goodsSize": "800*800",
            "goodsUnit": "平米",
            "info": "",
            "marque": marque,
            "factoryModel": "bb001",
            "remark": "瓷砖",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1689132072756.jpg",
            "sceneImg": ""
        }]
    }

    res = requests.post(url=url, headers=headers, json=data)
    print(res.json())


# 家具>床具>床 品牌：京世威登
def createJiaJuChuang():
    stockCode = 'b' + str(random.randint(100, 9999))
    # 销售属性
    valueName = 'xs' + str(random.randint(100, 9999))
    # 商品型号
    marque = 'sp' + str(random.randint(100, 9999))
    # 市场价
    customerPrice = random.randint(100, 999)
    # 会员价
    memberPrice = random.randint(100, 999)
    # 结算价
    settlementPrice = random.randint(100, 999)
    # 含税采购价
    salePrice = random.randint(100, 999)
    # 规格名称
    attributeName = 'gg' + str(random.randint(10, 99))
    # 规格值
    attributeValue = 'ggz' + str(random.randint(100, 999))
    data = {
        "t": 1689140955025,
        "goodsName": "床",
        "categoryIdThird": "a",
        "categoryIdFirst": "0100",
        "categoryIdSecound": "0101",
        "saleAttributeStatus": 1,
        "checkedAttributeList": [],
        "saleAttributeList": [{
            "isImage": 'false',
            "attributeName": attributeName,
            "id": 0.25717156742783476,
            "attributeValueList": [{
                "valueName": valueName,
                "id": 0.8234697303451735
            }]
        }],
        "categoryIdZero": "20",
        "brandId": 188,
        "brandName": "京世威登",
        "orderingCycle": "33",
        "factoryId": 117,
        "factoryName": "咖啡工厂",
        "goodsSkuList": [{
            "saleAttributes": [{
                "attributeName": "chua",
                "attributeValue": attributeValue
            }],
            "brandId": 188,
            "goodsName": "床",
            "factoryId": 117,
            "orderingCycle": "33",
            "id": 0.294915654166378,
            "categoryIdThird": "a",
            "categoryIdFirst": "0100",
            "categoryIdSecound": "0101",
            "stockCode": stockCode,
            "checkedAttributeList": [],
            "salePrice": salePrice,
            "settlementPrice": settlementPrice,
            "memberPrice": memberPrice,
            "customerPrice": customerPrice,
            "goodsUnit": "张",
            "info": "",
            "marque": marque,
            "factoryModel": "z123",
            "remark": "asda",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1689140929228.jpg",
            "sceneImg": ""
        }]
    }

    res = requests.post(url=url, headers=headers, json=data)
    print(res.json())


# 厨卫五金>地漏>普通地漏 品牌：飞利浦
def createDiLou():
    stockCode = 'b' + str(random.randint(100, 9999))
    # 销售属性
    valueName = 'xs' + str(random.randint(100, 9999))
    # 商品型号
    marque = 'sp' + str(random.randint(100, 9999))
    # 市场价
    customerPrice = random.randint(100, 999)
    # 会员价
    memberPrice = random.randint(100, 999)
    # 结算价
    settlementPrice = random.randint(100, 999)
    # 含税采购价
    salePrice = random.randint(100, 999)
    # 规格名称
    attributeName = 'gg' + str(random.randint(10, 99))
    # 规格值
    attributeValue = 'ggz' + str(random.randint(100, 999))
    data = {
        "t": 1689142170211,
        "goodsName": "地漏",
        "categoryIdThird": "c",
        "categoryIdFirst": "2600",
        "categoryIdSecound": "2812",
        "saleAttributeStatus": 1,
        "checkedAttributeList": [],
        "saleAttributeList": [{
            "isImage": 'false',
            "attributeName": "gh20",
            "id": 0.4680308093910721,
            "attributeValueList": [{
                "valueName": valueName,
                "id": 0.9091533011407629
            }]
        }],
        "categoryIdZero": "40",
        "brandId": 186,
        "brandName": "飞利浦",
        "orderingCycle": "33",
        "factoryId": 107,
        "factoryName": "富牌",
        "goodsSkuList": [{
            "saleAttributes": [{
                "attributeName": attributeName,
                "attributeValue": attributeValue
            }],
            "brandId": 186,
            "goodsName": "地漏",
            "factoryId": 107,
            "orderingCycle": "33",
            "id": 0.8940818279343987,
            "categoryIdThird": "c",
            "categoryIdFirst": "2600",
            "categoryIdSecound": "2812",
            "stockCode": stockCode,
            "checkedAttributeList": [],
            "salePrice": salePrice,
            "settlementPrice": settlementPrice,
            "memberPrice": memberPrice,
            "customerPrice": customerPrice,
            "goodsUnit": "个",
            "info": "",
            "marque": marque,
            "factoryModel": "z645",
            "remark": "qwd",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsCenter/new/1689142153351.jpg",
            "sceneImg": ""
        }]
    }
    res = requests.post(url=url, headers=headers, json=data)
    print(res.json())


if __name__ == '__main__':
    # 主材 - 墙地饰材>瓷砖>抛光砖 品牌：稚木青禾
    # crateGoods_a()
    # 家具>床具>床 品牌：京世威登
    # createJiaJuChuang()
    #厨卫五金>地漏>普通地漏 品牌：飞利浦
    createDiLou()