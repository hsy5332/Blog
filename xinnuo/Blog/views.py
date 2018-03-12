import time
import json
import pdb
# pdb.set_trace()
from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import quote
from urllib.request import urlopen  # quote,urlopen发送短信的接口使用
from random import randint  # random.randint是随机取数的，发送短信的接口使用

from Blog import models


def index(request):
    user = models.user.objects.get(id=1)

    return render(request, 'index.html', {"TEST": user})


# token计算规则
def token(token):
    try:
        if int(token) + 86400 > int(time.time()):  # 86400是一天的时间戳
            return True
        else:
            return False
    except:
        return False


# 登录接口

def login(request):
    if request.POST:
        try:
            if token(request.POST['token']):
                try:
                    userinfo = models.user.objects.get(username=request.POST['username'],
                                                       password=request.POST['password'])
                    # 判断用户信息是否在数据库中存在
                    # return HttpResponse("Success！")
                    # 返回json字符串方法：  (实际开发可以不返回，前端根据userinfo取出对应value)

                    login_userinfo = {
                        'code': '200',
                        'msg': 'Success！',
                        'data': {'userid': str(userinfo.id), 'username': userinfo.username,
                                 'phonenumber': userinfo.phonenumber, }  # 实际开发中，可直接返回一个字典
                    }
                    return HttpResponse(json.dumps(login_userinfo))
                except:
                    login_userInfoerror = {'code': '201', 'msg': '用户名或密码错误！', 'data': ''}
                    return HttpResponse(json.dumps(login_userInfoerror))
            else:
                login_tokenInvalid = {"code": "-11", "msg": "token过期", "data": {}}
                return HttpResponse(json.dumps(login_tokenInvalid))
        except:
            login_tokenError = {'code': "-10", 'msg': 'ERROR', 'data': ''}
            return HttpResponse(json.dumps(login_tokenError))
    else:
        login_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(login_requesterror))


# 注册接口

