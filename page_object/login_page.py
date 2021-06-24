'''
    login_page,登录页面对象类，用于实现系统的登录业务操作
'''
from pom.base.base_class import baseclass


class loginpage(baseclass):
    #基于元素实现的业务流:此处为账号密码登录
    def normal_login(self,kwargs):
        self.open(kwargs['url'])
        self.click((kwargs['button1']['method'],kwargs['button1']['content']))
        self.input((kwargs['user']['method'],kwargs['user']['content']),kwargs['account_txt'])
        self.input((kwargs['password']['method'],kwargs['password']['content']),kwargs['password_txt'])
        self.click((kwargs['button2']['method'],kwargs['button2']['content']))



