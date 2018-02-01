# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 0025 11:05
# @Author  : LaoZhongYi
# @File    : DataDrivenByMySQL.py
from selenium import webdriver
import unittest,time
import logging,traceback
import ddt
from Demo_01_shujuku.Case.MysqlUtil import MYMYSQL
from selenium.common.exceptions import NoSuchElementException
# 初始化日志
logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %Y-%m-%d %H:%M:%S',
    filename='c:dataDriverRreport.log',
    filemode='w'

)
def getTestDatas():
    db = MYMYSQL(
        host="120.**.**.213",
        port=3306,
        dbname="gloryroad",
        username="**",
        password="*******",
        charset="utf8"
    )
    testdata = db.getDataFromDataBases()
    db.closeDatabase()
    return testdata
@ddt.ddt
class TestDmeo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(*getTestDatas())
    def test_data(self,data):
        testData,expectData = data
        url = "http://www.baidu.com"
        self.driver.get(url)
        # self.driver.maximize_window()
        # 缩小浏览器
        self.driver.set_window_size(width=200, height=400, windowHandle='current')
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testData)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在,异常堆栈信息:"+str(traceback.format_exc()))
        except AssertionError as e:
            logging.info("搜索%s期望%s失败" %(testData,expectData))
        except Exception as e:
            logging.error("位置错误,错误信息:"+str(traceback.format_exc()))
        else:
            logging.info("搜索%s,期望%s通过" %(testData,expectData))
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()