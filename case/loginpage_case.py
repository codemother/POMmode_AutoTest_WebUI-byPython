import unittest
from pom.page_object.login_page import loginpage
from ddt import ddt,file_data


@ddt
class testdemo(unittest.TestCase):
    #只有一个检测点的测试用例
    @file_data('../data/login/1checkpoint.yaml')#导入测试用例具体数据
    def test_01_login(self,**kwargs):
        test1 = loginpage(kwargs['browser_type'])
        test1.normal_login(kwargs)
        #如果出现验证框，等待6秒手动解锁
        test1.confirm(kwargs)
        #检测
        test1.judgeExist(kwargs,'excepted1')






if __name__ == '__main__':
    unittest.main()