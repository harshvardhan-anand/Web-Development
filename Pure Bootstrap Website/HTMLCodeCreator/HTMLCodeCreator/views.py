from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER

def mail(request):
    subject = 'SUBJECT'
    message = 'Hope you are enjoying your Django Tutorials'
    recipient = 'mohan@gmail.com'
    send_mail(subject, 
        message, EMAIL_HOST_USER, [recipient], fail_silently = False)
    return HttpResponse('Email sent!!')

def home(request):
    return HttpResponse('<a href="mail">Send Mail</a>')