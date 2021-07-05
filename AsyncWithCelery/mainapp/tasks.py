from celery import shared_task
from django.core.mail import send_mail

@shared_task
def some_async_task(some_parameter):
    subject = 'welcome to Django world'
    message = f'Hi, thank you for learning Django.'
    email_from = 'from@mail.com'
    recipient_list = ['to@mail.com', ]
    send_mail( subject, message, email_from, recipient_list )    
    print('Printing - ',some_parameter)