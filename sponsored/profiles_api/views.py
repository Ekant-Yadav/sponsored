from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import login, logout, authenticate

def loginuser(request,slug):
    context={
        "slug":slug
    }
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        profile=slug
        User= authenticate(username=username, password=password)
        login(request, User)
        if (User is not None):
            return redirect("/organiser")
        else:
           return render(request, 'login.html')
    return render(request,'login.html',context)

def signupuser(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        email= request.POST.get('email')
        location= request.POST.get('location')
        profile = request.POST.get('profile')

        myuser=User.objects.create_user(username,email,password)
        myuser.set_password(password)
        myuser.save()

        userprofile = UserProfile(user=myuser, location=location, profile=profile)
        userprofile.save()

        user= authenticate(username=username, password=password)
        login(request, user)
        return redirect("/organiser")
    return render(request,'signup.html')
