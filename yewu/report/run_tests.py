import time, sys
from yewu.report.HTMLTestRunner import HTMLTestRunner
import unittest
#指定测试用例为当前文件夹下的interface目录
test_dir='../../cases'
discover= unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

if __name__=='__main__':
    #test_data.init_data() #初始化接口测试数据
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename='./result/'+now+'_result.html'

    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='Guest Manage System Inteface Test Report',description='Implementation Example with:')
    runner.run(discover)
    fp.close()