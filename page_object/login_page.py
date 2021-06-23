'''
    login_page,登录页面对象类，用于实现系统的登录业务操作
'''
from pom.base.base_class import baseclass

class loginpage(baseclass):
    url ='https://passport.xfyun.cn/login'#页面的url
    #页面中关联的元素对象,基于base的设计这里要输入元组(定位方式,定位内容)
    user =('id','username')#用户名输入框
    password =('id','password')#密码输入框
    button1 =('xpath','//*[@id="app"]/div/section/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/div[3]')#‘账号密码登录’按钮
    button2 =('xpath','//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/div/form/button') #‘登录’按钮
    #基于元素实现的业务流:此处为账号密码登录
    def normal_login(self,account_txt,password_txt):
        self.open(self.url)
        self.click(self.button1)
        self.input(self.user, account_txt)
        self.input(self.password, password_txt)
        self.click(self.button2)



