# coding=utf-8

import time
from ui.view.baseview.web.base_web import BaseWebPage

class dynamic_loading(BaseWebPage):
    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)

    def loading(self):
        js = "return action=document.body.scrollHeight"
        height = self.driver.execute_script(js)

        # 将滚动条调整至页面底部
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)

        #定义初始时间戳（秒）
        t1 = int(time.time())

        #定义循环标识，用于终止while循环
        status = True

        # 重试次数
        num=0
        flag = 0

        while status and flag < 5:
            flag = flag + 1
            # 获取当前时间戳（秒）
            t2 = int(time.time())
            # 判断时间初始时间戳和当前时间戳相差是否大于30秒，小于30秒则下拉滚动条
            if t2-t1 < 7:
                new_height = self.driver.execute_script(js)
                if new_height > height :
                    time.sleep(1)
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    # 重置初始页面高度
                    height = new_height
                    # 重置初始时间戳，重新计时
                    t1 = int(time.time())
            elif num < 3:    # 当超过30秒页面高度仍然没有更新时，进入重试逻辑，重试3次，每次等待30秒
                time.sleep(3)
                num = num+1
            else:    # 超时并超过重试次数，程序结束跳出循环，并认为页面已经加载完毕！
                print("滚动条已经处于页面最下方！")
                status = False
                # 滚动条调整至页面顶部
                self.driver.execute_script('window.scrollTo(0, 0)')
                break

    def scrool_top(self):
        # 拉到顶部
        self.driver.execute_script('window.scrollTo(0, 0)')

"""
if __name__ == '__main__':
    loading()
"""
