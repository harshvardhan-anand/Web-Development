from django.shortcuts import render
from . import form
from django import forms
from form.form import NewUser

# Create your views here.
def homepage(response):
    return render(response, 'homepage/homepage.html')

# Validation of form
def form_data(response):
    form_elements = form.FormElements()
    print()
    # print(form_elements)  # this is html of form
    if response.method == 'POST':
        postdata = form.FormElements(response.POST)
        # print(postdata)  # This will print the html returned after clicking the submit button

        print(postdata.is_valid()) 
        # This will only be true when all the data are valid and in correct form (eg. email without .com is not accepted)

        # untill you check is_valid you cannot use .cleaned_data
        if postdata.is_valid():
            print(postdata.cleaned_data['name'])
            print(postdata.cleaned_data['botcatcher'])
        print()
    return render(response, 'form/form.htm', {'form_elements':form_elements})

# For saving the data into database from the form
def newusers(response):
    form_elements = NewUser()
    context = {'form':form_elements}
    if response.method=='POST':
        form = NewUser(response.POST)
        # Saving post data to database
        if form.is_valid():
            form.save(commit=True)
            return homepage(response)  # after filling the form return to homepage
        else:
            raise forms.ValidationError("This is a validation Error")
    return render(response, "users/users.html", context=context)
