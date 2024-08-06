from django.shortcuts import render,redirect
from django.urls import reverse
from django.db import connection
from datetime import datetime
import os
from django.conf import settings
from .models import *
from django import forms
from django.contrib.auth import login,authenticate
from appname.models import CustomUser
def log_in(request):
    context={} 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if CustomUser.objects.filter(username=username).exists():
                user = CustomUser.objects.get(username=username)
                if user.password == password:
                    user = authenticate(request, username=username, password=password)
                    login(request,user)
                    print(user)
                    #  for redirect dashboard page
                    return redirect('index')
                else:
                    context['err'] = 'Login yoki parol xato'
        
       
    return render(request, 'login.html',context)