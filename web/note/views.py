from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def main_view(request):
    
    return HttpResponse("메인 화면")

def show_user(request):
    
    return render()