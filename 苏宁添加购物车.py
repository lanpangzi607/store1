from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.suning.com")
no = driver.maximize_window()

driver.find_element_by_id("searchKeywords").send_keys("iphone13")
driver.find_element_by_id("searchSubmit").click()

h = driver.current_window_handle
driver.find_element_by_id("0000000000-12314319126").click()

all_h = driver.window_handles

for i in all_h:
    if i != h:
        driver.switch_to.window(i)

driver.switch_to.window(all_h[1])
driver.find_element_by_xpath("//*[@id='colorItemList']/dd/ul/li[15]/a").click()

driver.find_element_by_xpath("//*[@id='versionItemList']/dd/ul/li[4]/a").click()
driver.find_element_by_xpath("//*[@id='addCart']").click()
driver.find_element_by_xpath("/html/body/div[9]/div/div[2]/div/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()