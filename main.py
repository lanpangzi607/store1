from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR系统测试报告",
    description= "HKR系统登陆测试",
    verbosity=1,
    stream = open(file="hkr.html",mode="w+",encoding="utf-8")
)

runner.run(tests)

# 邮件发送模块





