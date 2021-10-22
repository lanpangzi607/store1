'''
    测试银行：
        使用参数化。
        测试银行的核心业务
'''
from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_addUser

#username, password, country, province, street, door, money
da = [
    ["jason","123456","cn","安徽省","桃源路","s001",6000,1],
    ["jason","123456","cn","安徽省","桃源路","s001",6000,2],
    ["jasons1","123456","cn","安徽省","桃源路","s001",6000,1],
    ["jasons","123456","cn","安徽省","桃源路","s001",6000,3]
]
@ddt
class TestBank(TestCase):
    for i in range(98):
        name = "jason" + str(i)
        bank_addUser(name,"123456","cn","安徽省","桃源路","s001",6000)

    @data(*da)
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h):
        s = bank_addUser(a,b,c,d,e,f,g)
        self.assertEqual(h,s)