def register(request):
    # request.encoding='utf-8'
    if request.POST:
        try:
            postUsername = models.user.objects.get(username=request.POST['username'])  # 这个就能判断用户名是否存在
            register_userInfoerror = {'code': '202', 'msg': '该用户名已经存在！', 'data': ''}
            return HttpResponse(json.dumps(register_userInfoerror))
        except:
            try:
                phonenumber = models.user.objects.get(phonenumber=request.POST['phonenumber'])
                register_phoneNumberoccupy = {'code': '203', 'msg': '该手机号已经使用了！', 'data': ''}  # Occupy占用
                return HttpResponse(json.dumps(register_phoneNumberoccupy))
            except:
                try:
                    if len(request.POST['phonenumber']) >= 11:  # 判断手机号长度
                        try:
                            phoneStatus = models.phone_status.objects.get(
                                phonenumber=request.POST['phonenumber'])  # 判断手机号是否存在phone_status表中
                            if int(phoneStatus.status) == 1:  # 判断手机号是否被锁定
                                # pdb.set_trace()
                                try:
                                    phoneMessage = models.phone_message.objects.get(
                                        phonenumber=request.POST['phonenumber'], mcodestatus=1,
                                        usein='R')  # 判断phoneMessage是否有短信验证码
                                    if 'messagecode' in request.POST:
                                        if str(phoneMessage.messagecode) == request.POST['messagecode']:
                                            models.user.objects.create(username=request.POST['username'],
                                                                       password='123',
                                                                       realname=request.POST['username'],
                                                                       nickname=request.POST['username'],
                                                                       phonenumber=request.POST['phonenumber'], sex='1',
                                                                       userstatus='1',
                                                                       birthday=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                              time.localtime()),
                                                                       createdtime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                 time.localtime()),
                                                                       updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                time.localtime()))
                                            models.phone_message.objects.filter(
                                                phonenumber=request.POST['phonenumber']).update(
                                                mcodestatus='0', updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                          time.localtime()))
                                            register_messagecode = {'code': '200', 'msg': 'Success！',
                                                                    'data': ''}
                                            return HttpResponse(json.dumps(register_messagecode))
                                        else:
                                            register_phoneNumbererror = {'code': '214', 'msg': '请输入正确的手机验证码!',
                                                                         'data': ''}
                                            return HttpResponse(json.dumps(register_phoneNumbererror))
                                    else:
                                        register_notMessagecode = {'code': '-10', 'msg': 'ERROR', 'data': ''}
                                        return HttpResponse(json.dumps(register_notMessagecode))
                                except:
                                    register_notReceivedcode = {'code': '204', 'msg': '没有获取到手机验证码，请重试。',
                                                                'data': ''}  # Receive收到
                                    return HttpResponse(json.dumps(register_notReceivedcode))
                            else:
                                register_phonelocking = {'code': '205', 'msg': '该手机号已经被锁定，请解锁后再操作。', 'data': ''}
                                return HttpResponse(json.dumps(register_phonelocking))
                        except:
                            try:
                                phoneMessage = models.phone_message.objects.get(
                                    phonenumber=request.POST['phonenumber'],
                                    mcodestatus=1, usein='R')  # 判断phoneMessage是否有短信验证码
                                if 'messagecode' in request.POST:
                                    if str(phoneMessage.messagecode) == request.POST['messagecode']:
                                        models.user.objects.create(username=request.POST['username'],
                                                                   password='123',
                                                                   realname=request.POST['username'],
                                                                   nickname=request.POST['username'],
                                                                   phonenumber=request.POST['phonenumber'], sex='1',
                                                                   userstatus='1',
                                                                   birthday=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                          time.localtime()),
                                                                   createdtime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                             time.localtime()),
                                                                   updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                            time.localtime()))
                                        models.phone_message.objects.filter(
                                            phonenumber=request.POST['phonenumber']).update(
                                            mcodestatus='0', updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                      time.localtime()))
                                        register_messagecode = {'code': '200', 'msg': 'Success！',
                                                                'data': ''}
                                        return HttpResponse(json.dumps(register_messagecode))
                                    else:
                                        register_phoneNumbererror = {'code': '214', 'msg': '请输入正确的手机验证码!', 'data': ''}
                                        return HttpResponse(json.dumps(register_phoneNumbererror))
                                else:
                                    register_notMessagecode = {'code': '-10', 'msg': 'ERROR', 'data': ''}
                                    return HttpResponse(json.dumps(register_notMessagecode))
                            except:
                                register_notReceivedcode = {'code': '204', 'msg': '没有获取到手机验证码，请重试。',
                                                            'data': ''}  # Receive收到
                                return HttpResponse(json.dumps(register_notReceivedcode))
                    else:
                        register_Phonewrongful = {'code': '206', 'msg': '请输入正确的手机号！', 'data': ''}  # wrongful不合法
                        return HttpResponse(json.dumps(register_Phonewrongful))
                except:
                    try:
                        if "@" in request.POST['email']:
                            try:
                                if models.user.objects.filter(emailaddress=request.POST['email']):
                                    register_errorMail = {'code': '213', 'msg': '邮箱已经存在!', 'data': ''}
                                    return HttpResponse(json.dumps(register_errorMail))
                                else:
                                    try:
                                        eMail = models.mail.objects.get(email=request.POST['email'], ecodestatus=1,
                                                                        usein='R')  # 判断是否有验证码
                                        if str(eMail.emailcode) == request.POST['emailcode']:
                                            models.user.objects.create(username=request.POST['username'],
                                                                       password='123',
                                                                       realname=request.POST['username'],
                                                                       nickname=request.POST['username'],
                                                                       emailaddress=request.POST['email'], sex='1',
                                                                       userstatus='1',
                                                                       birthday=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                              time.localtime()),
                                                                       createdtime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                 time.localtime()),
                                                                       updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                time.localtime()))
                                            models.mail.objects.filter(email=request.POST['email']).update(
                                                ecodestatus='0', updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                          time.localtime()))
                                            register_Mailcode = {'code': '200', 'msg': 'Success', 'data': ''}
                                            return HttpResponse(json.dumps(register_Mailcode))
                                        else:
                                            register_errorMailcode = {'code': '212', 'msg': '请输入正确的邮箱验证码!', 'data': ''}
                                            return HttpResponse(json.dumps(register_errorMailcode))
                                    except:
                                        register_notReceivedMailcode = {'code': '207', 'msg': '没有获取到邮箱验证码，请重试。',
                                                                        'data': ''}
                                        return HttpResponse(json.dumps(register_notReceivedMailcode))
                            except:
                                register_mailwrongful = {'code': '208', 'msg': '请输入正确的邮箱地址！', 'data': ''}
                                return HttpResponse(json.dumps(register_mailwrongful))
                        else:
                            register_mailwrongful = {'code': '208', 'msg': '请输入正确的邮箱地址！', 'data': ''}
                            return HttpResponse(json.dumps(register_mailwrongful))
                    except:
                        register_mailPhonewrongful = {'code': '209', 'msg': '请输入邮箱或者手机号！', 'data': ''}
                        return HttpResponse(json.dumps(register_mailPhonewrongful))

    else:
        register_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(register_requesterror))


