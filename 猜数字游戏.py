import random
lan = random.randint(0, 100)
i = 0
R = 500
while R>=100 and i<3:
    pang=int(input('请输入一个数值：'))
    i+=1
    R = R - 100
    print(R)
    if   pang>lan:
        print("猜大了")
    elif pang<lan:
        print('猜小了')
    else :
        print('ok')
        R +=10
