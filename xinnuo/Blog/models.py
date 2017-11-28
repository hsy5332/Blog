from django.db import models

#article table 文章表
class article(models.Model):
    articleid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='articleid')
    authorid = models.CharField(max_length=11,null=False)
    classifyid =models.CharField(max_length=11,null=False)
    articletitle = models.TextField(null=False)
    articlecontent = models.TextField(null=False)
    articlestatus = models.CharField(max_length=3)
    coverpicture = models.CharField(max_length=50)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')

    #def  __str__(self):
        #return self.articletitle #Python方法，调取函数，返回对象为articletitle，这样页面不会显示object


#article_classify 文章分类表
class article_classify(models.Model):
    classifyid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='classifyid')
    classifyname = models.CharField(max_length=11)
    createrClassifyid = models.CharField(max_length=11)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')
    def __str__(self):
        return self.classifyname


#collection_record 收藏记录表
class collection_record(models.Model):
    collectionid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='collectionid')
    collentionUserid = models.CharField(max_length=11)
    collentionarticleid = models.CharField(max_length=11)
    iscollection = models.CharField(max_length=4)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')


#comment 评论表
class comment(models.Model):
    commentid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='commentid')
    createrid = models.CharField(max_length=11)
    articleid = models.CharField(max_length=11)
    commentcontent = models.TextField(null=True)
    isdel = models.CharField(max_length=4)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')


#count 统计表
class count(models.Model):
    countid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='countid')
    articleid = models.CharField(max_length=11)
    readUserid = models.CharField(max_length=11)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')


#leaving_message 留言内容表
class leaving_message(models.Model):
    leavingid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='leavingid')
    createrid = models.CharField(max_length=11)
    favoreeid = models.CharField(max_length=11)
    leavingcontent = models.TextField(null=False)
    isdel = models.CharField(max_length=4)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')


#mail 邮箱验证表
class mail(models.Model):
    emailid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='emailid')
    email = models.CharField(max_length=50)
    emailcode = models.CharField(max_length=20)
    ecodestatus = models.CharField(max_length=4)
    usein = models.CharField(max_length=4)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')


#phone_message 手机短信表
class phone_message(models.Model):
    messageid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='messageid')
    phonenumber = models.CharField(max_length=14)
    messagecode = models.CharField(max_length=20)
    mcodestatus = models.CharField(max_length=4)
    usein = models.CharField(max_length=4)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')
    def __int__(self):
        return int.phonenumber

#phone_status手机状态表
class phone_status(models.Model):
    phoneid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='phoneid')
    phonenumber = models.CharField(max_length=14)
    status = models.CharField(max_length=4)


#user  用户信息表
class user(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    realname = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=14)
    emailaddress = models.CharField(max_length=50)
    head = models.CharField(max_length=50)
    birthday = models.DateTimeField(default='auto_now_add')
    useraddress = models.CharField(max_length=100)
    sex = models.CharField(max_length=4)
    userstatus = models.CharField(max_length=4)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')


#主页配置
class link_configure(models.Model):
    linkid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='linkid')
    url = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)
    configurestatus = models.CharField(max_length=4)
    position = models.CharField(max_length=4)
    number = models.CharField(max_length=4)
    createdtime = models.DateTimeField(default='auto_now_add')
    updatetime = models.DateTimeField(default='auto_now')