# 忘记密码接口

def forgotpassword(request):
    if request.POST:
        if 'phonenumber' in request.POST:
            if len(request.POST['phonenumber']) >= 11:  # 判断手机号是否合法
                try:
                    forgotusername = models.user.objects.get(username=request.POST['username'],
                                                             phonenumber=request.POST['phonenumber'])  # 判断用户名和手机是否匹配
                    try:
                        forgotphonecode = models.phone_message.objects.get(phonenumber=request.POST['phonenumber'],
                                                                           messagecode=request.POST['messagecode'],
                                                                           mcodestatus='1',
                                                                           usein='F')  # 判断是否phone_message有验证码
                        # forgotuserinfo = models.user.objects.get(username=request.POST['username'])
                        forgotpassword_success = {'code': '200', 'msg': 'Success!',
                                                  'data': ''}  # 后期可考虑返回一个token，前端进入修改密码页面时可用这个，或者返回用户名和密码。
                        return HttpResponse(json.dumps(forgotpassword_success))
                    except:
                        forgotpassword_userNotmatching = {'code': '204', 'msg': '没有获取到手机验证码，请重试。', 'data': ''}
                        return HttpResponse(json.dumps(forgotpassword_userNotmatching))
                except:
                    forgotpassword_userNotmatching = {'code': '201', 'msg': '用户名和手机号不匹配！', 'data': ''}  # 用户名和密码不匹配
                    return HttpResponse(json.dumps(forgotpassword_userNotmatching))
            else:
                forgotpassword_Phonewrongful = {'code': '206', 'msg': '请输入正确的手机号！', 'data': ''}
                return HttpResponse(json.dumps(forgotpassword_Phonewrongful))

        elif 'email' in request.POST:  # 判断邮箱是否合法
            if '@' in request.POST:
                try:
                    forgotpassword_email = models.user.objects.get(username=request.POST['username'],
                                                                   emailaddress=request.POST['email'])  # 判断用户名和邮箱地址是否匹配
                    try:
                        forgotpassword_emailcode = models.mail.objects.get(email=request.POST['email'],
                                                                           emailcode=request.POST['emailcode'],
                                                                           ecodestatus=1, usein='F')
                        # forgotuserinfo = models.user.objects.get(username=request.POST['username'])
                        forgotpassword_success = {'code': '200', 'msg': 'Success!',
                                                  'data': ''}  # 后期可考虑返回一个token，前端进入修改密码页面时可用这个，或者返回用户名和密码。
                        return HttpResponse(json.dumps(forgotpassword_success))
                    except:
                        forgotpassword_userNotmatching = {'code': '207', 'msg': '没有获取到邮箱验证码，请重试。', 'data': ''}
                except:
                    forgotpassword_mailwrongful = {'code': '211', 'msg': '用户名和邮箱地址不匹配！', 'data': ''}
                    return HttpResponse(json.dumps(forgotpassword_mailwrongful))
            else:
                forgotpassword_mailerror = {'code': '208', 'msg': '请输入正确的邮箱地址！', 'data': ''}
                return HttpResponse(json.dumps(forgotpassword_mailerror))
        else:
            forgotpassword_requestwrong = {"code": "-12", "msg": "请求方式错误！", "data": {}}
            return HttpResponse(json.dumps(forgotpassword_requestwrong))


# 使用聚合的方法 发送短信方法
def sendsms(appkey, mobile, tpl_id, tpl_value):
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


# 邮箱验证码获取方法

