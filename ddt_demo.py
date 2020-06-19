# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 17:15
# @File    : ddt_demo.py
# @Author  : 守望@天空~

import unittest

from ddt import ddt, data
from selenium import webdriver



@ddt
class FooTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True


    @data("https://www.baidu.com")
    def test_greater(self, value):

        self.driver.get(value)
        self.add_img()

if __name__ =="__main__":
    from HTMLTestRunner_cn import HTMLTestRunner
    suite = unittest.TestLoader().loadTestsFromTestCase(FooTestCase)
    runer = HTMLTestRunner(title="带截图的测试报告", description="小试牛刀", stream=open("sample_test_report_ddt.html", "wb"), verbosity=2, retry=1, save_last_try=True)
    runer.run(suite)