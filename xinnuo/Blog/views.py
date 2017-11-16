import time
import json
import pdb
#pdb.set_trace()
from django.http import HttpResponse
from django.shortcuts import render

from Blog import models

'''
接口规范：
返回数据
失败：
{
    "code":"",
    "msg" : "",
}

{   
    "code" : "",
    "msg" : "",
    "data1" : "data1",
    data2" : "data2",
    data3" : "data3"
}
code = 200 成功
code = -10 参数未传全
code = 201 用户名或密码错误
code = -11 token过期
code = -12 请求方式错误
code = 202 用户名已经存在
code = 203 该手机号已经使用了
code = 204 没有获取到手机验证码，请重试 
code = 205 该手机号已经被锁定，请解锁后再操作。
code = 206 请输入正确的手机号
code = 207 没有获取到邮箱验证码，请重试。
code = 208 请输入正确的邮箱地址！
code = 209 请输入邮箱或者手机号。
'''


def index(request):
    user = models.user.objects.get(id=1)

    return render(request, 'index.html', {"TEST": user})


def login(request):
    if request.POST:
        try:
            if int(request.POST['token']) + 86400 > int(time.time()):  # 86400是一天的时间戳
                try:
                    userinfo = models.user.objects.get(username=request.POST['username'],
                                                       password=request.POST['password'])
                    # 判断用户信息是否在数据库中存在
                    # return HttpResponse("Success！")

                    # 返回json字符串方法：            (实际开发可以不返回，前端根据userinfo取出对应value)
                    login_userinfo = {
                        'code': '200',
                        'msg': 'Success！',
                        'data': {'userid': userinfo.id, 'username': userinfo.username,
                                 'phonenumber': userinfo.phonenumber, }  # 实际开发中，可直接返回一个字典
                    }
                    return HttpResponse(json.dumps(login_userinfo))
                except:
                    login_userInfoerror = {'code': '201', 'msg': '用户名或密码错误！', 'data': ''}
                    return HttpResponse(json.dumps(login_userInfoerror))
            else:
                login_tokenInvalid = {'code': '-11', 'msg': '', 'data': 'token过期'}
                return HttpResponse(json.dumps(login_tokenInvalid))
        except:
            login_tokenError = {'code': "-10", 'msg': 'ERROR', 'data': ''}
            return HttpResponse(json.dumps(login_tokenError))
    else:
        login_requesterror = {'code': '-12', 'msg': '请求方式错误！', 'data': ''}
        return HttpResponse(json.dumps(login_requesterror))


# 登录接口

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
                                try:
                                    phoneMessage = models.phone_message.objects.get(
                                        phonenumber=request.POST['phonenumber'], mcodestatus=1,
                                        usein='R')  # 判断phoneMessage是否有短信验证码
                                    register_messagecode = {'code': '200', 'msg': 'Success！',
                                                            'data': phoneMessage.messagecode}
                                    return HttpResponse(json.dumps(register_messagecode))
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
                                register_messagecode = {'code': '200', 'msg': 'Success！',
                                                            'data': phoneMessage.messagecode}
                                return HttpResponse(json.dumps(register_messagecode))
                            except:
                                register_notReceivedcode = {'code': '204', 'msg': '没有获取到手机验证码，请重试。',
                                                            'data': ''}  # Receive收到
                                return HttpResponse (json.dumps(register_notReceivedcode))
                    else:
                        register_Phonewrongful = {'code': '206', 'msg': '请输入正确的手机号！', 'data': ''}  # wrongful不合法
                        return HttpResponse(json.dumps(register_Phonewrongful))
                except:
                    try:
                        if "@" in request.POST['email']:
                            try:
                                eMail = models.mail.objects.get(email=request.POST['email'], ecodestatus=1 ,usein = 'R')  # 判断是否有验证码
                                register_mailcode = {'code': '200', 'msg': 'Success', 'data': eMail.emailcode}
                                return HttpResponse(json.dumps(register_mailcode))
                            except:
                                register_notReceivedMailcode = {'code': '207', 'msg': '没有获取到邮箱验证码，请重试。',
                                                                'data': ''}
                                return HttpResponse(json.dumps(register_notReceivedMailcode))
                        else:
                            register_mailwrongful = {'code': '208', 'msg': '请输入正确的邮箱地址！', 'data': ''}
                            return HttpResponse(json.dumps(register_mailwrongful))
                    except:
                        register_mailPhonewrongful = {'code': '209', 'msg': '请输入邮箱或者手机号！', 'data': ''}
                        return HttpResponse(json.dumps(register_mailPhonewrongful))

    else:
        register_requesterror = {'code': '-12', 'msg': '请求方式错误！', 'data': ''}
        return HttpResponse(json.dumps(register_requesterror))


# 注册接口
'''
def forgotpassword(request):
    if request.POST:
        try:
            forgotusername = models.user.objects.get(username=request.POST['username'],)

        except:
            print("用户错误")
'''
