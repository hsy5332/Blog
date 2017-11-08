from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world") #测试返回代码

