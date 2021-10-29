import threading
from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread
class test(threading.Thread):
    pattern = ''
    file = ''
    def run(self) -> None:
        tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern=self.pattern)
        runner = HTMLTestRunner.HTMLTestRunner(
            title= "HKR测试报告",
            description='',
            verbosity=1,
            stream=open(file=self.file,mode="w+",encoding="utf-8")
        )
        runner.run(tests)
r1 = test()
r2 = test()
r3 = test()

r1.pattern = "Testlogin.py"
r2.pattern = "Testlogin1.py"
r3.pattern = "Testlogin2.py"

r1.file = "账号密码正确的期望结果.html"
r2.file = "账号或密码不正确的结果.html"
r3.file = "账号或密码不能为空的结果.html"

r1.start()
r2.start()
r3.start()