from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.jd.com")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("大象")
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
time.sleep(3)

r = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[2]').click()
q = driver.window_handles
driver.switch_to.window(q[1])

# driver.find_element_by_xpath('//*[@id="area1"]/div[1]/div').send_keys("北京昌平区沙河地区")
# ele=driver.find_element_by_xpath('//*[@id="area1"]/div[1]/div')
# st=Select(ele)
# st.select_by_value('昌平区')
# st.select_by_value('沙河地区')
# driver.find_element_by_id("area='2901'").send_keys("昌平区")
# driver.find_element_by_id("text='55561'").send_keys("沙河地区")

driver.find_element_by_xpath('//*[@id="choose-attr-1"]/div[2]/div[8]').click()
driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()

driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("15536221213")
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys("ren414005477")
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()

source = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
box = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]')
x = box.size['width']
ActionChains(driver).drag_and_drop_by_offset(source,100,0).perform()

# driver.quit()





















