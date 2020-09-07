# coding:utf-8
#import unittest
import pytest
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from report.HTMLTestRunner import HTMLTestRunner
from cases.all_cases import run_all
current_path = os.getcwd()  # 当前文件路径
report_path = os.path.join(current_path, "report")
# 测试报告为result.html
#now=time.strftime("%Y-%m-%d %H_%M_%S")
#filename='./result/'+now+'_result.html'
#result_path = os.path.join(report_path, "result.html")

# 加载全部用例
'''
def all_case():
    #case_path = os.path.join(current_path, "cases")  # 用例路径
    case_path = '../cases'
    discover = pytest.main(case_path,pattern="test_*.py")
    return discover
'''

def send_email(smtpserver, port, sender, psw, receiver):
    # 写信模板
    msg = MIMEMultipart()
    msg['Subject'] = "这是wangyiyun项目的自动化测试报告"
    msg['From'] = sender
    msg['to'] = receiver

    # 通过os获取文件路径
    annex = open('report-all.html', "r", encoding="utf-8").read()  # 附件，打开并且读取测试报告

    main_body = '<pre><h1>这是wangyiyun项目的自动化测试报告，请查阅！`</h1></pre>'  # 正文的内容

    # 添加正文到容器
    body = MIMEText(main_body, "html", "utf-8")
    msg.attach(body)

    # 添加附件到容器
    att = MIMEText(annex, "base64", "utf-8")
    att["Content-Type"] = "application/octet-sream"
    att["Content-Disposition"] = 'attachment;filename="wangyiyun_test_report.html"'  # 附件名称
    msg.attach(att)

    # 连接发送邮件
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    run_all()
    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    #fp = open(filename, "wb")  # 打开result.html，把测试结果写进去
    #runner = HTMLTestRunner(stream=fp, title='Guest Manage System Inteface Test Report',
                            #description='Implementation Example with:')
    # 调用all_case函数返回值
    #runner.run(all_case())
    # 有开有闭，关闭刚才打开的文件
    #fp.close()

    # 发送邮件
    send_email("smtp.qq.com", 465, "3061505036@qq.com", "bzaibbqrtnmhddaf", "3061505036@qq.com")