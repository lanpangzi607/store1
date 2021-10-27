from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.zhihu.com")
zhihu = driver.maximize_window()

driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]').click()
time.sleep(2)

# data = driver.window_handles
# driver.switch_to.window(data[1])

driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[2]/div/label/input').send_keys('15536221213')
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys('ren414005477')
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/button').click()

data = driver.window_handles

xp = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/img[2]')
op = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div/div[1]')
r = op.size['qwe']
ActionChains(driver).drag_and_drop_by_offset(xp,100,0).perform()


