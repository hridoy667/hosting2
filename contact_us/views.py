from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback

# Create your views here.
def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        feedback = Feedback.objects.create(name=name, email=email, message=message)
        feedback.save()

        
        messages.success(request, "Thank you for your feedback!")

        return redirect('cont') 

    return render(request, 'contact.html')