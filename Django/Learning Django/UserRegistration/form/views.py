from django.shortcuts import render
from form.form import UserForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage/homepage.html')

def register(request):
    form = UserForm()
    context = {'form':form}
    print(form)
    return render(request, 'register/register.html',        
                    context=context)