from django.conf.urls import url
from Blog import views

urlpatterns = [
    url(r'^index', views.index),
    url(r'^login', views.login),  # 登录接口
    url(r'^register', views.register),  # 注册接口
    url(r'^forgotpassword', views.forgotpassword),  # 忘记密码接口
    url(r'^achievemessagecode', views.achievemessagecode),  # 手机验证码获取接口（注册、忘记密码、修改密码）
    url(r'^configure', views.configure),  # home配置接口
    url(r'^search', views.search),  # 搜索接口
    url(r'^articledetails', views.details),  # 文章详情
    url(r'^createarticle', views.createarticle),  # 创建文章
    url(r'^editarticle', views.editarticle),  # 编辑文章接口
    url(r'^requestuserinfo',views.requestuserinfo), #获取用户信息
    url(r"^edituserinfo",views.edituserinfo),#修改用户信息
    #评论、收藏、
]
