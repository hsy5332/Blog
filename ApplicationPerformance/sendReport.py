import smtplib
import json
from urllib.parse import quote
from urllib.request import urlopen  # quote,urlopen发送短信的接口使用
from email.mime.text import MIMEText
from email.header import Header

def senderEmail():
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "allencredit@163.com"  # 用户名
    mail_pass = "xiaoxi5332"  # 口令

    sender = 'allencredit@163.com'
    receivers = ['459941505@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")


def sendmessage():
    appkey = "12fa16d0a55a8ef4925ac22825487343"
    mobile = "17721292302"
    tpl_id = "52062"
    tpl_value ='#code#=%s&#company#=JuheData'%("ssss")
    sendurl = 'http://v.juhe.cn/sms/send'  # 短信发送的URL,无需修改

    params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % \
             (appkey, mobile, tpl_id, quote(tpl_value))  # 组合参数

    wp = urlopen(sendurl + "?" + params)
    content = wp.read()  # 获取接口返回内容

    result = json.loads(content)

    if result:
        error_code = result['error_code']
        if error_code == 0:
            # 发送成功
            smsid = result['result']['sid']
            return ("sendsms success,smsid: %s" % (smsid))
        else:
            # 发送失败
            return ("sendsms error :(%s) %s" % (error_code, result['reason']))
    else:
        # 请求失败
        return ("request sendsms error")

senderEmail()
# print(sendmessage())