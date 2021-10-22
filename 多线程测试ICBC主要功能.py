import threading
from HTMLTestRunner import HTMLTestRunner
import unittest
import os # 系统
from threading import Thread
# 加载所有用例
class test(threading.Thread):
    pattern = ''
    file = ""
    def run(self) -> None:
        tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern=self.pattern)
        # 执行器
        runner = HTMLTestRunner.HTMLTestRunner(
            title= "工商银行功能测试报告",
            description="",
            verbosity=1,
            stream = open(file=self.file, mode="w+", encoding="utf-8")
        )
        runner.run(tests)
r1 = test()
r2 = test()
r3 = test()
r4 = test()
r5 = test()
r1.pattern = "TestBank.py"
r2.pattern = "TestBank1.py"
r3.pattern = "TestBank2.py"
r4.pattern = "TestBank3.py"
r5.pattern = "TestBank4.py"

r1.file = "开户.html"
r2.file = "存钱.html"
r3.file = "取钱.html"
r4.file = "查询.html"
r5.file = "转账.html"

r1.start()
r2.start()
r3.start()
r4.start()
r5.start()









