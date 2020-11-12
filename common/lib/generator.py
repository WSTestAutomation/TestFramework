# coding=utf-8
import random
from faker import Faker

class Generator:

    def __init__(self, locale='zh_CN'):
            self.fake = Faker(locale)

    """一些生成器方法，生成姓名，手机号"""

    def random_phone_number(self):
        """随机手机号"""
        return self.fake.phone_number()


    def random_name(self):
        """随机姓名"""
        return self.fake.name()


    def random_ssn(self):
        """随机身份证号"""
        return self.fake.ssn()


    def random_number(self, digits=18):
        """digits=18的随机数"""
        return self.fake.random_number(digits, fix_len=True)


    def random_address(self):
        """随机地址"""
        return self.fake.address()


    def random_post_code(self):
        """随机邮编"""
        return self.fake.postcode()


    def random_email(self):
        """随机邮箱地址"""    
        return self.fake.ascii_company_email()


    def credit_card_number(self):
        """随机银行卡号"""
        return self.fake.credit_card_number()


    def random_company_name(self):
        """随机公司名称"""
        return self.fake.company()

    def random_ipv4(self):
        """随机IPV4地址"""
        return self.fake.ipv4()

    def random_str(self, min_chars=0, max_chars=8):
        """长度在最大值与最小值之间的随机字符串"""
        return self.fake.pystr(min_chars=min_chars, max_chars=max_chars)

    def factory_generate_ids(self, starting_id=1, increment=1):
        """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
        def generate_started_ids():
            val = starting_id
            local_increment = increment
            while True:
                yield val
                val += local_increment

        return generate_started_ids


    def factory_choice_generator(self, values):
        """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
        def choice_generator():
            my_list = list(values)
            rand = random.Random()
            while True:
                yield rand.choice(my_list)

        return choice_generator

if __name__ == '__main__':
    gen = Generator()
    print("随机手机号码", gen.random_phone_number())
    print("随机姓名", gen.random_name())
    print("随机地址", gen.random_address())
    print("随机邮箱地址", gen.random_email())
    print("随机IP地址", gen.random_ipv4())
    print("随机身份证号码", gen.random_ssn())
    print("随机字符串", gen.random_str(min_chars=6, max_chars=8))
    # id_gen = factory_generate_ids(starting_id=0, increment=2)()
    # for i in range(5):
    #     print(next(id_gen))
    #
    # choices = ['John', 'Sam', 'Lily', 'Rose']
    # choice_gen = factory_choice_generator(choices)()
    # for i in range(5):
    #     print(next(choice_gen))