# 手机验证码获取接口（注册、忘记密码、修改密码）
def achievemessagecode(request):
    if request.POST:
        randintnumber = randint(1000, 9000)  # 生成随机数发给短信商
        # 聚合发送短信appkey配置
        sendsmsconfigure = {
            'appkey': '12fa16d0a55a8ef4925ac22825487343',
            'mobile': '17721292302',
            'tpl_id': '52062',
            'tpl_value': '#code#=%s&#company#=JuheData' % (randintnumber),
        }
        if 'usein' in request.POST and 'phonenumber' in request.POST:
            if request.POST['usein'] == 'R' and len(
                    request.POST['phonenumber']) >= 11:  # 注册 and request.POST['operator'] == 'juhe' 后期不同运营，搭配使用
                # achievemessagecode_sendsms = sendsms(sendsmsconfigure.get('appkey'), sendsmsconfigure.get('mobile'), sendsmsconfigure.get('tpl_id'),sendsmsconfigure.get('tpl_value'))
                # if 'smsid' in achievemessagecode_sendsms:#判断第三方是否获取到验证码
                try:
                    models.phone_message.objects.filter(phonenumber=request.POST['phonenumber']).filter(
                        usein='R').filter(mcodestatus=1).update(mcodestatus=0,
                                                                updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                         time.localtime()))  # 更新数据库usein='R',mcodestatus=1的数据把mcodestatus=0
                    models.phone_message.objects.create(phonenumber=request.POST['phonenumber'],
                                                        messagecode=randintnumber, usein='R', mcodestatus=1,
                                                        createdtime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime()),
                                                        updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                 time.localtime()))  # 创建数据，生成验证码
                    achievemessagecode_success = {'code': '200', 'msg': 'Success！', 'data': ''}
                    return HttpResponse(json.dumps(achievemessagecode_success))
                except:
                    achievemessagecode_createdDataerror = {"code": "-13", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(achievemessagecode_createdDataerror))
                    # else:
                    # achievemessagecode_sendsmserror = {'code' : '204', 'msg' : '没有获取到手机验证码，请重试', 'data' : ''}
                    # return HttpResponse(json.dumps(achievemessagecode_sendsmserror))
                    # 上面注释的代码 是获取第三方的code，所有注释，记得删除
            elif request.POST['usein'] == 'F' and len(request.POST['phonenumber']) >= 11:  # 忘记密码
                # achievemessagecode_sendsms = sendsms(sendsmsconfigure.get('appkey'), sendsmsconfigure.get('mobile'), sendsmsconfigure.get('tpl_id'),sendsmsconfigure.get('tpl_value'))
                # if 'smsid' in achievemessagecode_sendsms:#判断第三方是否获取到验证码
                try:
                    models.phone_message.objects.filter(phonenumber=request.POST['phonenumber']).filter(
                        usein='F').filter(mcodestatus=1).update(mcodestatus=0,
                                                                updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                         time.localtime()))  # 更新数据库usein='F',mcodestatus=1的数据把mcodestatus=0
                    models.phone_message.objects.create(phonenumber=request.POST['phonenumber'],
                                                        messagecode=randintnumber, usein='F', mcodestatus=1,
                                                        createdtime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime()),
                                                        updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                 time.localtime()))  # 创建数据，生成验证码
                    achievemessagecode_success = {'code': '200', 'msg': 'Success！', 'data': ''}
                    return HttpResponse(json.dumps(achievemessagecode_success))
                except:
                    achievemessagecode_createdDataerror = {"code": "-13", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(achievemessagecode_createdDataerror))
                    # else:
                    # achievemessagecode_sendsmserror = {'code' : '204', 'msg' : '没有获取到手机验证码，请重试', 'data' : ''}
                    # return HttpResponse(json.dumps(achievemessagecode_sendsmserror))
            elif request.POST['usein'] == 'M':  # 修改密码
                # achievemessagecode_sendsms = sendsms(sendsmsconfigure.get('appkey'), sendsmsconfigure.get('mobile'), sendsmsconfigure.get('tpl_id'),sendsmsconfigure.get('tpl_value'))
                # if 'smsid' in achievemessagecode_sendsms:#判断第三方是否获取到验证码
                try:
                    models.phone_message.objects.filter(phonenumber=request.POST['phonenumber']).filter(
                        usein='M').filter(mcodestatus=1).update(mcodestatus=0,
                                                                updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                         time.localtime()))  # 更新数据库usein='M',mcodestatus=1的数据把mcodestatus=0
                    models.phone_message.objects.create(phonenumber=request.POST['phonenumber'],
                                                        messagecode=randintnumber, usein='M', mcodestatus=1,
                                                        createdtime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime()),
                                                        updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                 time.localtime()))  # 创建数据，生成验证码
                    achievemessagecode_success = {'code': '200', 'msg': 'Success！', 'data': ''}
                    return HttpResponse(json.dumps(achievemessagecode_success))
                except:
                    achievemessagecode_createdDataerror = {"code": "-13", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(achievemessagecode_createdDataerror))
                    # else:
                    # achievemessagecode_sendsmserror = {'code' : '204', 'msg' : '没有获取到手机验证码，请重试', 'data' : ''}
                    # return HttpResponse(json.dumps(achievemessagecode_sendsmserror))
            else:
                achieveMessagecode_requesterror = {'code': '-10', 'msg': 'ERROR！', 'data': ''}
                return HttpResponse(json.dumps(achieveMessagecode_requesterror))
        elif 'usein' in request.POST and 'email' in request.POST:
            if '@' in request.POST['email'] and request.POST['usein'] == 'R':
                try:
                    models.mail.objects.filter(email=request.POST['email']).filter(ecodestatus=1).filter(
                        usein='R').update(ecodestatus=0, updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime()))  # 更新数据库 userin='R' ecodestatus=1的数据
                    models.mail.objects.create(email=request.POST['email'], emailcode=randintnumber, ecodestatus=1,
                                               usein='R',
                                               createdtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                               updatetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 插入数据
                    achievemessagecode_success = {'code': '200', 'msg': 'Success！', 'data': ''}
                    return HttpResponse(json.dumps(achievemessagecode_success))
                except:
                    achievemessagecode_createdDataerror = {"code": "-13", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(achievemessagecode_createdDataerror))
            elif '@' in request.POST['email'] and request.POST['usein'] == 'F':
                try:
                    models.mail.objects.filter(email=request.POST['email']).filter(ecodestatus=1).filter(
                        usein='F').update(ecodestatus=0, updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime()))  # 更新数据库 userin='F' ecodestatus=1的数据
                    models.mail.objects.create(email=request.POST['email'], emailcode=randintnumber, ecodestatus=1,
                                               usein='F',
                                               createdtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                               updatetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 插入数据
                    achievemessagecode_success = {'code': '200', 'msg': 'Success！', 'data': ''}
                    return HttpResponse(json.dumps(achievemessagecode_success))
                except:
                    achievemessagecode_createdDataerror = {"code": "-13", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(achievemessagecode_createdDataerror))
            elif '@' in request.POST['email'] and request.POST['usein'] == 'M':
                try:
                    models.mail.objects.filter(email=request.POST['email']).filter(ecodestatus=1).filter(
                        usein='M').update(ecodestatus=0, updatetime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime()))  # 更新数据库 userin='M' ecodestatus=1的数据
                    models.mail.objects.create(email=request.POST['email'], emailcode=randintnumber, ecodestatus=1,
                                               usein='M',
                                               createdtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                               updatetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 插入数据
                    achievemessagecode_success = {'code': '200', 'msg': 'Success！', 'data': ''}
                    return HttpResponse(json.dumps(achievemessagecode_success))
                except:
                    achievemessagecode_createdDataerror = {"code": "-13", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(achievemessagecode_createdDataerror))
            else:
                register_mailwrongful = {'code': '208', 'msg': '请输入正确的邮箱地址！', 'data': ''}
                return HttpResponse(json.dumps(register_mailwrongful))
        else:
            achieveMessagecode_requesterror = {'code': '-10', 'msg': 'ERROR！', 'data': ''}
            return HttpResponse(json.dumps(achieveMessagecode_requesterror))
    else:
        achieveMessagecode_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(achieveMessagecode_requesterror))


