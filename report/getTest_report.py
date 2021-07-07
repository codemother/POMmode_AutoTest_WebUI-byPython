# import unittest
# from pom.base.HTMLTestRunner import HTMLTestRunner
# if __name__ =='__main__':
#     discover1 =unittest.defaultTestLoader.discover('../case',pattern='login')
#     print(discover1)
#     with open('./loginpage_report.html','wb') as f:
#         runner =HTMLTestRunner(stream=f,verbosity=2,title='登录界面测试报告',description='登录界面所有测试流程中所有测试用例执行信息')
#         runner.run(discover1)
#     f.close()
'''
这里不能用discover导入测试代码，这里待编写合适的代码来实现对所有测试用例的一键测试、生成报告
'''