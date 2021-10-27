from urllib import request
from selenium import webdriver
import cv2
import random
import time
import pyautogui

# 获取图片信息，返回最佳匹配位置
def findPic(target="img1.jpg", template="img2.png"):
    # 读取图片
    target_rgb = cv2.imread(target)
    # 图片灰度化
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    # 读取模块图片
    template_rgb = cv2.imread(template, 0)
    # 匹配模块位置
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    # 获取最佳匹配位置
    value = cv2.minMaxLoc(res)
    # 返回最佳X坐标
    return value[2][0]


# 打开FireFox浏览器
driver = webdriver.Chrome()
driver.get("https://www.jd.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('15536221213')
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('ren414005477')
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()

while True:
    try:
        # 从网页上获取组件
        target = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img')
        template = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
        # 获取模块的url路径
        src1 = target.get_attribute("src")
        src2 = template.get_attribute("src")
        # 下载图片
        request.urlretrieve(src1,"img1.jpg")
        request.urlretrieve(src2,"img2.png")
        x = findPic()
        w1 = cv2.imread('img1.jpg').shape[1]
        w2 = target.size['width']
        x = x / w1 * w2
        # 按钮坐标
        ox,oy = 1260,725
        # pyautogui库操作鼠标指针
        pyautogui.moveTo(ox,oy,duration=0.1 + random.uniform(0,0.1 + random.randint(1,100) / 100))
        pyautogui.mouseDown()
        oy += random.randint(9,19)
        pyautogui.moveTo(ox + int(x * random.randint(15,25) / 20),oy,duration=0.28)
        oy += random.randint(-9,0)
        pyautogui.moveTo(ox + int(x * random.randint(17,23) / 20),oy,
                         duration=random.randint(20,31) / 100)
        oy += random.randint(0,8)
        pyautogui.moveTo(ox + int(x * random.randint(19,21) / 20),oy,
                         duration=random.randint(20,40) / 100)
        oy += random.randint(-3,3)
        pyautogui.moveTo(x + ox + random.randint(-3,3),oy,duration=0.5 + random.randint(-10,10) / 100)
        oy += random.randint(-2,2)
        pyautogui.moveTo(x + ox + random.randint(-2,2),oy,duration=0.5 + random.randint(-3,3) / 100)
        pyautogui.mouseUp()
        time.sleep(2)
        result = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]').text
        if '不匹配' in result:
            print("账户名密码不匹配!", result)
            break
    except:
        print("异常!")
        break
