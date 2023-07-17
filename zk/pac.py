import json
import re
import sys
import time
from zk.zk_erp import zk
# import redis
import requests


# 发送短信
def send_ver(phone):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'}
    body = {
        'phone': phone,
        # 'phone':'18513087397'
    }
    url = 'http://testonline.zk-house.com/api/giftbag/sms/phone/send'
    res = requests.post(url=url, headers=headers, json=body).text
    a = re.findall('"message":"(.*?)","da', res)
    if a[0] == '成功':
        return res
    else:
        print('接口报错')


# 查询验证码
def search_redis(phone):
    ip = '123.57.50.102'
    port = '6379'
    passwd = '123456'
    try:
        re = redis.Redis(host=ip, password=passwd, port=port, db=0, decode_responses=True)
        code = re.get('giftbag:phone:' + str(phone))
        print('验证码：' + str(code))
        re.close()
    except Exception as e:
        print(e)
    return code


# 登录
def login(code, phone):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}
    body = {
        'phone': phone,
        'verificationCode': code,
    }
    url = 'http://testonline.zk-house.com/api/giftbag/login/submit'
    try:
        res = requests.post(url=url, headers=headers, json=body).text
        token = json.loads(res)['data']['token']
        return token
    except Exception as e:
        print(e)



def creat_order(token, phone, p_id, huxing_id, libao_id, a_id=None):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'token': token
    }
    body = {
        "suitGoods": [{
            "id": 38778,
            "suitId": 919,
            "groupId": 7619,
            "goodsId": 15887,
            "goodsName": "客厅、餐厅、厨房、阳台地砖",
            "goodsNum": 0,
            "isCheck": 0,
            "brandName": "金意陶",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1631267522443.jpg",
            "marque": "K00808156YAF",
            "goodsSize": "800*800mm",
            "remark": "抛釉砖，防污耐磨",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1659624298079.png",
            "stockCode": "0101004",
            "purchasePrice": 30.33,
            "marketPrice": 298,
            "showPrice": "null",
            "sortNo": 1,
            "categoryIdFirst": "1400",
            "categoryIdSecound": "1402",
            "categoryIdThird": "e",
            "goodsUnit": "片",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38779,
            "suitId": 919,
            "groupId": 7619,
            "goodsId": 15888,
            "goodsName": "厨房墙砖",
            "goodsNum": 0,
            "isCheck": 0,
            "brandName": "金意陶",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1659624473167.png",
            "marque": "K00632226CAF",
            "goodsSize": "300*600mm",
            "remark": "抛釉砖，防污耐磨",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1659624358088.png",
            "stockCode": "0101005",
            "purchasePrice": 6.15,
            "marketPrice": 49,
            "showPrice": "null",
            "sortNo": 2,
            "categoryIdFirst": "1400",
            "categoryIdSecound": "1402",
            "categoryIdThird": "e",
            "goodsUnit": "片",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38780,
            "suitId": 919,
            "groupId": 7619,
            "goodsId": 15888,
            "goodsName": "公共卫生间墙砖",
            "goodsNum": 0,
            "isCheck": 0,
            "brandName": "金意陶",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1659624473167.png",
            "marque": "K00632226CAF",
            "goodsSize": "300*600mm",
            "remark": "抛釉砖，防污耐磨",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1659624358088.png",
            "stockCode": "0101005",
            "purchasePrice": 6.15,
            "marketPrice": 49,
            "showPrice": "null",
            "sortNo": 3,
            "categoryIdFirst": "1400",
            "categoryIdSecound": "1402",
            "categoryIdThird": "e",
            "goodsUnit": "片",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38781,
            "suitId": 919,
            "groupId": 7619,
            "goodsId": 15889,
            "goodsName": "公共卫生间地砖",
            "goodsNum": 0,
            "isCheck": 0,
            "brandName": "金意陶",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1659624081843.png",
            "marque": "K00302226CAN",
            "goodsSize": "300*300mm",
            "remark": "抛釉砖，防污耐磨",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1659624495735.png",
            "stockCode": "0101006",
            "purchasePrice": 3.08,
            "marketPrice": 49,
            "showPrice": "null",
            "sortNo": 4,
            "categoryIdFirst": "1400",
            "categoryIdSecound": "1402",
            "categoryIdThird": "e",
            "goodsUnit": "片",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38790,
            "suitId": 919,
            "groupId": 7622,
            "goodsId": 16599,
            "goodsName": "大自然地板 (浅木纹）",
            "goodsNum": 0,
            "isCheck": 0,
            "brandName": "大自然",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658840649588.png",
            "marque": "午后云谷",
            "goodsSize": "1218*195*10",
            "remark": "强化复合地板 耐磨6000转/锁扣/封蜡防潮",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0102032",
            "purchasePrice": 52,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 1,
            "categoryIdFirst": "1500",
            "categoryIdSecound": "1503",
            "categoryIdThird": "e",
            "goodsUnit": "平米",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goodsScene/1663915167712.png",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38793,
            "suitId": 919,
            "groupId": 7623,
            "goodsId": 16504,
            "goodsName": "乳胶漆底漆",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "三棵树",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1656575428431.png",
            "marque": "25kg",
            "goodsSize": "25kg",
            "remark": "/",
            "defaultCheck": 1,
            "requiredStatus": 1,
            "codeUrl": "",
            "stockCode": "0103003",
            "purchasePrice": 175,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 1,
            "categoryIdFirst": "4300",
            "categoryIdSecound": "4301",
            "categoryIdThird": "m",
            "goodsUnit": "桶",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38794,
            "suitId": 919,
            "groupId": 7623,
            "goodsId": 16505,
            "goodsName": "乳胶漆面漆",
            "goodsNum": 2,
            "isCheck": 0,
            "brandName": "三棵树",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1656576968363.png",
            "marque": "30kg",
            "goodsSize": "30kg",
            "remark": "/",
            "defaultCheck": 1,
            "requiredStatus": 1,
            "codeUrl": "",
            "stockCode": "0103004",
            "purchasePrice": 141,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 2,
            "categoryIdFirst": "4300",
            "categoryIdSecound": "4301",
            "categoryIdThird": "m",
            "goodsUnit": "桶",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38796,
            "suitId": 919,
            "groupId": 7624,
            "goodsId": 15938,
            "goodsName": "四季沐歌马桶-400孔距",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "四季沐歌",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1641375610888.png",
            "marque": "M-ZD288X",
            "goodsSize": "715*385*755（400）",
            "remark": "400孔距",
            "defaultCheck": 1,
            "requiredStatus": 1,
            "codeUrl": "null",
            "stockCode": "0204009",
            "purchasePrice": 469,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 3,
            "categoryIdFirst": "1800",
            "categoryIdSecound": "2102",
            "categoryIdThird": "h",
            "goodsUnit": "个",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38797,
            "suitId": 919,
            "groupId": 7624,
            "goodsId": 15945,
            "goodsName": "四季沐歌花洒三件套",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "四季沐歌",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1641375659876.png",
            "marque": "M-A3570-1D",
            "goodsSize": "龙头：15中心距）",
            "remark": "null",
            "defaultCheck": 1,
            "requiredStatus": 1,
            "codeUrl": "null",
            "stockCode": "0205003",
            "purchasePrice": 258,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 4,
            "categoryIdFirst": "2400",
            "categoryIdSecound": "2807",
            "categoryIdThird": "c",
            "goodsUnit": "个",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38798,
            "suitId": 919,
            "groupId": 7624,
            "goodsId": 15948,
            "goodsName": "四季沐歌地漏",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "四季沐歌",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1631937208201.jpg",
            "marque": "M-E015B-G",
            "goodsSize": "112*112",
            "remark": "优质不锈钢  防臭防堵防虫",
            "defaultCheck": 1,
            "requiredStatus": 1,
            "codeUrl": "",
            "stockCode": "0206001",
            "purchasePrice": 13.9,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 5,
            "categoryIdFirst": "2600",
            "categoryIdSecound": "2812",
            "categoryIdThird": "c",
            "goodsUnit": "个",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38799,
            "suitId": 919,
            "groupId": 7624,
            "goodsId": 16515,
            "goodsName": "不锈钢挂件六件套",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "四季沐歌",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1656662558959.png",
            "marque": "'M-D611-B",
            "goodsSize": "11*10",
            "remark": "浴巾架，毛巾架，不锈钢五排挂衣钩，双层三角篮，纸巾盒马桶杯",
            "defaultCheck": 0,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0207001",
            "purchasePrice": 279,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 6,
            "categoryIdFirst": "2800",
            "categoryIdSecound": "2817",
            "categoryIdThird": "c",
            "goodsUnit": "套",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38800,
            "suitId": 919,
            "groupId": 7625,
            "goodsId": 16570,
            "goodsName": "沙发-右贵妃",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "新舍-华戴",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658381254070.png",
            "marque": "L6010（右）（主色9070-14色，配色9070-10色（科技布）",
            "goodsSize": "2900*1840*740mm",
            "remark": "科技布面料，座包填充物，高密度\n18公分回弹环保海绵\n\n",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0301095（右）",
            "purchasePrice": 3450,
            "marketPrice": 12880,
            "showPrice": "null",
            "sortNo": 1,
            "categoryIdFirst": "0400",
            "categoryIdSecound": "0401",
            "categoryIdThird": "a",
            "goodsUnit": "套",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0,
            "active": 1
        }, {
            "id": 38802,
            "suitId": 919,
            "groupId": 7625,
            "goodsId": 16563,
            "goodsName": "茶几",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "新舍-华戴",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658375881451.png",
            "marque": "T152茶几",
            "goodsSize": "大800*800*450mm 小600*600*400mm\"",
            "remark": "碳钢素+岩板\n",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0302033",
            "purchasePrice": 520,
            "marketPrice": 6452,
            "showPrice": "null",
            "sortNo": 3,
            "categoryIdFirst": "0800",
            "categoryIdSecound": "0803",
            "categoryIdThird": "a",
            "goodsUnit": "件",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0,
            "active": 1
        }, {
            "id": 38803,
            "suitId": 919,
            "groupId": 7625,
            "goodsId": 16564,
            "goodsName": "餐桌",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "新舍-华戴",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658380275242.png",
            "marque": "17501餐桌",
            "goodsSize": "1400*800*750mm",
            "remark": "面板 ： 岩板+ 底板\n脚 ：钢铁黑沙脚\n",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0304032",
            "purchasePrice": 530,
            "marketPrice": 6530,
            "showPrice": "null",
            "sortNo": 4,
            "categoryIdFirst": "0800",
            "categoryIdSecound": "0802",
            "categoryIdThird": "a",
            "goodsUnit": "张",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0,
            "active": 1
        }, {
            "id": 38804,
            "suitId": 919,
            "groupId": 7625,
            "goodsId": 16565,
            "goodsName": "餐椅",
            "goodsNum": 4,
            "isCheck": 0,
            "brandName": "新舍-华戴",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658380545294.png",
            "marque": "Y6038餐椅",
            "goodsSize": "490*460*900mm",
            "remark": "钢铁黑砂脚+PU皮\n",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0305116",
            "purchasePrice": 199,
            "marketPrice": 1075,
            "showPrice": "null",
            "sortNo": 5,
            "categoryIdFirst": "0600",
            "categoryIdSecound": "0603",
            "categoryIdThird": "a",
            "goodsUnit": "把",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0,
            "active": 1
        }, {
            "id": 38805,
            "suitId": 919,
            "groupId": 7625,
            "goodsId": 16566,
            "goodsName": "双人床",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "新舍-华戴",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658380623590.png",
            "marque": "1808床",
            "goodsSize": "2370*1880*1050mm",
            "remark": "科技布+靠背填充物高密度回弹海\n绵+全实木框架+实木板材结\n",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0306056",
            "purchasePrice": 1150,
            "marketPrice": 9890,
            "showPrice": "null",
            "sortNo": 6,
            "categoryIdFirst": "0100",
            "categoryIdSecound": "0101",
            "categoryIdThird": "a",
            "goodsUnit": "张",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0,
            "active": 1
        }, {
            "id": 38806,
            "suitId": 919,
            "groupId": 7625,
            "goodsId": 16567,
            "goodsName": "床头柜",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "新舍-华戴",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658380784825.png",
            "marque": "K08床头柜",
            "goodsSize": "450*400*400mm",
            "remark": "实木抽屉板材+布+磨砂五金铁脚+磨砂五金铁拉手\n\n",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0307036",
            "purchasePrice": 198,
            "marketPrice": 3080,
            "showPrice": "null",
            "sortNo": 7,
            "categoryIdFirst": "0100",
            "categoryIdSecound": "0103",
            "categoryIdThird": "a",
            "goodsUnit": "件",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0,
            "active": 1
        }, {
            "id": 38822,
            "suitId": 919,
            "groupId": 7628,
            "goodsId": 15614,
            "goodsName": "洗衣机",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "TCL",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658934206082.png",
            "marque": "TG-V80BA",
            "goodsSize": "595*520*850",
            "remark": "CL 8公斤 变频全自动滚筒洗衣机   节能静音 95度高温除菌除螨（芭蕾白）",
            "defaultCheck": 1,
            "requiredStatus": 1,
            "codeUrl": "",
            "stockCode": "0403011",
            "purchasePrice": 1320,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 1,
            "categoryIdFirst": "4600",
            "categoryIdSecound": "4912",
            "categoryIdThird": "b",
            "goodsUnit": "台",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38823,
            "suitId": 919,
            "groupId": 7628,
            "goodsId": 14631,
            "goodsName": "冰箱",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "TCL",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658934836645.png",
            "marque": "BCD-509WEFA1流光金（509L）",
            "goodsSize": "920*630*1768",
            "remark": "TCL 509升 风冷无霜对开门双开门电冰箱  隐形电脑控温  纤薄机身(流光金)",
            "defaultCheck": 1,
            "requiredStatus": 1,
            "codeUrl": "",
            "stockCode": "0401001",
            "purchasePrice": 2300,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 2,
            "categoryIdFirst": "4700",
            "categoryIdSecound": "4916",
            "categoryIdThird": "b",
            "goodsUnit": "台",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38825,
            "suitId": 919,
            "groupId": 7628,
            "goodsId": 16373,
            "goodsName": "扫地机器人",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "康佳",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1654953878938.png",
            "marque": "KC-VS53",
            "goodsSize": "334*344*114",
            "remark": "主要适用于木质地板，光滑水泥地面，瓷砖地面及其它硬质地板",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0501002",
            "purchasePrice": 245,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 4,
            "categoryIdFirst": "4900",
            "categoryIdSecound": "5706",
            "categoryIdThird": "b",
            "goodsUnit": "台",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38826,
            "suitId": 919,
            "groupId": 7628,
            "goodsId": 16374,
            "goodsName": "电饭煲",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "康佳",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1654954048850.png",
            "marque": "KRC-RS25",
            "goodsSize": "205*235*200",
            "remark": "2L黄金容积，一次煮6杯米的饭满足2-4人；",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0504002",
            "purchasePrice": 115,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 5,
            "categoryIdFirst": "4900",
            "categoryIdSecound": "4935",
            "categoryIdThird": "b",
            "goodsUnit": "台",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38827,
            "suitId": 919,
            "groupId": 7628,
            "goodsId": 15703,
            "goodsName": "美的吸尘器",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "美的",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658934406090.png",
            "marque": "VS04K1-FW",
            "goodsSize": "244*132*1118mm",
            "remark": "不锈钢推杆 一键取尘 180度旋转刷头",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0512001",
            "purchasePrice": 168,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 6,
            "categoryIdFirst": "4900",
            "categoryIdSecound": "5705",
            "categoryIdThird": "b",
            "goodsUnit": "件",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38828,
            "suitId": 919,
            "groupId": 7628,
            "goodsId": 15715,
            "goodsName": "空气净化器",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "志高",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658934422445.png",
            "marque": "F909",
            "goodsSize": "364*222*603",
            "remark": "给新家置一份安心 除甲醛 除装修味 除细菌",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0505001",
            "purchasePrice": 125,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 7,
            "categoryIdFirst": "4900",
            "categoryIdSecound": "4939",
            "categoryIdThird": "b",
            "goodsUnit": "台",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38829,
            "suitId": 919,
            "groupId": 7628,
            "goodsId": 15716,
            "goodsName": "净水器",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "志高",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1658934439171.png",
            "marque": "UF2",
            "goodsSize": "380*220*452",
            "remark": "五级精滤 出水直饮 保留有益的矿物质元素 物理过滤 无废水 无桶设计 静音制水",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "0506001",
            "purchasePrice": 138,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 8,
            "categoryIdFirst": "4900",
            "categoryIdSecound": "4945",
            "categoryIdThird": "b",
            "goodsUnit": "台",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }, {
            "id": 38895,
            "suitId": 919,
            "groupId": 7640,
            "goodsId": 16733,
            "goodsName": "美的烟机灶具（直吸）",
            "goodsNum": 1,
            "isCheck": 0,
            "brandName": "美的",
            "brandId": "null",
            "imgPath": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/goods/0/1661325421123.png",
            "marque": "T33A+Q218B",
            "goodsSize": "895*480*506/720*420*135",
            "remark": "面板材质\n钢化玻璃\n出风口径190mm",
            "defaultCheck": 1,
            "requiredStatus": 0,
            "codeUrl": "",
            "stockCode": "...........",
            "purchasePrice": 2000,
            "marketPrice": "null",
            "showPrice": "null",
            "sortNo": 1,
            "categoryIdFirst": "4800",
            "categoryIdSecound": "4924",
            "categoryIdThird": "b",
            "goodsUnit": "套",
            "sceneImg": "null",
            "color": "null",
            "goodSceneImg": "null",
            "original": 0,
            "makeUpPrices": 0
        }],
        "suitOrder": {
            "adviserId": None,
            "adviserName": None,
            "buildingNumber": "room",
            "houseId": huxing_id,
            "identityCard": "410523199311152554",
            "ownerName": "test-创建订单-2",
            "ownerPhone": phone,
            "projectId": p_id,
            "quickPay": 0.01,
            "signUrl": "https://zk-app-home.oss-cn-beijing.aliyuncs.com/wechatapp/sign/1663923280551.png",
            "suitId": libao_id,
            "orderAmount": 20000
            #"orderAmount": 10000
        },
        "timeStamp": 1663923280751,
        "sign": "aa3fdcd5b6f61acf6a98175adb148fdb",
        "openId": "ogmax5PvJzGBoNpDNwYZWcHB_iUo"
    }
    url = 'http://testonline.zk-house.com/api/giftbag/order/createOrder'
    res = requests.post(url=url, headers=headers, json=body).text
    a = re.findall('"message":"(.*?)","da', res)
    if a[0] == '成功':
        return json.loads(res)['data']
    else:
        print(res)
        print('订单接口报错')


