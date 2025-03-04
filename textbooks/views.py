from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        
        user = authenticate(request, username=user_id, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("available_textbooks") 
        else:
            messages.error(request, "Invalid ID or password")
            
    return render(request, "login.html")


def available_textbooks(request):
    return render(request, "available_textbooks.html")


def home(request):
    return render(request,"home.html")

def COMP250(request):
    return render (request,'comp250.html')

def AI101(request):
    return render (request,'ai101.html')

def ML202(request):
    return render (request,'ml202.html')

def COMP312(request):
    return render (request,'comp312.html')

