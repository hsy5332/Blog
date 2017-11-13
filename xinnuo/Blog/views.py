from django.shortcuts import render
from Blog import models
from django.http import HttpResponse
import time
import json
# Create your views here.

def index(request):
    user = models.user.objects.get(id=1)

    return render(request,'index.html',{"TEST":user})



def login(request):
    if request.POST:
       try:
            if int(request.POST['token']) + 86400 < int(time.time()): #86400是一天的时间戳
                try:
                    userinfo = models.user.objects.get(username=request.POST['username'],password=request.POST['password'])
                    #判断用户信息是否在数据库中存在
                    return HttpResponse("Success！")
                    '''
                    #返回json字符串方法：            (实际开发可以不返回，前端根据userinfo取出对应value)
                    request_userinof = {
                                    'userid':userinfo.id,
                                    'username':userinfo.username,
                                    'phonenumber':userinfo.phonenumber,
                                    'code':'200',
                                    'status':"Success",
                            }
                    return HttpResponse(json.dumps(request_userinof)) 
                '''
                except:
                    return HttpResponse("用户名或密码错误！")
            else:
                return HttpResponse("token过期！")
       except:
            return HttpResponse("ERROR!")
    else:
        return HttpResponse("请求方式错误！")

#登录接口

def register(request):
    if request.POST:
        try:
            postUsername = models.user.objects.get(username=request.POST['username'])#这个就能判断用户名是否存在
            return HttpResponse("该用户名已经存在！")
        except:
            try:
                phonenumber = models.user.objects.get(phonenumber=request.POST['phonenumber'])
                return HttpResponse("该手机号已经使用了！")
            except:
                try:
                    phoneStatus = models.phone_status.objects.get(phonenumber=request.POST['phonenumber']) #判断手机号是否存在phone_status表中
                    if int(phoneStatus.status) == 1:#判断手机号是否被锁定
                            try:
                                phoneMessage = models.phone_message.objects.get(phonenumber=request.POST['phonenumber'],mcodestatus=1)#判断是否有短信验证码
                                return HttpResponse(phoneMessage.messagecode)
                            except:
                                return HttpResponse("没有获取到验证码，请重试。")
                    else:
                        return HttpResponse("该手机号已经被锁定，请解锁后再操作。")
                except:
                    try:
                        phoneMessage = models.phone_message.objects.get(phonenumber=request.POST['phonenumber'],
                                                                        mcodestatus=1)  # 判断是否有短信验证码
                        return HttpResponse(phoneMessage.messagecode)
                    except:
                        return HttpResponse("没有获取到验证码，请重试。")

    else:
        return HttpResponse("请求方式错误！")
#注册接口
