from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def registryForm(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            messages.success(request, "Your account has been created successfully!")
            return redirect('bIn', user_id=user.id) 
    else:
        form = UserRegistrationForm()  

    return render(request, 'forms/signup.html', {'userreg': form})
