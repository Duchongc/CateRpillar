# coding=utf-8
import unittest,os,time
from tomorrow import threads
from BeautifulReport import BeautifulReport
from Demo_01_shujuku.post_email.Email import *

# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "case")
test_report = 'D:\\toors\\python\\selenium_python\\unittest_test\\Unittest_Demo\\report'  # 测试报告所在目录
if not os.path.exists(casepath):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(casepath)
reportpath = os.path.join(curpath, "report")
if not os.path.exists(reportpath): os.mkdir(reportpath)


def add_case(case_path=casepath, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间
    filename = test_report + '\\' + now + 'result.html'  # 拼接出测试报告名
    result.report(filename='report.html',description='测试beautiful报告',log_path='report')

def newReport(testReport):
    lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表

    #lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists[0])  # 获取最后一个即最新的测试报告地址
    print(file_new)
    return file_new

if __name__ == "__main__":
    # 用例集合
    cases = add_case()

    print(cases)
    for i in cases:
        print(i)
        run(i)
    time.sleep(20)
    new_report = newReport(test_report)  # 获取最新报告文件
    sendReport(new_report)  # 发送最新的测试报告

