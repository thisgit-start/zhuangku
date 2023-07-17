# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/28 下午6:33
@Auth ： wangzhanjun

"""
import datetime

# 获取当前日期和时间
now = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")


def writeTxt(text):
    f = open('/Users/wang/PycharmProjects/zhuangku/zk/text.txt', 'a+')
    textStr = str(text) + str(formatted_time) + str('\n')

    f.write(textStr)
    f.close()


if __name__ == '__main__':
    for i in range(5):
        writeTxt('\n{}'.format("*" * 100))
    pass
