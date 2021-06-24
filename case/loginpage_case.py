import unittest
from pom.page_object.login_page import loginpage
from ddt import ddt,file_data
from time import sleep


@ddt
class testdemo(unittest.TestCase):
    #成功登录的测试用例
    @file_data('../data/login/success_login.yaml')#导入测试用例具体数据
    def test_01_login(self,**kwargs):
        test1 = loginpage(kwargs['browser_type'])
        test1.normal_login(kwargs)
        #如果出现验证框，等待6秒手动解锁
        try:
            # iframe =test1.locate(('xpath','/iframe'))
            # test1.switch_to(iframe)
            # test1.locate(('class','geetest_slider_button'))#定位验证框界面的一个元素
            sleep(6)
        except Exception as r:
            print(r)

        #能否成功登录判断
        flag =True
        try:
            test1.locate((kwargs['excepted']['method'],kwargs['excepted']['content']))#定位成功登录以后界面的一个元素
        except:
            flag =False
        self.assertTrue(flag,'无法正常登录，测试不通过')

    @file_data('../data/login/unsuccess_login.yaml')
    def test_02_login(self,**kwargs):
        test2 =loginpage(kwargs['browser_type'])
        test2.normal_login(kwargs)
        sleep(6)



if __name__ == '__main__':
    unittest.main()