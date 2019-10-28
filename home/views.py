# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):
    site = 'https://blackwiz4rd.github.io'
    return redirect(site)

def resume(request):
    drive = 'https://drive.google.com/drive/folders/1I4cr069Hqpecq6MbcY5tIQ18dPuHCusB?usp=sharing'
    return redirect(drive)

def transcript(request):
    drive = 'https://drive.google.com/drive/folders/1I4cr069Hqpecq6MbcY5tIQ18dPuHCusB?usp=sharing'
    return redirect(drive)

def thesis(request):
    site = 'https://blackwiz4rd.github.io/projects/2018-07-16-dash/'
    return redirect(site)

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