# home配置接口
def configure(request):
    if request.POST:
        try:
            configureinfo = models.link_configure.objects.get(position=request.POST['position'],
                                                              number=request.POST['number'], configurestatus=1)
            configure_info = {
                "code": "200",
                "msg": "Success！",
                "data": [{
                    "position": configureinfo.position,
                    "number": configureinfo.number,
                    "url": configureinfo.url,
                    "picture": configureinfo.picture
                }
                ]
            }
            return HttpResponse(json.dumps(configure_info))
        except:
            configure_createdDataerror = {"code": "-10", "msg": "ERROR！", "data": {}}
            return HttpResponse(json.dumps(configure_createdDataerror))
    else:
        configure_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(configure_requesterror))


# 搜索接口
def search(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                datasource = models.article.objects.filter(articletitle__contains=request.POST['keyword'],
                                                           articlestatus=1)
                returnkey = ["articleid", "articletitle", "articlecontent", "authorid", "author", "classifyid",
                             "coverpicture", "createdtime", "updatetime"]
                # 创建一个key的列表
                returnvalues = []
                # 创建一个values的列表
                returndic = {}
                # 创建字典，在遍历的时候，把单组的数据存入字典，再清空字典
                returndata = []
                # 把遍历得来的字典存入列表作为返回数据
                for x in datasource:
                    try:
                        author_nickname = models.user.objects.get(
                            id=x.authorid).nickname  # 查询user表，把author获取出来。（articleid需要转换类型）
                    except:
                        author_nickname = ""
                    cachevalues = x.articleid, x.articletitle, x.articlecontent, x.authorid, author_nickname, x.classifyid, x.coverpicture, x.createdtime, x.updatetime
                    returnvalues.append(cachevalues)
                for j in returnvalues:
                    for a, b in zip(j, returnkey):
                        returndic[b] = a
                    returndata.append(returndic)
                    returndic = {}
                # 三个for循环实现 返回数据（returndata）
                search_data = {"code": "200", "msg": "Success！", "data": returndata}
                return HttpResponse(json.dumps(search_data))
            except:
                search_createdDataerror = {"code": "-10", "msg": "ERROR！", "data": {}}
                return HttpResponse(json.dumps(search_createdDataerror))
        else:
            search_tokenInvalid = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(search_tokenInvalid))
    else:
        search_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(search_requesterror))


