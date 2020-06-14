from django.shortcuts import render
from . import OutBreakData
import time
# Also remember to do tasks in threads so that processing time is low

# Create your views here.
def homepage(request):
    u = OutBreakData.Update()
    data = u.data()
    context = {'Total':data[0], 'New':data[1],'Active':data[2]}
    return render(request, 'homepage/homepage.html', context)