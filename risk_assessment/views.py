from django.shortcuts import render


def assessments(request):
    return render(request,'risk_assessment/assessments.html')
