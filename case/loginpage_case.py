import unittest
from pom.page_object.login_page import loginpage
from ddt import ddt,file_data
from time import sleep

@ddt
class testdemo(unittest.TestCase):
    #login_page测试用例实现

    @file_data('../data/login-normal_login.yaml')#导入测试用例具体数据
    def test_01_login(self,browser_type,account,password):
        test1 = loginpage(browser_type)
        test1.normal_login(account, password)
        #如果出现验证框，等待6秒手动解锁
        try:
            test1.locate(('xpath','/html/body/div[4]/div[1]'))#定位验证框界面的一个元素
            sleep(6)
        except:
            pass

        #能否成功登录判断
        flag =True
        try:
            test1.locate(('xpath','//*[@id="__next"]/div[1]/div[1]/div[1]/div/div[1]'))#定位成功登录以后界面的一个元素
        except:
            flag =False
        excepted =True
        self.assertEqual(excepted,flag,'登陆失败')
if __name__ == '__main__':
    unittest.main()