# 文章详情页接口
def details(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                articleinfo = models.article.objects.get(articleid=request.POST['articleid'])
                author = models.user.objects.get(id=str(articleinfo.authorid))
                articleDetailsdata = {
                    "articleid": articleinfo.articleid,
                    "articletitle": articleinfo.articletitle,
                    "articlecontent": articleinfo.articlecontent,
                    "authorid": articleinfo.authorid,
                    "author": author.nickname,
                    "classifyid": articleinfo.classifyid,
                    "coverpicture": articleinfo.coverpicture,
                    "updatetime": articleinfo.updatetime,
                    "createdtime": articleinfo.createdtime
                }
                returndata = {"code": "200", "msg": "Success！", "data": articleDetailsdata}
                return HttpResponse(json.dumps(returndata))
            except:
                details_createdDataerror = {"code": "-10", "msg": "ERROR！", "data": {}}
                return HttpResponse(json.dumps(details_createdDataerror))
        else:
            articledetails_tokenInvalid = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(articledetails_tokenInvalid))
    else:
        articledetails_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(articledetails_requesterror))


# 创建文章
def createarticle(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if 'coverpicture' in request.POST:
                    models.article.objects.create(articletitle=request.POST['articletitle'],
                                                  articlecontent=request.POST['articlecontent'],
                                                  authorid=request.POST['authorid'],
                                                  classifyid=request.POST['classifyid'],
                                                  articlestatus=1,
                                                  coverpicture=request.POST['coverpicture'],
                                                  createdtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                                  updatetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    createdarticle = models.article.objects.filter(authorid=request.POST['authorid']).filter(
                        articletitle=request.POST['articletitle']).order_by('-articleid')[0]
                    authorinfo = models.user.objects.get(id=createdarticle.authorid)
                    Articledata = {
                        "articleid": createdarticle.articleid,
                        "articletitle": createdarticle.articletitle,
                        "articlecontent": createdarticle.articlecontent,
                        "authorid": createdarticle.authorid,
                        "author": authorinfo.nickname,
                        "classifyid": createdarticle.classifyid,
                        "coverpicture": createdarticle.coverpicture,
                        "updatetime": createdarticle.updatetime,
                        "createdtime": createdarticle.createdtime
                    }
                    returnArticledata = {"code": "200", "msg": "Success！", "data": Articledata}
                    return HttpResponse(json.dumps(returnArticledata))
                else:
                    models.article.objects.create(articletitle=request.POST['articletitle'],
                                                  articlecontent=request.POST['articlecontent'],
                                                  authorid=request.POST['authorid'],
                                                  classifyid=request.POST['classifyid'],
                                                  articlestatus=1,
                                                  createdtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                                  updatetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

                    createdarticle = models.article.objects.filter(authorid=request.POST['authorid']).filter(
                        articletitle=request.POST['articletitle']).order_by('-articleid')[0]
                    authorinfo = models.user.objects.get(id=createdarticle.authorid)
                    Articledata = {
                        "articleid": createdarticle.articleid,
                        "articletitle": createdarticle.articletitle,
                        "articlecontent": createdarticle.articlecontent,
                        "authorid": createdarticle.authorid,
                        "author": authorinfo.nickname,
                        "classifyid": createdarticle.classifyid,
                        "coverpicture": createdarticle.coverpicture,
                        "updatetime": createdarticle.updatetime,
                        "createdtime": createdarticle.createdtime
                    }
                    returnArticledata = {"code": "200", "msg": "Success！", "data": Articledata}
                    return HttpResponse(json.dumps(returnArticledata))
            except:
                createarticle_createdDataerror = {"code": "-10", "msg": "ERROR！", "data": {}}
                return HttpResponse(json.dumps(createarticle_createdDataerror))
        else:
            createarticle_tokenInvalid = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(createarticle_tokenInvalid))
    else:
        articledetails_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(articledetails_requesterror))


# 编辑文章接口
def editarticle(request):
    if request.POST:
        if token(request.POST['token']):
            try:
                if request.POST['articletitle'] == "" or request.POST['articlecontent'] == "":
                    editarticle_titleContentnull = {"code": "215", "msg": "文章标题或文章内容不能为空！", "data": {}}
                    return HttpResponse(json.dumps(editarticle_titleContentnull))
                else:
                    editArticledata = models.article.objects.get(articleid=request.POST['articleid'],
                                                                 authorid=request.POST['authorid'])
                    authorinfo = models.user.objects.get(id=editArticledata.authorid)
                    editArticledata.articletitle = request.POST['articletitle']
                    editArticledata.articlecontent = request.POST['articlecontent']
                    editArticledata.updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    editArticledata.save()
                    Articledata = {
                        "articleid": editArticledata.articleid,
                        "articletitle": editArticledata.articletitle,
                        "articlecontent": editArticledata.articlecontent,
                        "authorid": editArticledata.authorid,
                        "author": authorinfo.nickname,
                        "classifyid": editArticledata.classifyid,
                        "coverpicture": editArticledata.coverpicture,
                        "updatetime": editArticledata.updatetime,
                        "createdtime": editArticledata.createdtime
                    }
                    editarticle_data = {"code": "200", "msg": "Success！", "data": Articledata}
                    return HttpResponse(json.dumps(editarticle_data))
            except:
                editarticle_createdDataerror = {"code": "-10", "msg": "ERROR！", "data": {}}
                return HttpResponse(json.dumps(editarticle_createdDataerror))

        else:
            editarticle_tokenInvalid = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(editarticle_tokenInvalid))

    else:
        articledetails_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(articledetails_requesterror))


