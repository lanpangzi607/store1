#查询
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_selectUser
ee = [
    [123456789, 123, True],
    [123123123123123123, 123, False],
    [123456789, 122, False],
    [1234567890, 122, False]
]
@ddt
class TestBank3(TestCase):
    @data(*ee)
    @unpack
    def testselectUser(self,a,b,c):
        a = bank_selectUser(a,b)
        self.assertEqual(c,a)








