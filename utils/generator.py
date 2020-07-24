# coding=utf-8

from faker import Factory, Faker

"""一些生成器方法，生成姓名，手机号"""
fake = Factory().create('zh_CN')


def random_phone_number():
    """随机手机号"""
    return fake.phone_number()


def random_name():
    """随机姓名"""
    return fake.name()


def random_id_number():
    """随机身份证号"""
    return fake.ssn()


def random_number(digits=18):
    """digits=18的随机数"""
    return fake.random_number(digits, fix_len=True)


def random_address():
    """随机地址"""
    return fake.address()


def random_post_code():
    """随机邮编"""
    return fake.postcode()


def random_email_address():
    """随机邮箱地址"""
    return fake.ascii_company_email()


def credit_card_number():
    """随机银行卡号"""
    return fake.credit_card_number()


def random_company_name():
    """随机公司名称"""
    return fake.company()


if __name__ == '__main__':
    print(random_name())
    print(random_phone_number())
    print(random_id_number())
    print(random_number())
    print(random_address())
    print(random_post_code())
    print(random_email_address())
    print(credit_card_number())
    print(random_company_name())
