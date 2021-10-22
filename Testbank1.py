#存钱
from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_saveMoney
qq = [
    [123456789,123,True],
    [123123123123123123,123,False],
    [123456789,-1,False]
]
@ddt
class TestBank1(TestCase):
    @data(*qq)
    @unpack
    def testsavemoney(self,a,b,c):
        e = bank_saveMoney(a,b)
        self.assertEqual(c,e)


