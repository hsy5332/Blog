from django.shortcuts import render
from Blog import models
# Create your views here.

def index(request):
    user = models.user.objects.get(id=1)
    return render(request,'index.html',{"TEST":user})



def login(getusernmae,getpassword,gettoken):
    usernmae = models.user.objects.get(username=getusernmae)

    return "success"

