# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):
    return render(request, 'home/index.html')

def resume(request):
    return render(request, 'home/resume.html')

def transcript(request):
    return render(request, 'home/transcript.html')

def thesis(request):
    return render(request, 'home/thesis.html')

def career(request):
    return render(request, 'home/career.html')

def projects(request):
    return render(request, 'home/projects.html')

def contacts(request):
    return render(request, 'home/contacts.html')

def email_sent(request):
    return render(request, 'home/email_sent.html')

def email_unsuccessful(request):
    return render(request, 'home/email_unsuccessful.html')

def send_email(request):
	if request.method == 'POST' and request.POST.get("subject", "") != "" and request.POST.get("content", "") != "" and validateEmail(request.POST.get("email", "")):
		send_mail(
		    request.POST.get("subject", ""),
		    request.POST.get("content", ""),
		    request.POST.get("email", ""),
		    ['blackwiz4rd@gmail.com'],
		    fail_silently=False,
		)
		return email_sent(request)
	else:	
		return email_unsuccessful(request)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False
