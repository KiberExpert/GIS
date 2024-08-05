from django.shortcuts import render,redirect
from django.urls import reverse
from django.db import connection
from datetime import datetime
import os
from django.conf import settings
from .models import *
from django import forms

def index(request):
    context={
    }
    return render(request, 'index.html',context)