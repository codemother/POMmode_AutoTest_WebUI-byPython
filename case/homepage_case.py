'''
    home_page的测试用例实现
'''
import unittest
from pom.page_object.home_page import home_page
from ddt import ddt,file_data

@ddt
class testdemo(unittest.TestCase):
    @file_data('../data/home-fast_login.yaml')
    def test_01_fastlogin(self,browser_type):
        test1 = home_page(browser_type)
        test1.fastlogin()

if __name__ == '__main__':
    unittest.main()