from django.shortcuts import HttpResponse
from .tasks import some_async_task
import time

# Create your views here.
def home(request):
    some_async_task.delay('This is new parameter')
    return HttpResponse('Hello')