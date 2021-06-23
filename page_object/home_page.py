'''
    home_page,首页页面对象类，用于实现在系统的首页各项操作
'''

from pom.base.base_class import baseclass

class home_page(baseclass):
    url ='https://www.xfyun.cn/'
    button_fastlogin =('xpath','//*[@id="__next"]/div[1]/div[1]/div[1]/div/div[2]/a[2]')
    def fastlogin(self):
        self.open(home_page.url)
        self.click(home_page.button_fastlogin)

