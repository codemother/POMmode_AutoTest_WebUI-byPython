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
    #进入到iframe页
    def switch_to(self,iframe):
        self.driver.switch_to.frame(iframe)
    #退出iframe页
    def switch_out(self):
        self.driver.switch_to.default_content()
    #检测滑动验证框
    def confirm(self,kwargs):
        sleep(1)
        try:
            self.locate((kwargs['confirm']['method'],kwargs['confirm']['content']))
            sleep(5)
        except:
            print('没有出现验证框')
    #检测期望元素是否存在
    def judgeExist(self,kwargs,exceptednum):
        flag = kwargs[exceptednum]['exist?']
        try:
            sleep(0.5)
            self.locate((kwargs[exceptednum]['method'], kwargs[exceptednum]['content']))
        except:
            flag = not flag
        assert flag, kwargs[exceptednum]['wrongmsg']