# 更换封面接口




# 获取用户信息接口
def requestuserinfo(request):
    if request.POST:
        if token(request.POST['token']):

            print(request.POST['userid'], request.POST['username'])
            try:
                userInfo = models.user.objects.get(id=request.POST['userid'], username=request.POST['username'],
                                                   userstatus='1')
                userInfodata = {
                    "id": userInfo.id,
                    "username": userInfo.id,
                    "realname": userInfo.realname,
                    "nickname": userInfo.nickname,
                    "phonenumber": userInfo.phonenumber,
                    "emailaddress": userInfo.emailaddress,
                    "head": userInfo.head,
                    "birthday": userInfo.birthday,
                    "useraddress": userInfo.useraddress,
                    "sex": userInfo.sex,
                    "userstatus": userInfo.userstatus,
                    "createdtime": userInfo.createdtime,
                    "updatetime": userInfo.updatetime,
                }
                return HttpResponse(json.dumps({"code": "200", "msg": "Success!", "dara": userInfodata}))
            except:
                requestuserinfo_notquery = {"code": "216", "msg": "数据未不存在", "data": {}}
                return HttpResponse(json.dumps(requestuserinfo_notquery))
        else:
            requestuserinfo_tokenInvalid = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(requestuserinfo_tokenInvalid))
    else:
        requestuserinfo_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(requestuserinfo_requesterror))


