

# Create your views here.
from multiprocessing import context
from pydoc import describe
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def  home(request):
    return render(request,'home1.html')


def usercreate(request):
    if request.method =='POST':
        username=request.POST['username']
       
        email=request.POST['email']
      
        password=request.POST['password']
       
    
        
        user=User.objects.create_user(
            username=username,
            email=email,
              password=password)
        user.save()
        
            
        
    return redirect('home')

def SLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            
            auth.login(request,user)
            return redirect('home')#index
        else:
            return redirect('home')
    else:
        return redirect('home')
def  log(request):
    return render(request,'login.html')
def  sinin(request):
    return render(request,'signup.html')
def  book(request):
    return render(request,'Book.html')
def  ht(request):
    return render(request,'hotel1.html')
def  htt(request):
    return render(request,'hotel2.html')
def  uk(request):
    return render(request,'uk.html')
