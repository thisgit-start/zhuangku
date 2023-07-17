# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/31 下午6:02
@Auth ： wangzhanjun

"""
import pymysql
import random


def get_db_conn():
    '''
    连接数据库
    :return:返回数据库连接
    '''
    try:
        conn = pymysql.connect(
            host='123.57.50.102',
            port=3306,
            user='root',
            passwd='Zk887@638294rT',
            db='renren_fast',
            charset='utf8'
        )
    except Exception as e:
        print(e)
    return conn

#随机生成
def randomNumber():
    random_number = random.randint(10 ** 11, 10 ** 12 - 1)
    print(random_number)
    return random_number


def insertJDCode():
    conn = get_db_conn()
    cur = conn.cursor()
    # 京东卡密
    pwd_number = randomNumber()
    # 金额
    jd_price = 20.00
    # 用户ID
    user_id = 106803

    sql = '''INSERT INTO `renren_fast`.`jd_code` (`order_id`, `pwd_number`, `sku_id`, `effective_date`
	, `sku_name`, `sku_type`, `jd_price`, `payment`, `commission`
	, `payment_online`, `unused_count`, `market_price`, `user_id`, `jd_status`
	, `status`)
VALUES (202305261112, '{}', 10074475654543, NOW()
	, '金意陶（KITO）招商公园1872 家居大礼包（购房业主专享） 壹元家具家电包', '0', {}, NULL, NULL
	, 1.00, 1, 10000.00, {}, 1
	, 0);'''.format(pwd_number, jd_price, user_id)
    cur.execute(sql)
    conn.commit()
    print("提交成功")


if __name__ == '__main__':
    insertJDCode()