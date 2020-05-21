from django.shortcuts import render
from form.form import UserForm, UserProfileInfo

# Create your views here.
def homepage(request):
    return render(request, 'homepage/homepage.html')

def register(request):
    user_form = UserForm()
    profile_info = UserProfileInfo()
    print('\n', request.method,)
    if request.method == 'POST':
        filled_userform = UserForm(request.POST)
        filled_profileinfo = UserProfileInfo(request.POST)
        # print(filled_profileinfo)
        # print(filled_userform.is_valid() and filled_profileinfo.is_valid())
        if filled_userform.is_valid() and filled_profileinfo.is_valid():
            username = filled_userform.save(commit=True)
            username.set_password(username.password)
            username.save()  # by default commit is true
            print(username, '\n')

            profile = filled_profileinfo.save(commit=False)
            profile.user = username  # Here we have created the one to one relation.
            profile.save()
            print(request.FILES )
        else:
            print(filled_profileinfo.errors,'\n', filled_userform.errors)
    context = {'form':user_form, 'profile_info':profile_info}
    return render(request, 'register/register.html',        
                    context=context)