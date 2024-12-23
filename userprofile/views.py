from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from bmiInput.models import UserProfile

# View to display profile information
@login_required
def view_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'userprofile/view_profile.html', {
        'user': request.user,
        'user_profile': user_profile,
    })

# View to edit profile information
@login_required
def edit_profile(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)  # Ignore `created` using `_`

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)  # Handle file uploads

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('view')  # Redirect to profile view after saving
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'userprofile/edit_profile.html', {
        'user': request.user,
        'user_form': user_form,
        'profile_form': profile_form,
    })
