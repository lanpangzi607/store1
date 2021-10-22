#取钱
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_takeMoney
ww = [
    [123456789,123,6001,3],
    [123123123123123123,123,100,1],
    [123456789,122,1,2],
    [123456789,123,5999,0],
    [1234567890,123,6000,0],
    [123456789,123,-1,3],
    [123456789,123,1,0]
]
@ddt
class TestBank2(TestCase):
    @data(*ww)
    @unpack
    def testtakemoney(self,a,b,c,d):
        r = bank_takeMoney(a,b,c)
        self.assertEqual(d,r)
#0是取钱成功，1是账号不存在，2是密码错误，3是余额不足
