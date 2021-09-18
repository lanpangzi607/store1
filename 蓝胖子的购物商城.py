import random
shop = [
    #角标   0        ,     1
    ["机械革命"   ,   15000],#0 print(shop[0][1])=15000
    ["HUAWEI watch", 1200],#1 print(shop[1][1])=1200
    ["MAC PC",       13000],#2 print(shop[2][1])=13000
    ["Iphone 54 plus",45000],
    ["辣条"           ,2.5],
    ["老干妈"          ,13]
]
moeny=int(input("请输入你的金额"))#str
mycart=[]
ran = random.randint(1,50)
print(ran)
i = 1
if ran <= 10:
    R = 8
    print("辣条优惠卷一张")
elif ran <= 30:
    R = 9
    print("机械革命优惠卷一张")
else:
    print("谢谢惠顾")
while True: #永远循环
    for index,value in enumerate(shop):#枚举，把角标和角标对应的内容进行整体打印
        print(index,value)#打印所有的商品
    chose=input("请输入你想要的商品")
    # int 如果你一开始就是数字，那么下面的if就没有意义
    if chose.isdigit():#isdigit-判断是否为数字
        chose =int(chose)
        if chose>len(shop)-1:#你输入的角标，如果大于商品的长度就执行代码
            print("你所输入的商品不存在")
            break
        else:
            if moeny> shop[chose][1] :#你原有存款和商品价格对比
                mycart.append(shop[chose])#加入购物车
                if R == 8 and shop[chose][0] == "辣条" :
                    moeny = moeny - shop[chose][1]*0.3
                elif R == 9 and shop[chose][0] == "机械革命":
                    moeny = moeny - shop[chose][1]*0.9
                else:
                    moeny=moeny-shop[chose][1]#存款减去商品价格
                print("恭喜你购买成功，已经加入购物车")
            else:
                print("gun")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临，下面的是您的小票")
        for index,value in enumerate(mycart):
            print(index," ",value)
        print("您的余额还剩:",moeny,"元")
        break
    else:
        print("输入非法")