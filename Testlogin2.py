from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import time
from InitPage import InitPage
from LoginOperation import  LoginOperation
from selenium import webdriver


@data(*InitPage.login_kong_data)
def testloginKong(self, testdata):
    username = testdata["username"]
    pwd = testdata["pwd"]
    expect = testdata["expect"]
    driver = webdriver.Chrome()
    loginop = LoginOperation(driver)
    loginop.login(username, pwd)
    result = loginop.getError_result()
    driver.quit()
    self.assertEqual(result, expect)
