# coding=utf-8
# @Time :
# @Author :
# @File : generate_phone_number.py
import random


def create_phone():
    # 第二位数字
    second = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 4)]

    # 第三位数字
    third = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0][random.randint(0, 3)]
    # third = {
    #     3: random.randint(0, 9),
    #     4: [5, 7, 9][random.randint(0, 2)],
    #     5: [i for i in range(10) if i != 4][random.randint(0, 8)],
    #     7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
    #     8: random.randint(0, 9),
    # }[second]

    # 最后八位数字
    suffix = random.randint(10000000, 99999999)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    # 生成手机号
    phone = create_phone()
    phonee = create_phone()
    print(phone, phonee)