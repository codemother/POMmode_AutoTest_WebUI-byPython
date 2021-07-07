import unittest
from pom.page_object.login_page import loginpage
from ddt import ddt,file_data
from pom.base.HTMLTestRunner import HTMLTestRunner

def run_test(tcls):
    suite =unittest.TestLoader().loadTestsFromTestCase(tcls)
    with open('../report/loginpage_report.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='登录界面测试报告', description='登录界面所有测试流程中所有测试用例执行信息')
        runner.run(suite)
    f.close()


@run_test
@ddt
class test_login(unittest.TestCase):#以操作流程分类
    #以检测方法不同分方法
    @file_data('../data/login/1checkpoint.yaml')#导入测试用例具体数据
    def test_01_login(self,**kwargs):#只有一个检测点的登录流程测试用例。
        test1 = loginpage(kwargs['browser_type'])
        test1.normal_login(kwargs)
        #如果出现验证框，等待5秒手动解锁
        test1.confirm(kwargs)
        #检测
        test1.judgeExist(kwargs,'excepted1')
        test1.quit()









if __name__ == '__main__':
    # # unittest.main(argv=['ignored', '-v'])
    # with open('../report/loginpage_report.html', 'wb') as f:
    #     runner = HTMLTestRunner(stream=f, verbosity=2, title='登录界面测试报告', description='登录界面所有测试流程中所有测试用例执行信息')
    #     runner.run(suite)
    # f.close()
    unittest.main()

