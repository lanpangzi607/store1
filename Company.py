# author:jason
import random
from DBUtils1 import select
from DBUtils1 import update

# 银行库
bank = {}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye"}  # 银行业务选项
# 开户成功的信息模板
myinfo = '''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
'''

# 欢迎模板
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''


def print_welcome():
    print(welcome, end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i, bank_choice[i]))
    print("**********************************")


# 输入帮助方法：chose是打印选项
def inputHelp(chose, datatype="str"):
    while True:
        print("请输入", chose, ":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i


# 判断是否存在该银行选项
def isExists(chose, data):
    if chose in data:
        return True
    return False


# 获取随机码
def getRandom():
    li = "0123456789"
    global string
    string = ""
    for i in range(8):
        string = string + li[int(random.random() * len(li))]
    return string


# 通过账号获取账户信息
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"] == account:
            return i
    return None


# 银行的开户方法
def bank_addUser(username, password, country, province, street, door, money):
    # 查询是否已满
    sql1 = "select count(*) from user"
    param1 = []
    data = select(sql1,param1) # ((100),)
    if data[0][0] >= 100:
        return 3

    # 查询是否存在
    sql2 = "select * from user where username  = %s"
    param2 = [username]
    data2 = select(sql2, param2)  # ("adfadf","贾生","adsfadsfa")
    if len(data2) != 0:
        return 2

    # 插入数据
    sql3 = "insert into user  values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [getRandom(), username, password, country, province, street, door, money, bank_name]
    update(sql3, param3)
    return 1


# 银行的存钱方法
def bank_saveMoney(ac, money):
    sql = "select account from user where account = %s"
    param =[ac]
    date = select(sql,param)
    if date[0][0] == ac:
        sql4 = "update user set money = money+%s where account = %s"
        param4 = [money, ac]
        update(sql4, param4)
        return True
    else:
        return False

# 银行的查询功能
def bank_selectUser(account, password):
    # uname = findByAccount(account)
    sql = "select account,password1 from user where account = %s and password1 = %s"
    param = [account,password]
    date = select(sql,param)

    if date[0][0] == account:
        if password == date[0][1]:
            sql2 = "select account,username, money from user where account = %s and password1 = %s"
            param2 = [account, password]
            date2 = select(sql2, param2)
            print(date2)

        else:
            print("用户密码错误！")
    else:
        print("该用户不存在！")


# 银行的取钱功能
def bank_takeMoney(ac, password, money):
    sql = "select account,password1,money from user where account = %s"
    param = [ac]
    date = select(sql, param)
    if date[0][0] == ac:
        print(type(date[0][1]))
        if date[0][1] == password:
            if date[0][2] < money:
                return 3
            else:
                sql2 = "update user set money = money - %s where account = %s"
                param2 = [money, ac]
                update(sql2, param2)
                return 0
        else:
            return 2
    else:
        return 1


# 银行的转账功能
def bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney):
    sql = "select account,password1,money from user where account = %s"
    param = [outputaccount]
    date = select(sql, param)
    sql2 ="select account,money from user where account = %s"
    param2 =[inputaccount]
    date2 = select(sql2, param2)
    if date[0][0] == outputaccount:
        if date[0][1] == outputpassword:
            if date2[0][0] == inputaccount:
                if date[0][2] >= outputmoney:
                    bank_takeMoney(date[0][0], date[0][1], outputmoney)
                    bank_saveMoney(date2[0][0], outputmoney)
                    return 0
                else:
                    return 3
            else:
                return 1
        else:
            return 2
    else:
        return 1


# 开户方法
def addUser():
    username = inputHelp("用户名")
    password = inputHelp("密码", "int")
    country = inputHelp("居住地址：1.国家：")
    province = inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money = inputHelp("银行卡余额", "int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(username, password, country, province, street, door, money)
    # 判断1   2   3
    if status == 1:

        print("恭喜开户成功！以下是您的开户信息：")
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
        print(info % (username,string,password,money,country,province,street,door,bank_name))


    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")


# 存钱
def saveMoney():
    account = inputHelp("账号")
    m = inputHelp("存入的金额", "int")

    flag = bank_saveMoney(account, m)

    if flag == True:
        print("存储成功!您的个人信息为：")
        sql = "select username,money from user where account = %s"
        param = [account]
        date = select(sql, param)
        info = '''
                        用户名：%s
                        账号:%s
                        余额：%s
                        '''
        print(info % (date[0][0], account, date[0][1]))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")
    return 1


# 取钱
def takeMoney():
    account = inputHelp("账户")
    password = inputHelp("密码", "int")
    money = inputHelp("取出金额", "int")

    f = bank_takeMoney(account, password, money)

    if f == 1:
        print("改用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account, password)


# 转账功能
def transformMoney():
    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputpass = inputHelp("转出的密码", "int")
    outputmoney = inputHelp("要转出的金额", "int")

    f = bank_transformMoney(output, input, outputpass, outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    elif f == 0:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(output, outputpass)


# 查询账户方法
def selectUser():
    account = inputHelp("账号")
    password = inputHelp("密码", "int")
    # sql = "select account,username,money from user where account = %s and password = %s"
    # param = [account, password]
    # date = select(sql, param)
    # print(date)
    bank_selectUser(account, password)


# 核心程序
while True:

    print_welcome()
    chose = inputHelp("选项")
    if isExists(chose, bank_choice):
        if chose == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transformMoney()
        elif chose == "5":
            selectUser()
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")