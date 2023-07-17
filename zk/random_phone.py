# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/28 下午1:51
@Auth ： wangzhanjun

"""

# -*- coding: utf-8 -*-

import random

'''随机手机号'''


def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # second = 2

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # third = 0

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    print(create_phone())
