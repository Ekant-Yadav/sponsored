from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def events(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'organiser.html')