# 修改用户信息
def edituserinfo(request):
    if request.POST:
        if token(request.POST['token']):
            if request.POST['birthday'] != "":
                try:
                    userinfo = models.user.objects.get(id=request.POST['userid'],
                                                       username=request.POST['username'],
                                                       phonenumber=request.POST['phonenumber'],
                                                       userstatus='1'
                                                       )
                    # 更新数据库数据
                    userinfo.realname = request.POST['realname']
                    userinfo.nickname = request.POST['nickname']
                    userinfo.phonenumber = request.POST['phonenumber']
                    userinfo.emailaddress = request.POST['emailaddress']
                    userinfo.head = request.POST['head']
                    userinfo.birthday = request.POST['birthday']
                    userinfo.useraddress = request.POST['useraddress']
                    userinfo.sex = request.POST['sex']
                    userinfo.updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    userinfo.save()
                    userinfodata = {
                        "userid": userinfo.id,
                        "username": userinfo.username,
                        "realname": userinfo.realname,
                        "nickname": userinfo.nickname,
                        "phonenumber": userinfo.phonenumber,
                        "emailaddress": userinfo.emailaddress,
                        "head": userinfo.emailaddress,
                        "birthday": userinfo.birthday,
                        "useraddress": userinfo.useraddress,
                        "sex": userinfo.sex,
                        "updatetime": userinfo.updatetime,
                        "createdtime": userinfo.createdtime
                    }
                    print(userinfodata)
                    return HttpResponse(json.dumps({"code": "200", "msg": "Success!", "data": userinfodata}))
                except:
                    edituserinfo_createdDataerror = {"code": "-10", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(edituserinfo_createdDataerror))
            else:
                try:
                    userinfo = models.user.objects.get(id=request.POST['userid'],
                                                       username=request.POST['username'],
                                                       phonenumber=request.POST['phonenumber'],
                                                       userstatus='1'
                                                       )
                    # 更新数据库数据
                    userinfo.realname = request.POST['realname']
                    userinfo.nickname = request.POST['nickname']
                    userinfo.phonenumber = request.POST['phonenumber']
                    userinfo.emailaddress = request.POST['emailaddress']
                    userinfo.head = request.POST['head']
                    userinfo.birthday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    userinfo.useraddress = request.POST['useraddress']
                    userinfo.sex = request.POST['sex']
                    userinfo.updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    userinfo.save()
                    userinfodata = {
                        "userid": userinfo.id,
                        "username": userinfo.username,
                        "realname": userinfo.realname,
                        "nickname": userinfo.nickname,
                        "phonenumber": userinfo.phonenumber,
                        "emailaddress": userinfo.emailaddress,
                        "head": userinfo.emailaddress,
                        "birthday": userinfo.birthday,
                        "useraddress": userinfo.useraddress,
                        "sex": userinfo.sex,
                        "updatetime": userinfo.updatetime,
                        "createdtime": userinfo.createdtime
                    }
                    print(userinfodata)
                    return HttpResponse(
                        json.dumps({"code": "200", "msg": "Success,生日时间格式为空，已经修改为当前时间!", "data": userinfodata}))
                except:
                    edituserinfo_createdDataerror = {"code": "-10", "msg": "ERROR！", "data": {}}
                    return HttpResponse(json.dumps(edituserinfo_createdDataerror))
        else:
            requestedituserinfo_tokenInvalid = {"code": "-11", "msg": "token过期", "data": {}}
            return HttpResponse(json.dumps(requestedituserinfo_tokenInvalid))
    else:
        edituserinfo_requesterror = {"code": "-12", "msg": "请求方式错误！", "data": {}}
        return HttpResponse(json.dumps(edituserinfo_requesterror))
