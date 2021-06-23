'''
    base_class,工具类，用于提供各个页面对象所要进行的操作行为，将其封装成各种类型的各种类型的函数便于页面对象调用。
'''
from selenium import webdriver
from time import sleep

#选择浏览器
def browser(type_):
    try:
        driver =getattr(webdriver,type_)()
    except Exception as e:
        print(e)
        driver =webdriver.Chrome()
        driver.implicitly_wait(5)#设置隐式等待时间，防止出现界面还没加载出来报错的情况
    return driver

class baseclass:
    #实例化webdriver
    def __init__(self,type_):
        self.driver =browser(type_)
    #打开网址
    def open(self,url):
        self.driver.get(url)
    #定位元素
    def locate(self,args):
        return self.driver.find_element(*args)
    #输入
    def input(self,args,txt):
        self.locate(args).send_keys(txt)
    #点击
    def click(self,args):
        self.locate(args).click()
    #等待
    def wait(self,time_):
        sleep(time_)
    #退出
    def quit(self):
        self.driver.close()
