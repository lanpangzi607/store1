import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import unittest
msg_from = "414005477@qq.com"
pwd = "yansdslysvlubhea"
to = "414005477@qq.com"

msg = MIMEMultipart()
msg["From"] = msg_from
msg["to"] = to
msg["Subject"] = Header("主题：测试报告","utf-8")
msg.attach(MIMEText('测试报告','plain','utf-8'))

att = MIMEText(open(r'D:\python\python\day16【自动化测试基础】\day03\autoweb03\账号密码正确的期望结果.html','rb').read(),'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att)

att1 = MIMEText(open(r'D:\python\python\day16【自动化测试基础】\day03\autoweb03\账号或密码不正确的结果.html','rb').read(),'base64','utf-8')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att1)

att2 = MIMEText(open(r'D:\python\python\day16【自动化测试基础】\day03\autoweb03\账号或密码不能为空的结果.html','rb').read(),'base64','utf-8')
att2['Content-Type'] = 'application/octet-stream'
att2['Content-Disposition'] = 'attachment; filename="test.html"'
msg.attach(att2)

ss = smtplib.SMTP_SSL('smtp.qq.com')
ss.connect('smtp.qq.com')
ss.login(msg_from,pwd)
ss.sendmail(msg_from,to,msg.as_string())
