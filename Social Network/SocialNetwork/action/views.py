from django.shortcuts import render
from .models import Action

# Create your views here.
def feed(request):
    feeds = Action.objects.prefetch_related('user').exclude(user=request.user)
    print(feeds)
    return render(request, 'action/feed.html', {'feeds':feeds})