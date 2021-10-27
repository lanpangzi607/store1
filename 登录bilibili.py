from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains
import random
import requests
from hashlib import md5
import logging

driver = webdriver.Chrome()

driver.get("https://www.bilibili.com")
qq = driver.maximize_window()
# time.sleep(2)
driver.find_element_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/ul[2]/li[1]/li/div/div').click()

data = driver.window_handles
driver.switch_to.window(data[1])

driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("15535211843")
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("ren414005477")
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()


