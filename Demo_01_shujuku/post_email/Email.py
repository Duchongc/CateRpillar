# 发送html内容的邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
def sendReport(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'm18625680375_1@163.com'  # 发件地址
    msg['To'] = '1978529954@qq.com;3102733837@qq.com'  # 收件人地址，多人以分号分隔

    smtp = smtplib.SMTP('smtp.163.com')
    smtp.set_debuglevel(1)
    smtp.login('m18625680375_1@163.com', '*****')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

    smtp.quit()
    print('test report has send out!')

