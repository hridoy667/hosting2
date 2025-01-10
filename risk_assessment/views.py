from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required
def assessments(request):
    return render(request,'risk_assessment/assessments.html')
