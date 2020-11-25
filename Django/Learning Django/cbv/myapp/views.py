from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.
class homepage(View):
    def get(self, request):
        html = '''<h1><a href="homepagehtml/"><button>Go to html home page</button></a><h1><H1>This is a home page from CBV</H1>'''
        return HttpResponse(html)

class homepagehtml(TemplateView):
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected'] = "This is home page from homepage.html"
        return context