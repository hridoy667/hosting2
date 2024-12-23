from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# Create your views here.
def signin(request):
    return render(request,'forms/signin.html')

def login_user(request):
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('dashbord')
        else:
            messages.error(request, "Bad username or password!")
            return redirect('signin')
    else:
        return render(request, 'forms/signin.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You've successfully logged out")
    return redirect('signin')  # Redirects to signin page after logout
