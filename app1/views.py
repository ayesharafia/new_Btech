from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import usersignup
from django.contrib import messages

# def brian(request):
#     return HttpResponse("Hello, brian!")

def user_signup(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('pswd'):
            saverecord = usersignup()
            saverecord.username.request.POST.get('username')
            saverecord.pswd.request.POST.get('pswd')
            saverecord.save()
            messages.success(request,"Signup successfull")
            return render(request,'app1/modules/signup/signup.html')
            
    else:
        return render(request,'app1/modules/signup/signup.html')


def login(request):
    return render(request, "app1/modules/login/login.html")
    # return HttpResponse("Login")

def signup(request):
    return render(request, "app1/modules/signup/signup.html")
# Create your views here.
