from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserProfileForm

from django.contrib import messages
def bmiIn(request, user_id):
    user = User.objects.get(id=user_id) 
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user  
            profile.save()
            
            return redirect('signin')
       
    else:
        form = UserProfileForm()

    return render(request, 'forms/bmiinput.html', {'form': form})
