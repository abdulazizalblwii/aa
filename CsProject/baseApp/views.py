from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


def home(request):
    return render(request, 'home.html',{})

def FQA(request):
    return render(request, 'FQA.html',{})

def CoursesList(request):
    return render(request, 'CoursesList.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have logged in succsecfully"))
            return redirect('home')
        else:
            messages.success(request, ("Error, please try again"))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have succsecfully logged out"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if  form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # login user>>
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("# You have Registered Successfully"))
            return redirect('home')
        else:
            messages.success(request, ("#There error in registering, please try agin "))
            return redirect('register')
    else:
        return render(request, 'register.html',{'form':form})