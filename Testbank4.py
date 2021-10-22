#转账
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_transformMoney
tt = [
    [123456789,1234567890,123,0,0],
    [123456789,1234567890,123,-1,3],
    [1234567891,123456789,123,1,1],
    [123456789,12345678900,123,1,1],
    [123456789,1234567890,111,1,2],
]
@ddt
class TestBank4(TestCase):
    @data(*tt)
    @unpack
    def testtransformMoney(self,a,b,c,d,e):
        a = bank_transformMoney(a,b,c,d)
        self.assertEqual(e,a)
#0是转账成功，1是转出或转入得账号不存在，2输入密码错误，3转账金额不足