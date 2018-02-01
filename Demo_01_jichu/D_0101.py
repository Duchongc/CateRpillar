# -*- coding: utf-8 -*-
# @Time    : 2018/2/17 0017 22:09
# @Author  : LaoZhongYi
# @File    : D_0101.py
from selenium import webdriver
import unittest,time
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_demo01(self):
        firstURL = "http://www.sogou.com"
        secondURL = "http://www.baidu.com"
        # 最大化浏览器
        self.driver.maximize_window()
        # 首先访问sogou
        self.driver.get(firstURL)
        time.sleep(1)
        # 然后访问baidu
        self.driver.get(secondURL)
        # 返回上一次访问过得搜狗首页
        time.sleep(1)
        self.driver.back()
        # 再次回到百度首页
        time.sleep(1)
        self.driver.forward()
        # 刷新当前页面
        time.sleep(2)
        self.driver.refresh()
        # 获取并设置当前窗口的位置
        position = self.driver.get_window_position()
        print(position['x'], position['y'])
        # 设置当前浏览器在屏幕上的位置
        self.driver.set_window_position(x=400, y=300)
        time.sleep(3)
        print(self.driver.get_window_position())
        sizeDict = self.driver.get_window_size()
        print(sizeDict['width'], sizeDict['height'])
        time.sleep(2)
        self.driver.set_window_size(width=200, height=400, windowHandle='current')
        print(self.driver.get_window_size())
        time.sleep(2)
        # 获取当前title
        title = self.driver.title
        print(title)
        #self.assertEqual(title, u"百度一下，你就知道","页面title属性错误")
        # 获取网页源代码
        pageSource = self.driver.page_source
        print(pageSource)
        #self.assertTrue(u"新闻" in  pageSource,"页面源码未找到关键字")
        # 获取当前页面的URL
        currentPageUrl = self.driver.current_url
        print(currentPageUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id("kw").send_keys("w3cschool")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@id="1"]//a[text()="w3"]').click()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

