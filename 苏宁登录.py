from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.suning.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="reg-bar-node"]/a[1]').click()
driver.find_element_by_xpath('//html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()
driver.find_element_by_xpath('//*[@id="userName"]').send_keys('15536221213')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('ren414005477')
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="iar1_sncaptcha_button"]').click()