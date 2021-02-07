from django.shortcuts import HttpResponse, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from .forms import BasicForm
from .models import Blog


#  If the request method is not in http_method_names then it will call http_method_not_allowed method.
def home(request):
    html = '<h1>Homepage</h1>'
    return HttpResponse()

class Home(TemplateView):
    template_name = 'home.html'
    def get(self, request):
        return render(request, 'home.html')


class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["var"] = 'This is a context data'
        print(context)
        return context

class Redirect(RedirectView):
    pattern_name = 'myapp:redirect_to_me'
    def get_redirect_url(self, *args, **kwargs):
        # logic to implement like no. of clicks in the link
        return super().get_redirect_url(*args, **kwargs)

class RedirectedToMe(TemplateView):
    template_name = 'redirected.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"

class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"
    context_object_name = 'blogs'
    paginate_by = 10
    allow_empty = True
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class BasicFormView(FormView):
    template_name = 'form.html'
    form_class = BasicForm
    success_url = reverse_lazy('myapp:home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    def form_valid(self, form):
        print('valid')
        return super().form_valid(form)

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title']
    success_url = reverse_lazy('myapp:home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.object)
        print(context)
        return context
    
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'another_title']
    template_name = 'myapp/blog_form.html'
    success_url = reverse_lazy('myapp:home')


class DeleteObject(DeleteView):
    model = Blog
    success_url = reverse_lazy('myapp:home')
    template_name_suffix = '_confirm_delete'
