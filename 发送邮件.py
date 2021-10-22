import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import unittest
# tests = unittest.defaultTestLoader.discover(r"D:\python\python\day13【单元测试】\代码\day13",pattern="*Test.py")
#
# runner = HTMLTestRunner.HTMLTestRunner(
#     title = "计算器的测试报告",
#     description="这是计算器加法测试报告",
#     verbosity=1,
#     stream = open(file="计算器测试报告.html",mode="w+",encoding="utf-8")
# )
# runner.run(tests)

msg_from = "414005477@qq.com"
pwd = "yansdslysvlubhea"
to = "2431320433@qq.com"

msg = MIMEMultipart()
msg["From"] = msg_from
msg["to"] = to
msg['Subject'] = Header('主题：测试报告','utf-8')
msg.attach(MIMEText('测试报告','plain','utf-8'))

att = MIMEText(open(r'D:\python\python\day14【参数化测试】\代码\ICBC多线程\开户.html','rb').read(),'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att)

att1 = MIMEText(open(r'D:\python\python\day14【参数化测试】\代码\ICBC多线程\取钱.html','rb').read(),'base64','utf-8')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att1)

att2 = MIMEText(open(r'D:\python\python\day14【参数化测试】\代码\ICBC多线程\存钱.html','rb').read(),'base64','utf-8')
att2['Content-Type'] = 'application/octet-stream'
att2['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att2)

att3 = MIMEText(open(r'D:\python\python\day14【参数化测试】\代码\ICBC多线程\查询.html','rb').read(),'base64','utf-8')
att3['Content-Type'] = 'application/octet-stream'
att3['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att3)

att4 = MIMEText(open(r'D:\python\python\day14【参数化测试】\代码\ICBC多线程\转账.html','rb').read(),'base64','utf-8')
att4['Content-Type'] = 'application/octet-stream'
att4['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att4)

ss = smtplib.SMTP_SSL('smtp.qq.com')
ss.connect('smtp.qq.com')
ss.login(msg_from,pwd)
ss.sendmail(msg_from,to,msg.as_string())


