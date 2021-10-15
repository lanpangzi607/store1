import time
from threading import Thread
baket = 0
count1 = 0
class cooker(Thread):
    def run(self) -> None:
        global baket
        global count1
        count_end = 0
        while 1:
            if baket < 500:
                baket += 1
                count1 += 1
                count_end = 0
            else:
                time.sleep(0.1)
                count_end += 1
                if count_end > 100:
                    print('总共制作了',count1,'个汉堡')
                    break
class eater(Thread):
    username = ''
    def run(self) -> None:
        global baket
        money = 10000
        count = 0
        while 1:
            if money > 0:
                if baket > 0:
                    baket -= 1
                    money -= 5
                    count +=1
                else:
                    time.sleep(0.1)
            else:
                print(self.username,'买了',count,'个！')
                break
c1 = cooker()
c2 = cooker()
c3 = cooker()
c1.start()
c2.start()
c3.start()
e1 = eater()
e1.username = '刘皇叔'
e1.start()
e2 = eater()
e2.username = '关逼王'
e2.start()
e3 = eater()
e3.username = '张窟窿'
e3.start()
e4 = eater()
e4.username = '赵子龙'
e4.start()
e5 = eater()
e5.username = '黄哈哈'
e5.start()
e6 = eater()
e6.username = '马儿'
e6.start()