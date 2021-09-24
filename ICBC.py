'''
中国工商银行账户管理系统：
    ICBC：
'''
import random
#1.准备一个数据库和银行名称
bank = {12345678:{"username":"大先生",
        "password":123,
        "country":"CN",
        "province":"北京",
        "street":"昌平",
        "gate":"回龙观",
        "money":1000},
        87654321:{
        "username":"二先生",
        "password":123,
        "country":"CN",
        "province":"北京",
        "street":"昌平",
        "gate":"回龙观",
        "money":1000} } #空的数据库
bank_name = "中国工商银行昌平回龙观支行" #银行名称写死的



#2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


#银行的开户逻辑
def bank_adduser(account,username,password,country,province,street,gate,money,bank_name):
    #1.判断数据库是否已满
    if len(bank) >= 100:
        return 3
    #2.判断用户是否存在
    if username in bank:
        return 2
    #3.正常开户
    bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "gate":gate,
        "money":money,
        "bank_name":bank_name
    }
    return 1

#用户的开户操作逻辑
def adduser():
    username = input("请输入您的用户名：")
    password = int(input("请输入您的开户密码："))
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号")
    money = int(input("请输入您开户时存入的金额"))     #将输入金额转换成int类型（整形）

    # 随机产生一个数字，导入import random
    account = random.randint(10000000,99999999)

    status = bank_adduser(account,username,password,country,province,street,gate,money,bank_name)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其它银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
                    ----------个人信息------
                    用户名：%s
                    密码：%s
                    账号：%s
                    地址信息
                        国家：%s
                        省份：%s
                        街道：%s
                        门牌号: %s
                    余额：%s
                    开户行地址：%s
                    ------------------------
                '''
        print(info % (username,password,account,country,province,street,gate,money,bank_name))



def lan_cunkuan():
    account = int(input('请输入要存款的账号：'))
    if account in bank:
        money = int(input('请输入存款金额：'))
        bank[account]['money'] += money
        info = '''
                用户名：%s
                账号:%s
                余额：%s
                '''
        print(info % (bank[account]['username'], account, bank[account]['money']))
    else:
        print('您输入的账号不存在')
        return 0
def lan_qukuan():
    account = int(input("请输入要取款的账号："))
    if account in bank:
        password = int(input("请输入密码："))
        if password == bank[account]["password"]:
            money = int(input("请输入取款金额："))
            if money <= bank[account]["money"]:
                bank[account]["money"] -= money
                info = '''
                        用户名：%s
                        账号：%s
                        余额：%s
                        '''
                print(info % (bank[account]["username"],account,bank[account]["money"]))
            else:
                print("余额不足，请充值")
        else:
            print("密码输入错误")
    else:
        print("您输入的账号不存在")
        return 0
def lan_zhuanzhang():
    taccount = int(input('请输入转出账号：'))
    if taccount in bank:
        gaccount = int(input('请输入转入账号：'))
        if gaccount in bank:
            tpassword = int(input('请输入密码：'))
            if tpassword == bank[taccount]['password']:
                tmoney = int(input('请输入转账金额￥：'))
                if tmoney <= bank[taccount]['money']:
                    bank[taccount]['money'] -= tmoney
                    bank[gaccount]['money'] += tmoney
                    info = '''
                    用户名：%s
                    转出账号:%s
                    转入账号：%s
                    转出金额：%s
                    余额：%s

                    '''
                    print(info % (bank[taccount]['username'], taccount, gaccount, tmoney, bank[taccount]['money']))
                else:
                    print('您的账户余额不足！')
                    return 0
            else:
                print('密码错误！')
                return 0
        else:
            print('您输入的账户不存在！')
            return 0
    else:
        print('您输入的账户不存在！')
        return 0


def lan_chaxun():
    account = int(input('请输入您的账户：'))
    if account in bank:
        password = int(input('请输入密码：'))
        if password == bank[account]['password']:
            info = '''
            --------------以下是您的个人信息---------------
            用户名：%s
            账号：%s
            密码：%s
            余额：%s
            地址：
                国家：%s
                省份：%s
                街道：%s
                门牌号：%s
            开户行：%s
            --------------------------------------------
            '''
            print(info % (bank[account]['username'], account, password, bank[account]['money'],
                          bank[account]['country'], bank[account]['province'], bank[account]['street'],
                          bank[account]['gate'], bank_name))
        else:
            print('密码错误！')
            return 0
    else:
        print('您输入的账号不存在！')
        return 0
while True:
#打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        adduser()
        print(bank)
    elif chose == "2":
        lan_cunkuan()
    elif chose == "3":
        lan_qukuan()
    elif chose == "4":
        lan_zhuanzhang()
    elif chose == "5":
        lan_chaxun()
    elif chose == "6":
        print("欢饮下次光临")
        break