def jd_pay(order, token, img_path):
    headers = {
        # 'Content-Type': 'multipart/form-data;charset=UTF-8',
        'token': token
    }
    body = {
        'orderId': order
    }

    files = {"files": (
        "1663654088716.jpg", open(img_path, 'rb'), "image/jpg")}
    url = 'http://testonline.zk-house.com/api/giftbag/order/uploadPaidImg'
    res = requests.post(url=url, headers=headers, data=body, files=files).text
    return res


'''
# 零元购
def lingyuangou(order, token):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'token': token
    }
    body = {
        'orderId': order,
        'timeStamp': 1663923280751,
        'sign': 'aa3fdcd5b6f61acf6a98175adb148fdb',
        'body': '',
        'openid': 'ogmax5PvJzGBoNpDNwYZWcHB_iUo',
        'totalFee': '',
        'tradeType': '',
        'productType': 'phoneSuit'
    }
    url = 'http://testonline.zk-house.com/api/giftbag/order/directOrder'
    res = requests.post(url=url, headers=headers, json=body).text
    return res
'''

if __name__ == '__main__':
    op = sys.argv
    # 手机号
    phone = str(op[1])
    # 图片地址
    img_path = r'C:\Users\nymel\Pictures\Saved Pictures\1664247767120.jpg'
    # 项目id
    p_id = op[2]
    huxing_id = op[3]
    # 礼包id
    libao_id = op[4]
    send_ver(phone)
    time.sleep(3)
    code = search_redis(phone)
    token = login(code, phone)
    # 置业顾问id
    if len(op) == 6:
        a_id = op[5]

        order = creat_order(token, phone, p_id, huxing_id, libao_id, a_id)
    else:
        order = creat_order(token, phone, p_id, huxing_id, libao_id)
    print('订单编号：' + str(order))
    print(jd_pay(order, token, img_path))
    print(zk(order).determine())
    # print(lingyuangou(order, token))
    # 手机号  项目id  户型id  礼包id 置业顾问id
#  18513087397 1317  2093  4656
# 18513087397   1318    2094    4662
# 1319 2095 4667
# 1290 2066 4575

'''  
1 2 1 2 2 1 
合伙人2 1349   2131  4827  4828  4829  4830  4831  4832
                2132 4833 4834 4835 4836  4837 4838
合伙人1 1348     2130 4811  


合伙人a   1354  2138 4862


hhr2 1355  2139  4867
项目礼包2 1356 2140 4877

桂林礼包1  1358 2143  4891
地图测试  1427 2236  5179
'''